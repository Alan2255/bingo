# Autor: Alan Hergenreder.

from src.bingo import carton_ejemplo
from src.bingo import de_a_10_columnas
from src.bingo import orden_columnas

# Compruebo si los numeros de cada columna estan ordenados de menor a mayor.
def test_orden_columnas():
    assert orden_columnas(carton_ejemplo()) == True


# Compruebo si la progrecion entre cada columna es 10.
def test_de_a_10_columnas():
    assert de_a_10_columnas(carton_ejemplo()) == True


# Compruebo si el talonario contiene todos los numeros del 1 al 90.
def test_1a90():
    assert _1a90(talonario_ejemplo) == True

