# Autor: Alan Hergenreder.

import random

# Los 0 representan celdas vacias.
# Los numeros mayores que cero representan celdas ocupadas.

def  carton_ejemplo():
     carton = [
       [7 ,10 ,0  ,0  ,41 ,0  ,0  ,72  ,80],
       [0 ,12 ,25 ,0  ,48 ,52 ,0  ,78  ,0 ],
       [9 ,0  ,29 ,33 ,0  ,0  ,63 ,0   ,87],
     ]
     return carton

# Genera los espacios de todas las columnas de los 6 cartones aleatoriamente.
def espacios_carton():
    random.seed()
    t = [
         [0,0,0,0,0,0],
         [0,0,0,0,0,0],
         [0,0,0,0,0,0],
         [0,0,0,0,0,0],
         [0,0,0,0,0,0],
         [0,0,0,0,0,0],
         [0,0,0,0,0,0],
         [0,0,0,0,0,0],
         [0,0,0,0,0,0],
        ]
    s = 0
    dos = 0
    uno = 0
    for i in range(9):
      if i > 0:
        s = 1
      if i == 8:
        s = 2
      uno = 0
      dos = 0
      for x in range(6):
        a = random.randrange(2)+1
        if uno == 3-s:
          t[i][x] = 2
          a = 0
        if dos == 3+s:
          t[i][x] = 1
          a = 0
        if uno != 3-s and dos != 3+s:
          t[i][x] = a
        if a == 2:
          dos += 1
        if a == 1:
          uno += 1
    return t

print(espacios_carton())



