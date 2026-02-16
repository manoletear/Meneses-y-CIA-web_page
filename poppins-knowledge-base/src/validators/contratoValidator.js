/**
 * Validador de contratos según normativa DT
 * Basado en casos reales documentados
 */

/**
 * Valida un objeto contrato contra las reglas de la DT
 * @param {Object} contrato - Objeto con los datos del contrato
 * @returns {Array} - Array de errores encontrados (vacío si es válido)
 */
function validateContrato(contrato) {
    const errores = [];

    // Validación de RUT (formato básico y dígito verificador)
    if (!validarRUT(contrato.rutTrabajador)) {
        errores.push({
            campo: 'rutTrabajador',
            mensaje: 'RUT inválido',
            casoAsociado: 'Caso general'
        });
    }

    // Validación de jornada parcial (Caso 3)
    if (contrato.tipoJornada === 'Parcial') {
        if (contrato.horasSemanales >= 44) {
            errores.push({
                campo: 'horasSemanales',
                mensaje: 'Jornada parcial no puede tener 44 o más horas semanales',
                casoAsociado: 'Caso 3'
            });
        }
    }

    // Validación de fecha para Ley 21.561 (Caso 2)
    const fechaInicio = new Date(contrato.fechaInicio);
    const fechaLimite = new Date('2024-04-26');
    
    if (contrato.horasSemanales === 44 && fechaInicio < fechaLimite) {
        errores.push({
            campo: 'fechaInicio',
            mensaje: 'La jornada de 44 horas solo aplica desde el 26 de abril de 2024',
            casoAsociado: 'Caso 2'
        });
    }

    // Validación para trabajadoras de casa particular (Caso 1)
    if (contrato.tipoTrabajador === 'CasaParticular') {
        const codigosValidos = ['191-1', '191-2'];
        if (!codigosValidos.includes(contrato.codigoPago)) {
            errores.push({
                campo: 'codigoPago',
                mensaje: 'Código de pago inválido para casa particular. Use 191-1 (puertas afuera) o 191-2 (puertas adentro)',
                casoAsociado: 'Caso 1'
            });
        }
    }

    return errores;
}

/**
 * Valida formato de RUT chileno
 * @param {string} rut - RUT a validar
 * @returns {boolean} - true si es válido
 */
function validarRUT(rut) {
    if (!rut) return false;
    
    // Eliminar puntos y guión
    const rutLimpio = rut.replace(/[\.\-]/g, '');
    
    // Debe tener al menos 2 caracteres (número + dv)
    if (rutLimpio.length < 2) return false;
    
    // Separar cuerpo y dígito verificador
    const cuerpo = rutLimpio.slice(0, -1);
    const dv = rutLimpio.slice(-1).toUpperCase();
    
    // Validar que el cuerpo sean solo números
    if (!/^\d+$/.test(cuerpo)) return false;
    
    // Calcular dígito verificador
    let suma = 0;
    let multiplo = 2;
    
    for (let i = cuerpo.length - 1; i >= 0; i--) {
        suma += parseInt(cuerpo.charAt(i)) * multiplo;
        multiplo = multiplo === 7 ? 2 : multiplo + 1;
    }
    
    const dvEsperado = 11 - (suma % 11);
    let dvCalculado = dvEsperado === 11 ? '0' : dvEsperado === 10 ? 'K' : dvEsperado.toString();
    
    return dv === dvCalculado;
}

module.exports = { validateContrato, validarRUT };
