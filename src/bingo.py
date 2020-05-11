# Autor: Alan Hergenreder.

from __future__ import print_function
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
def columna(carton):
    bul = True
    for i in range(9):
      contador = 0
      for fila in carton: 
        if fila[i] > 0: 
          contador += 1
      if not(contador > 0 and contador < 3):
        bul = False
    return bul


# Verifico que cada 3 celdas consecutivas no haya mas de 3 ocupadas o vacias.
def nomasde3(carton):
    bul = True
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
def fila(carton):
    bul = True
    for fila in carton:
      contador = 0
      for celda in fila:
        if celda > 0:
          contador += 1
      if not(contador == 5):
        bul = False
    return bul


# Compruebo si los numeros de cada columna estan ordenados de menor a mayor.
def orden_columnas(carton):
    bul = True
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
def de_a_10_columnas(carton):
    bul = True
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


# Compruebo si el talonario contiene todos los numeros del 1 al 90.
def _1a90(t):
    bul = True
    numeros = [0,1,2,3,4,5,6,7,8,9,10,
              11,12,13,14,15,16,17,18,19,20,
              21,22,23,24,25,26,27,28,29,30,
              31,32,33,34,35,36,37,38,39,40,
              41,42,43,44,45,46,47,48,49,50,
              51,52,53,54,55,56,57,58,59,60,
              61,62,63,64,65,66,67,68,69,70,
              71,72,73,74,75,76,77,78,79,80,
              81,82,83,84,85,86,87,88,89,90]
    for carton in range(6):
      for fila in range(3):
        for columna in range(9):
          if t[carton][fila][columna] != 0:
            numeros[t[carton][fila][columna]] = 0
    for i in range(90):
      if numeros[i] != 0:
       bul = False

    return bul

