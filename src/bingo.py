# Autor: Alan Hergenreder.

import random

# Los 0 representan celdas vacias.
# Los numeros mayores que cero representan celdas ocupadas.

def  carton_ejemplo():
     carton = [
       [7 ,10 ,0  ,0  ,41 ,0  ,0  ,72  ,80],
       [0 ,12 ,25 ,0  ,48 ,52 ,0  ,78  ,0 ],
       [9 ,0  ,29 ,33 ,0  ,0  ,63 ,0   ,90],
     ]
     return carton


# Verifico que cada columna no este vacia ni llena.
def columna():
    bul = True
    carton = carton_ejemplo()
    for i in range(9):
      contador = 0
      for fila in carton: 
        if fila[i] > 0: 
          contador += 1
      if not(contador > 0 and contador < 3):
        bul = False
    return bul


# Verifico que cada 3 celdas consecutivas no haya mas de 3 ocupadas o vacias.
def nomasde3():
    bul = True
    carton = carton_ejemplo()
    for m in range (7):
      for i in range(3):
        contador = 0
        for x in range(0,3):
          if carton[i][x+m] > 0:
            contador += 1
        if not(contador > 0 and contador < 3):
          bul = False

    return bul


# Verifico que cada fila tenga 5 celdas ocupadas.
def fila():
    bul = True
    carton = carton_ejemplo()
    for fila in carton:
      contador = 0
      for celda in fila:
        if celda > 0:
          contador += 1
      if not(contador == 5):
        bul = False
    return bul


# Compruebo si los numeros de cada columna estan ordenados de menor a mayor.
def orden_columnas():
    bul = True
    carton = carton_ejemplo()
    for i in range(9):
      a = carton[0][i]
      b = carton[1][i]
      c = carton[2][i]
      if a != 0:
        if b != 0:
          if not(a < b):
            bul = False
        if c != 0:
          if not(a < c):
            bul = False
      if b != 0:
        if c != 0:
          if not(b < c):
            bul = False

    return bul

# Compruebo si la progrecion entre cada columna es 10.
def de_a_10_columnas():
    bul = True
    carton = carton_ejemplo()
    n = 0
    for i in range(9):
      a = carton[0][i]
      b = carton[1][i]
      c = carton[2][i]
      if i == 8:
        n = 1
      if a != 0:
        if not( a > ((i+1)*10)-11 and a < (i+1)*10+n):
          bul = False
      if b != 0:
        if not( b > ((i+1)*10)-10 and b < (i+1)*10+n):
          bul = False
      if c != 0:
        if not( c > ((i+1)*10)-10 and c < (i+1)*10+n):
          bul = False

    return bul

