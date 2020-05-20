# Autor: Alan Hergenreder.

from __future__ import print_function
import random

# Los 0 representan celdas vacias.
# Los numeros mayores que cero representan celdas ocupadas.


# Genera un talonario de bingo valido.
def generador_bingo():
    print("Por favor, aguarde un momento.")
    print("")
    
    t = orden_talonario(numeros_talonario(ubicacion_talonario(espacios_talonario())))

    for carton in range(6):
      for fila in range(3):
        for celda in t[carton][fila]:
          print("% 4d" % celda, end='')
        print("")
      print("")

    return 0

# Ordena los numeros de un talonario.
def orden_talonario(n):
    a = 0
    b = 0
    for carton in range(6):
      for columna in range(9):
        if n[carton][0][columna] != 0:
          a = n[carton][0][columna]
          if n[carton][1][columna] != 0:
            b = n[carton][1][columna]
            if a > b:
              n[carton][0][columna] = b
              n[carton][1][columna] = a

          if n[carton][2][columna] != 0:
            b = n[carton][2][columna]
            if a > b:
              n[carton][0][columna] = b
              n[carton][2][columna] = a


        if n[carton][1][columna] != 0:
          a = n[carton][1][columna]
          if n[carton][2][columna] != 0:
            b = n[carton][2][columna]
            if a > b:
              n[carton][1][columna] = b
              n[carton][2][columna] = a

    return n


# Coloca numeros en los espacios no ocupados del talonario.
def numeros_talonario(u):
    numeros = [0,1,2,3,4,5,6,7,8,9,10,
              11,12,13,14,15,16,17,18,19,20,
              21,22,23,24,25,26,27,28,29,30,
              31,32,33,34,35,36,37,38,39,40,
              41,42,43,44,45,46,47,48,49,50,
              51,52,53,54,55,56,57,58,59,60,
              61,62,63,64,65,66,67,68,69,70,
              71,72,73,74,75,76,77,78,79,80,
              81,82,83,84,85,86,87,88,89,90]
    r = 0
    n = 0
    for carton in range(6):
      for fila in range(3):
        for columna in range(9):
          if columna > 7:
            n = 1
          if u[carton][fila][columna] == -1:
            r = 0
            while(numeros[r] == 0):
              r = random.randrange(((columna+1)*10)-10,(columna+1)*10+n)
              if numeros[r] != 0:
                numeros[r] = 0
                u[carton][fila][columna] = r
                break
        n = 0
    return u

# Ubica los espacios ocupados en el talonario.
def ubicacion_talonario(e):
    b = False
    while(b == False):
      b = True
      r1 = 0
      r2 = 0
      bul = True
      u = [
           [
            [-1, -1, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1, -1],
           ],
           [
            [-1, -1, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1, -1],
           ],
           [
            [-1, -1, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1, -1],
           ],
           [
            [-1, -1, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1, -1],
           ],
           [
            [-1, -1, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1, -1],
           ],
           [
            [-1, -1, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1, -1],
           ],
          ]

      for carton in range(6):
        for columna in range(9):
          r1 = 0
          r2 = 0
          if e[carton][columna] == 1:
            r1 = random.randrange(3)
            while(u[carton][r1][columna-1] == 0 and u[carton][r1][columna-2] == 0):
              r1 = random.randrange(3)

            if columna > 1:
              if u[carton][0][columna-1] == -1:
                if u[carton][0][columna-2] == -1:
                  r1 = 0
              if u[carton][1][columna-1] == -1:
                if u[carton][1][columna-2] == -1:
                  r1 = 1
              if u[carton][2][columna-1] == -1:
                if u[carton][2][columna-2] == -1:
                  r1 = 2

            u[carton][r1][columna] = 0

          else:
            r1 = random.randrange(3)
            r2 = r1
            while (r2 == r1):
              r2 = random.randrange(3)


            if columna > 1:
              if u[carton][0][columna-1] == -1:
                if u[carton][0][columna-2] == -1:
                  u[carton][0][columna] = 0
                  r1 = 0
                  r2 = r1
                  while (r2 == r1):
                    r2 = random.randrange(3)
                  if u[carton][1][columna-1] == -1:
                    if u[carton][1][columna-2] == -1:
                      u[carton][1][columna] = 0
                      r2 = 1                  
                  if u[carton][2][columna-1] == -1:
                    if u[carton][2][columna-2] == -1:
                      u[carton][2][columna] = 0
                      r2 = 2                  



              if u[carton][1][columna-1] == -1:
                if u[carton][1][columna-2] == -1:
                  u[carton][1][columna] = 0
                  r1 = 1
                  r2 = r1
                  while (r2 == r1):
                    r2 = random.randrange(3)
                  if u[carton][2][columna-1] == -1:
                    if u[carton][2][columna-2] == -1:
                      u[carton][2][columna] = 0
                      r2 = 2                                    


              if u[carton][2][columna-1] == -1:
                if u[carton][2][columna-2] == -1:
                  u[carton][2][columna] = 0
                  r1 = 2
                  r2 = r1
                  while (r2 == r1):
                    r2 = random.randrange(3)

            u[carton][r1][columna] = 0
            u[carton][r2][columna] = 0


      for i in range(6):
        if columnas(u[i]) == False:
          b = False
        if nomasde3(u[i]) == False:
          b = False
        if fila(u[i]) == False:
          b = False

    return u


# Genera los espacios ocupados de un talonario valido.
def espacios_talonario():
    r = 0
    b = False
    i = 0
    while(b == False):
      b = True

      banderaX = [[0,0,0,0,0,0],[0,0,0,0,0,0]]
      banderaY = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]

      e = [
           [0,0,0,0,0,0,0,0,0,],
           [0,0,0,0,0,0,0,0,0,],
           [0,0,0,0,0,0,0,0,0,],
           [0,0,0,0,0,0,0,0,0,],
           [0,0,0,0,0,0,0,0,0,],
           [0,0,0,0,0,0,0,0,0,]
          ]

      for x in range(6):
        for y in range(9):
          r = random.randrange(2)+1

          if banderaX[0][x] == 3:
            r = 1

          if banderaX[1][x] == 6:
            r = 2

          if banderaY[0][y] == 3 and y == 0:
            r = 1
          if banderaY[0][y] == 2 and y > 0 and y < 8:
            r = 1
          if banderaY[0][y] == 1 and y == 8:
            r = 1

          if banderaY[1][y] == 3 and y == 0:
            r = 2
          if banderaY[1][y] == 4 and y > 0 and y < 8:
            r = 2
          if banderaY[1][y] == 5 and y == 8:
            r = 2

          e[x][y] = r
          if r == 2:
            banderaX[0][x] += 1
            banderaY[0][y] += 1

          if r == 1:
            banderaX[1][x] += 1
            banderaY[1][y] += 1

      if espacios_ocupados(e) == False:
        b = False

    return e

# Verifico que los espacios ocupados sean validos horizontal y verticalmente.
def espacios_ocupados(e):
    bul = True
    x = 0
    y = 0

    # Verifico los espacios en las filas.
    for fila in range(6):
      for columna in range(9):
        x += e[fila][columna]
      if x != 12:
        bul = False
      x = 0

    columna = 0
    fila = 0

    # Verifico los espacios en las columnas.
    for columna in range(9):
      for fila in range(6):
        y += e[fila][columna]
      if columna == 0:
        if y != 9:
          bul = False
      if columna > 0 and columna < 8:
         if y != 8:
           bul = False
      if columna == 8:
         if y != 7:
           bul = False
      y = 0


    return bul

# Verifico que cada columna no este vacia ni llena.
def columnas(carton):
    bul = True
    for i in range(9):
      contador = 0
      for fila in carton: 
        if fila[i] != 0: 
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
          if carton[i][x+m] != 0:
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
        if celda != 0:
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
        if not( b > ((i+1)*10)-11 and b < (i+1)*10+n):
          bul = False
      if c != 0:
        if not( c > ((i+1)*10)-11 and c < (i+1)*10+n):
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

generador_bingo()

