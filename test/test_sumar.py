from src.bingo import carton_ejemplo

def test_contar_celdas_ocupadas():
    carton = carton_ejemplo()
    contador = 0
    for fila in carton:
      for celda in filas:
        contador += celda



    assert contador == 15

