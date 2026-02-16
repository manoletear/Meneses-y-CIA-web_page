\"\"\"
Parser para comprobantes de registro de la Dirección del Trabajo (DT)
Basado en casos reales documentados
\"\"\"

import re
import hashlib
import pdfplumber
from typing import Dict, Optional

class DTParser:
    \"\"\"Extrae datos de comprobantes PDF de la DT\"\"\"
    
    def __init__(self, pdf_path: str):
        self.pdf_path = pdf_path
        self.texto = self._extraer_texto()
        self.hash = self._calcular_hash()
    
    def _extraer_texto(self) -> str:
        \"\"\"Extrae todo el texto del PDF\"\"\"
        texto_completo = \"\"
        with pdfplumber.open(self.pdf_path) as pdf:
            for pagina in pdf.pages:
                texto_completo += pagina.extract_text() or \"\"
        return texto_completo
    
    def _calcular_hash(self) -> str:
        \"\"\"Calcula hash SHA-256 del archivo\"\"\"
        sha256 = hashlib.sha256()
        with open(self.pdf_path, 'rb') as f:
            for bloque in iter(lambda: f.read(4096), b''):
                sha256.update(bloque)
        return sha256.hexdigest()
    
    def extraer_numero_operacion(self) -> Optional[str]:
        \"\"\"Extrae el número de operación del comprobante\"\"\"
        # Patrones comunes en comprobantes DT
        patrones = [
            r'N[°º]\s*(\d+)',
            r'Número de operación[:\s]*(\d+)',
            r'Operación[:\s]*(\d+)'
        ]
        
        for patron in patrones:
            match = re.search(patron, self.texto, re.IGNORECASE)
            if match:
                return match.group(1)
        return None
    
    def extraer_ruts(self) -> Dict[str, Optional[str]]:
        \"\"\"Extrae RUTs del empleador y trabajador\"\"\"
        # Buscar RUTs con formato chileno (XX.XXX.XXX-X o XXXXXXXXX-X)
        patron_rut = r'(\d{1,2}\.\d{3}\.\d{3}[-][0-9Kk])'
        ruts = re.findall(patron_rut, self.texto)
        
        resultado = {
            'empleador': None,
            'trabajador': None
        }
        
        # Asumir que el primer RUT es del empleador, el segundo del trabajador
        if len(ruts) >= 1:
            resultado['empleador'] = ruts[0]
        if len(ruts) >= 2:
            resultado['trabajador'] = ruts[1]
            
        return resultado
    
    def extraer_fecha_registro(self) -> Optional[str]:
        \"\"\"Extrae fecha de registro\"\"\"
        patrones_fecha = [
            r'Fecha[:\s]*(\d{2}[/-]\d{2}[/-]\d{4})',
            r'Registrado el[:\s]*(\d{2}[/-]\d{2}[/-]\d{4})'
        ]
        
        for patron in patrones_fecha:
            match = re.search(patron, self.texto, re.IGNORECASE)
            if match:
                return match.group(1)
        return None
    
    def obtener_todos_datos(self) -> Dict:
        \"\"\"Obtiene todos los datos extraídos\"\"\"
        return {
            'hash': self.hash,
            'numero_operacion': self.extraer_numero_operacion(),
            'ruts': self.extraer_ruts(),
            'fecha_registro': self.extraer_fecha_registro()
        }

# Ejemplo de uso
if __name__ == \"__main__\":
    parser = DTParser(\"ejemplo_comprobante_dt.pdf\")
    datos = parser.obtener_todos_datos()
    print(datos)
