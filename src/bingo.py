# Autor: Alan Hergenreder.

import random

# Los 0 representan celdas vacias.

def  carton_ejemplo():
     carton = (
       (7 ,10 ,0  ,0  ,41 ,0  ,0  ,72  ,80),
       (0 ,12 ,25 ,0  ,48 ,52 ,0  ,78  ,0 ),
       (9 ,0  ,29 ,33 ,0  ,0  ,63 ,0   ,87),
     )
     return carton

def suma(x,f):
    s = 0
    for i in range(x):
      s += f[i]

    return s
# Genero los 6 cartones aleatoreamente según el criterio de celdas.
def posicion(c):
    s1 = 0
    s2 = 0
    s3 = 0
    for i in range(6):
      for x in range(9):
        v = 0
        if x < 2:
          s1 = random.randrange(3)
          c[i][s1][x] = 0
        else:
          if c[i][0][x-1] == 1:
            if c[i][0][x-2] == 1:
              c[i][0][x] = 0
            else:
              v += 1
          else:
            if c[i][0][x-2] == 1:
              v += 1

          if c[i][1][x-1] == 1:
            if c[i][1][x-2] == 1:
              c[i][1][x] = 0
            else:
              v += 1
          else:
            if c[i][1][x-2] == 1:
              v += 1

          if c[i][2][x-1] == 1:
            if c[i][2][x-2] == 1:
              c[i][2][x] = 0
            else:
              v += 1
          else:
            if c[i][2][x-2] == 1:
              v += 1

          if v > 1:
            s1 = suma(x,c[i][0])
            s2 = suma(x,c[i][1])
            s3 = suma(x,c[i][2])
            if c[i][0][x] == 0:
              if s2 >= s3:
                c[i][1][x] = 0
              else:
                c[i][2][x] = 0
            else:
              if c[i][1][x] == 0:
                if s1 >= s3:
                  c[i][0][x] = 0
                else:
                  c[i][2][x] = 0
              else:
                if c[i][2][x] == 0:
                  if s1 >= s2:
                    c[i][0][x] = 0
                  else:
                    c[i][1][x] = 0
                
                else:
                  if s1 >= s2:
                    if s1 >= s3:
                      c[i][0][x] = 0
                    else:
                      c[i][2][x] = 0
                  else:
                    if s2 >= s3:
                      c[i][1][x] = 0
                    else:
                      c[i][2][x] = 0

    return c

def carton_6():
    c = [
          [  
             [1,1,1,1,1,1,1,1,1],
             [1,1,1,1,1,1,1,1,1],
             [1,1,1,1,1,1,1,1,1]
          ],
          [  
             [1,1,1,1,1,1,1,1,1],
             [1,1,1,1,1,1,1,1,1],
             [1,1,1,1,1,1,1,1,1]
          ],
          [  
             [1,1,1,1,1,1,1,1,1],
             [1,1,1,1,1,1,1,1,1],
             [1,1,1,1,1,1,1,1,1]
          ],
          [  
             [1,1,1,1,1,1,1,1,1],
             [1,1,1,1,1,1,1,1,1],
             [1,1,1,1,1,1,1,1,1]
          ],
          [  
             [1,1,1,1,1,1,1,1,1],
             [1,1,1,1,1,1,1,1,1],
             [1,1,1,1,1,1,1,1,1]
          ],
          [  
             [1,1,1,1,1,1,1,1,1],
             [1,1,1,1,1,1,1,1,1],
             [1,1,1,1,1,1,1,1,1]
          ],
        ]


    return c


