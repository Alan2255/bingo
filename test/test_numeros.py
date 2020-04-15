# Autor: Alan Hergenreder.

from src.bingo import carton_ejemplo

# Compruebo si los numeros de cada columna estan ordenados de menor a mayor.
def test_orden_columnas():
    carton = carton_ejemplo()
    for i in range(9):
      a = carton[0][i]
      b = carton[1][i]
      c = carton[2][i]
      if a != 0:
        if b != 0:
          assert a < b
        if c != 0:
          assert a < c
      if b != 0:
        if c != 0:
          assert b < c


