# Glosario Crítico Poppins

## Términos Dirección del Trabajo (DT)

| Término | Definición | Por qué importa |
|:---|:---|:---|
| **REL** | Registro Electrónico Laboral. Sistema donde se registran los contratos en MiDT. | Es el corazón de la integración. |
| **SIREL** | Sistema de Registro Electrónico Laboral. Nombre técnico del sistema. | Para búsquedas técnicas. |
| **Comprobante de Registro** | Documento PDF emitido por la DT que acredita que un contrato está registrado. | Tiene valor legal; debe ser almacenado con hash. |
| **Jornada Parcial** | Hasta 30 horas semanales (según nueva definición). | Impacta cálculo de cotizaciones y validaciones. |
| **Jornada Completa** | 44 horas semanales (transición a 40). | Requiere validación de fecha (Ley 21.561). |
| **Código 191-1 / 191-2** | Códigos para pago de trabajadoras de casa particular (puertas afuera / adentro). | Usar el incorrecto invalida el pago (Caso 1). |

## Términos Previred

| Término | Definición | Por qué importa |
|:---|:---|:---|
| **DPN** | Declaración y Pago con Nulidad. Pago atrasado de cotizaciones. | Tiene requisitos específicos y plazo límite. |
| **FUN** | Formulario Único de Notificación para Isapres. | Debe enviarse junto con el pago. |
| **Seguro Social** | Nueva cotización del empleador (1% desde ago-2025). | Nuevo campo obligatorio en la nómina. |
| **Archivo de 105 campos** | Formato de archivo para carga masiva en Previred. | Debe generarse correctamente. |

## Términos Técnicos

| Término | Definición | Por qué importa |
|:---|:---|:---|
| **Hash (SHA-256)** | Huella digital única de un archivo. | Para acreditar que un comprobante no fue alterado (Dictamen 2927/58). |
| **Idempotencia** | Propiedad de que una operación produzca el mismo resultado aunque se ejecute múltiples veces. | Evita duplicados en integraciones. |
| **Worker** | Módulo independiente que ejecuta tareas en segundo plano. | Para la integración con MiDT. |
