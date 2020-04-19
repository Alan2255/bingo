# Autor: Alan Hergenreder.

from src.bingo import carton_ejemplo


# Verifico que la cantidad de celdas ocupadas es 15.
def test_contar_celdas_ocupadas():
    carton = carton_ejemplo()
    contador = 0
    for fila in carton:
      for celda in fila:
        if celda > 0:
          contador += 1

    assert contador == 15

# Verifico que cada columna no este vacia ni llena.
def test_columna():
    carton = carton_ejemplo()
    for i in range(9):
      contador = 0
      for fila in carton: 
        if fila[i] > 0: 
          contador += 1

      assert contador > 0 and contador < 3

# Verifico que cada 3 celdas consecutivas no haya mas de 3 ocupadas o vacias.
def test_nomasde3():
    carton = carton_ejemplo()
    for m in range (7):
      for i in range(3):
        contador = 0
        for x in range(0,3):
          if carton[i][x+m] > 0:
            contador += 1
        assert contador > 0 and contador < 3 

# (!) Este test posiblemente pueda reemplazar al primero.
# Verifico que cada fila tenga 5 celdas ocupadas.
def test_fila():
    carton = carton_ejemplo()
    for fila in carton:
      contador = 0
      for celda in fila:
        if celda > 0:
          contador += 1
      assert contador == 5


