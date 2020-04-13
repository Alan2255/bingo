from src.bingo import carton_ejemplo

def test_contar_celdas_ocupadas():
    carton = carton_ejemplo()
    contador = 0
    for fila in carton:
      for celda in fila:
        if celda > 0:
          contador += 1

    assert contador == 15

def test_columna():
    carton = carton_ejemplo()
    for i in range(9):
      contador = 0
      for fila in carton: 
        if fila[i] > 0: 
          contador += 1

      assert contador > 0 and contador < 3

def test_nomasde3():
    carton = carton_ejemplo()
    for m in range (7):
      for i in range(3):
        contador = 0
        for x in range(0,3):
          if carton[i][x+m] > 0:
            contador += 1
        assert contador > 0 and contador < 3 

def test_fila():
    carton = carton_ejemplo()
    for fila in carton:
      contador = 0
      for celda in fila:
        if celda > 0:
          contador += 1
      assert contador == 5


