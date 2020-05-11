# Autor: Alan Hergenreder.

from src.bingo import carton_ejemplo
from src.bingo import de_a_10_columnas
from src.bingo import orden_columnas

# Compruebo si los numeros de cada columna estan ordenados de menor a mayor.
def test_orden_columnas():
    assert orden_columnas() == True


# Compruebo si la progrecion entre cada columna es 10.
def test_de_a_10_columnas():
    assert de_a_10_columnas() == True

