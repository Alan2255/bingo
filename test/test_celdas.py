# Autor: Alan Hergenreder.

from src.bingo import carton_ejemplo
from src.bingo import columnas
from src.bingo import fila
from src.bingo import nomasde3


# Verifico que cada columna no este vacia ni llena.
def test_columnas():
    assert columna(carton_ejemplo()) == True


# Verifico que cada 3 celdas consecutivas no haya mas de 3 ocupadas o vacias.
def test_nomasde3():
    assert nomasde3(carton_ejemplo()) == True


# Verifico que cada fila tenga 5 celdas ocupadas.
def test_fila(carton_ejemplo()):
    assert fila() == True


