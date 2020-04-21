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

# Compruebo si la progrecion entre cada columna es 10.
def test_de_a_10_columnas():
    carton = carton_ejemplo()
    n = 0
    for i in range(9):
      a = carton[0][i]
      b = carton[1][i]
      c = carton[2][i]
      if i == 8:
        n = 1
      if a != 0:
        assert a > ((i+1)*10)-11 and a < (i+1)*10+n
      if b != 0:
        assert b > ((i+1)*10)-10 and b < (i+1)*10+n
      if c != 0:
        assert c > ((i+1)*10)-10 and c < (i+1)*10+n

