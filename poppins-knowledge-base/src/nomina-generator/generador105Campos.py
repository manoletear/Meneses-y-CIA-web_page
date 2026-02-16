\"\"\"
Generador de archivo de 105 campos para Previred
Basado en la Reforma de Pensiones 2025-2026
\"\"\"

import csv
from typing import List, Dict
from datetime import datetime

class GeneradorNominaPrevired:
    \"\"\"Genera archivo CSV con estructura de 105 campos para Previred\"\"\"
    
    def __init__(self):
        self.encabezado = self._generar_encabezado()
    
    def _generar_encabezado(self) -> List[str]:
        \"\"\"Genera los nombres de los 105 campos\"\"\"
        # Esto es una simplificación - los nombres reales deben obtenerse de Previred
        campos = []
        for i in range(1, 106):
            campos.append(f\"campo_{i:03d}\")
        return campos
    
    def _calcular_nueva_cotizacion(self, renta_imponible: float, tipo_jornada: str) -> Dict:
        \"\"\"
        Calcula la nueva cotización del empleador según Reforma 2025
        A partir de agosto 2025: 1% (0.1% a cuenta individual, 0.9% a FAPP)
        \"\"\"
        # Porcentaje base desde agosto 2025
        porcentaje_total = 0.01  # 1%
        
        monto_total = renta_imponible * porcentaje_total
        monto_cuenta_individual = renta_imponible * 0.001  # 0.1%
        monto_fapp = renta_imponible * 0.009  # 0.9%
        
        return {
            'monto_total': round(monto_total, 0),
            'monto_cuenta_individual': round(monto_cuenta_individual, 0),
            'monto_fapp': round(monto_fapp, 0),
            'tipo_jornada': tipo_jornada
        }
    
    def generar_fila(self, trabajador: Dict) -> List:
        \"\"\"
        Genera una fila del archivo de 105 campos
        trabajador debe contener: rut, nombres, renta, tipo_jornada, etc.
        \"\"\"
        fila = [''] * 105
        
        # Campos básicos (índices de ejemplo - deben ajustarse)
        fila[0] = trabajador.get('rut', '')
        fila[1] = trabajador.get('nombres', '')
        fila[2] = trabajador.get('apellidos', '')
        fila[3] = str(trabajador.get('renta_imponible', 0))
        
        # Nuevos campos de la Reforma 2025
        cotizacion = self._calcular_nueva_cotizacion(
            trabajador.get('renta_imponible', 0),
            trabajador.get('tipo_jornada', 'completa')
        )
        
        fila[4] = str(cotizacion['monto_total'])  # Total nueva cotización
        fila[5] = cotizacion['tipo_jornada']      # Tipo de jornada (completa/parcial)
        fila[6] = str(cotizacion['monto_cuenta_individual'])  # A cuenta individual
        fila[7] = str(cotizacion['monto_fapp'])   # A FAPP
        
        return fila
    
    def generar_archivo(self, trabajadores: List[Dict], nombre_archivo: str):
        \"\"\"Genera archivo CSV con todos los trabajadores\"\"\"
        with open(nombre_archivo, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(self.encabezado)
            
            for trabajador in trabajadores:
                writer.writerow(self.generar_fila(trabajador))
        
        print(f\"Archivo generado: {nombre_archivo}\")

# Ejemplo de uso
if __name__ == \"__main__\":
    generador = GeneradorNominaPrevired()
    
    trabajadores_ejemplo = [
        {
            'rut': '12.345.678-5',
            'nombres': 'JUAN',
            'apellidos': 'PEREZ GONZALEZ',
            'renta_imponible': 800000,
            'tipo_jornada': 'completa'
        },
        {
            'rut': '23.456.789-0',
            'nombres': 'MARIA',
            'apellidos': 'RODRIGUEZ SILVA',
            'renta_imponible': 450000,
            'tipo_jornada': 'parcial'
        }
    ]
    
    generador.generar_archivo(trabajadores_ejemplo, \"nomina_ejemplo.csv\")
