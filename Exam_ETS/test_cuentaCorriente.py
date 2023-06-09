import pytest
from cuentaCorriente import CuentaCorriente
from dni import Dni

cuenta1 = CuentaCorriente('Alejandro','Hdez','La Hoya 1','766767676','77877825A', 1000.0)
dni1 = Dni('77877825A')
def test_cuenta_building():
    assert cuenta1.nombre == 'Alejandro'
    assert cuenta1.apellido == 'Hdez'
    assert cuenta1.direccion == 'La Hoya 1'
    assert cuenta1.telefono == '766767676'
    assert cuenta1.nif.dni == dni1.dni
    assert cuenta1.saldo == 1000.0
    

def test_retirar_dinero():
    cuenta1.retirarDinero(500.0)
    dineroRestante = cuenta1.getSaldo()
    assert dineroRestante == 500.0


def test_ingresar_dinero():
    cuenta1.ingresarDinero(500.0)
    dineroRestante = cuenta1.getSaldo()
    assert dineroRestante == 1000.0

   
def test_saldo_negativo():
    cuenta1.retirarDinero(2000.0)
    assert cuenta1.saldoNegativo() == False