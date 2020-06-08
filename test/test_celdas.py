# Autor: Alan Hergenreder.

from src.bingo import ejemplo
from src.bingo import columnas
from src.bingo import fila
from src.bingo import nomasde3

# Verifico que cada columna no este vacia ni llena.
def test_columnas():
    for i in range(10):
      assert columnas(ejemplo()) == True


# Verifico que cada 3 celdas consecutivas no haya mas de 3 ocupadas o vacias.
def test_nomasde3():
    for i in range(10):
      assert nomasde3(ejemplo()) == True


# Verifico que cada fila tenga 5 celdas ocupadas.
def test_fila():
    for i in range(10):
      assert fila(ejemplo()) == True


