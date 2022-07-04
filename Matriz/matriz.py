import random

matriz=[[random.randint(0,30) for i in range(5)] for j in range(5)]

matriz_test = [[1, 2, 3, 4, 0],
          [2, 3, 4, 16, 0],
          [3, 4, 5, 0, 0],
          [4, 3, 2, 1, 0],
          [5, 4, 3, 2, 1]]

#Busqueda por fila
for i in range(5):
    for j in range(2):
        if ((matriz[i][j]-matriz[i][j+1]==-1 ) and (matriz[i][j]-matriz[i][j+2]==-2 ) and (matriz[i][j]-matriz[i][j+3]==-3 )):
            print(f"Se encontró una secuencia de 4 números consecutivos ASC en la fila {i} entre la posición {j} y {j+3}")
        if (matriz[i][j]-matriz[i][j+1]==1) and (matriz[i][j]-matriz[i][j+2]==2) and (matriz[i][j]-matriz[i][j+3]==3):
                print(f"Se encontró una secuencia de 4 números consecutivos DESC en la fila {i} entre la posición {j} y {j+3}")

#busqueda por columna
for j in range(5):
    for i in range(2):
        if ((matriz[i][j]-matriz[i+1][j]==-1 ) and (matriz[i][j]-matriz[i+2][j]==-2 ) and (matriz[i][j]-matriz[i+3][j]==-3 )):
            print(f"Se encontró una secuencia de 4 números consecutivos ASC en la columna {j} entre la posición {i} y {i+3}")
        if (matriz[i][j]-matriz[i+1][j]==1) and (matriz[i][j]-matriz[i+2][j]==2) and (matriz[i][j]-matriz[i+3][j]==3):
                print(f"Se encontró una secuencia de 4 números consecutivos DESC en la columna {j} entre la posición {i} y {i+3}")