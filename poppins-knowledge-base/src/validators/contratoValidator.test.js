const { validateContrato } = require('./contratoValidator');

describe('Validador de Contratos DT', () => {
    
    test('Contrato válido debe retornar array vacío', () => {
        const contratoValido = {
            rutTrabajador: '12.345.678-5',
            tipoJornada: 'Completa',
            horasSemanales: 44,
            fechaInicio: '2024-05-01',
            tipoTrabajador: 'General',
            codigoPago: null
        };
        
        expect(validateContrato(contratoValido)).toEqual([]);
    });

    test('Jornada parcial con 44 horas debe dar error (Caso 3)', () => {
        const contratoInvalido = {
            rutTrabajador: '12.345.678-5',
            tipoJornada: 'Parcial',
            horasSemanales: 44,
            fechaInicio: '2024-05-01',
            tipoTrabajador: 'General',
            codigoPago: null
        };
        
        const errores = validateContrato(contratoInvalido);
        expect(errores.length).toBeGreaterThan(0);
        expect(errores[0].casoAsociado).toBe('Caso 3');
    });

    test('Fecha anterior a 26-abr-2024 con 44h debe dar error (Caso 2)', () => {
        const contratoInvalido = {
            rutTrabajador: '12.345.678-5',
            tipoJornada: 'Completa',
            horasSemanales: 44,
            fechaInicio: '2024-04-01',
            tipoTrabajador: 'General',
            codigoPago: null
        };
        
        const errores = validateContrato(contratoInvalido);
        expect(errores.length).toBeGreaterThan(0);
        expect(errores[0].casoAsociado).toBe('Caso 2');
    });

    test('Casa particular con código de pago incorrecto debe dar error (Caso 1)', () => {
        const contratoInvalido = {
            rutTrabajador: '12.345.678-5',
            tipoJornada: 'Completa',
            horasSemanales: 44,
            fechaInicio: '2024-05-01',
            tipoTrabajador: 'CasaParticular',
            codigoPago: '191-3'
        };
        
        const errores = validateContrato(contratoInvalido);
        expect(errores.length).toBeGreaterThan(0);
        expect(errores[0].casoAsociado).toBe('Caso 1');
    });
});
