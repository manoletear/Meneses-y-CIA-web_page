# Prompts para Investigación Normativa en Antigravity

## Prompt 1: Investigación de Ley Específica

\`
Actúa como un experto en legislación laboral chilena. Analiza la Ley [NÚMERO] y genera un resumen estructurado con:

1. Objetivo principal de la ley
2. Artículos más relevantes para un software de RR.HH.
3. Requisitos técnicos específicos (campos obligatorios, plazos, formatos)
4. Sanciones por incumplimiento
5. Enlaces a fuentes oficiales
6. Casos de error comunes (basado en fiscalizaciones reales)

Formato de salida: Markdown con tablas para los requisitos técnicos.
\`

## Prompt 2: Interpretación de Dictamen Técnico

\`
Eres un asesor técnico-legal. El Dictamen ORD. N°2927/58 de la DT establece requisitos para sistemas digitales. 
Extrae y explica en lenguaje para desarrolladores:

- ¿Qué es un "checksum" según la DT y cómo implementarlo?
- ¿Qué constituye "evidencia válida" para una fiscalización?
- Requisitos de arquitectura (logs, trazabilidad, integridad)
- Diagrama de flujo sugerido

Incluye referencias a los artículos específicos del dictamen.
\`

## Prompt 3: Actualización Normativa (Reforma de Pensiones)

\`
Investiga la Reforma de Pensiones 2025-2026 en Chile. Crea una tabla comparativa con:

| Concepto | Antes de Reforma | Desde Ago 2025 | 2026-2033 (progresión) |
|----------|------------------|----------------|------------------------|
| Cotización empleador | 0% | 1% | Hasta 7% |
| Distribución | - | 0.1% cuenta indv, 0.9% FAPP | Variable |
| Campo nuevo en planilla | No | Tipo de jornada (completa/parcial) | Se mantiene |

Fuentes principales: ChileAtiende, Ministerio de Hacienda, Previred.
\`
"@ | Out-File -FilePath training\prompts\01-investigacion.md -Encoding utf8

@"
# Prompts para Generación de Código en Antigravity

## Prompt 1: Validador de Reglas DT

\`
Genera una función en JavaScript que valide un contrato contra las reglas de la Dirección del Trabajo. 
Debe incluir:

- Validación de RUT (formato y dígito verificador)
- Validación de jornada parcial (no puede tener 44h semanales)
- Validación de fecha para Ley 21.561 (44h solo desde 26-abr-2024)
- Validación para casa particular (códigos 191-1 y 191-2)

La función debe retornar un array de errores con: campo, mensaje y casoAsociado (ej. "Caso 2").
Incluye comentarios que expliquen cada validación.
\`

## Prompt 2: Parser de PDF de DT

\`
Crea un script en Python usando pdfplumber que extraiga de un comprobante PDF de la DT:

- Número de operación
- RUT del empleador
- RUT del trabajador
- Fecha de registro
- Hash SHA-256 del archivo

Incluye manejo de errores y casos donde no se encuentren los datos.
Documenta el código con ejemplos de uso.
\`

## Prompt 3: Generador de Nómina Previred (105 campos)

\`
Escribe una clase en Python que genere el archivo CSV de 105 campos para Previred, 
incorporando los cambios de la Reforma de Pensiones 2025:

- Nueva cotización del empleador (1% desde ago-2025)
- Campo "tipo_jornada" (completa/parcial)
- Distribución entre cuenta individual y FAPP

La clase debe tener métodos para calcular los montos y generar el archivo.
Incluye validaciones de datos de entrada.
\`
"@ | Out-File -FilePath training\prompts\02-codigo.md -Encoding utf8

@"
# Prompts para Creación de Workflows en Antigravity

## Prompt 1: Workflow de Monitoreo Normativo

\`
Diseña un workflow en formato YAML para Antigravity que se ejecute semanalmente y realice:

Agente 1 (Investigador):
- Revisa los 5 enlaces de prioridad máxima (ChileAtiende, Ministerio Hacienda)
- Detecta cambios en textos, fechas o requisitos
- Genera resumen de cambios

Agente 2 (Analista de Impacto):
- Toma el resumen del Agente 1
- Evalúa impacto en módulos de Poppins (validadores, generador de nóminas, UI)
- Genera lista de tareas técnicas priorizadas

Agente 3 (Documentador):
- Actualiza CHANGELOG-NORMATIVO.md
- Crea un artifact con el informe completo
- Envía notificación al equipo

El workflow debe incluir triggers, agentes, tareas y artifacts de salida.
\`

## Prompt 2: Workflow de Onboarding de Nuevo Empleado

\`
Crea un workflow que orqueste 4 agentes en paralelo para el onboarding de un nuevo trabajador:

Agente Normativo: Verifica tipo de contrato y reglas aplicables según DT
Agente de Documentos: Genera borrador de contrato con datos ingresados
Agente Previred: Calcula cotizaciones según jornada (incluyendo nueva cotización 2025)
Agente UI: Actualiza la interfaz con resultados y genera resumen para el usuario

Define la comunicación entre agentes y los artifacts que debe producir cada uno.
\`

## Prompt 3: Workflow de Simulación de Fiscalización

\`
Diseña un workflow para autoevaluación de cumplimiento:

1. Toma un contrato de prueba
2. Ejecuta todas las validaciones DT (usando el validador existente)
3. Consulta pagos en Previred (simulado)
4. Genera informe de riesgos con:
   - Posibles multas según tipo de infracción
   - Recomendaciones de corrección
   - Checklist de documentos que debería presentar

El informe debe ser legible para el cliente final (no técnico).
\`
"@ | Out-File -FilePath training\prompts\03-workflows.md -Encoding utf8

# ===== RESEARCH =====
@"
# Enlaces Oficiales - Investigación

## Dirección del Trabajo
- Código del Trabajo: https://www.dt.gob.cl/portal/1628/w3-propertyvalue-22293.html
- Buscador de Dictámenes: https://www.dt.gob.cl/portal/1628/w3-propertyvalue-23058.html
- Centro de Consultas: https://www.dt.gob.cl/portal/1628/w3-propertyvalue-181481.html
- Mi DT - Ingreso: https://www.dt.gob.cl/portal/1628/w3-article-116464.html
- Certificado Indisponibilidad: https://www.dt.gob.cl/portal/1626/w3-article-127352.html

## Reforma de Pensiones
- Aportes del empleador: https://www.chileatiende.gob.cl/fichas/130987-aportes-del-empleador-al-sistema-de-pensiones
- Casa Particular: https://www.chileatiende.gob.cl/fichas/133768-nueva-cotizacion-para-empleadores-de-personas-trabajadoras-de-casa-particular
- Portal Reforma: https://previsionsocial.gob.cl/pensiones-para-chile/
- Seguro Social: https://www.chileatiende.gob.cl/fichas/130459

## Previred
- Portal: https://www.previred.com/
- FAQ Empresas: https://www.previred.com/empresas/preguntas-frecuentes/
- Quiénes Somos: https://www.previred.com/quienes-somos/

## Leyes (búsqueda en Ley Chile)
- Ley 20.786: https://www.bcn.cl/leychile (buscar Ley 20786)
- Ley 21.561: https://www.bcn.cl/leychile (buscar Ley 21561)
- Ley 19.728: https://www.bcn.cl/leychile (buscar Ley 19728)
