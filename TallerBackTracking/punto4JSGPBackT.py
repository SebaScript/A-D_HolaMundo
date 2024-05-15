# Juan Sebastian Garcia Perez

def sudoku_sumas(matriz, objetivo):
    if sum(1 for row in matriz for num in row if num == 0) == 0:
        for row in matriz:
            if sum(row) != objetivo:
                return False
        for col in range(3):
            if sum(matriz[row][col] for row in range(3)) != objetivo:
                return False
        return True

    for i in range(3):
        for j in range(3):
            if matriz[i][j] == 0:
                for num in range(1, objetivo):
                    matriz[i][j] = num
                    if sudoku_sumas(matriz, objetivo):
                        return matriz
                    matriz[i][j] = 0
                return False
    return False


matriz = [[3,6,7],
          [0,7,0],
          [8,0,5]]
objetivo = 16

#PROFE ACUERDESE Q UD DIJO Q EXCEPCIONES NO PQ NO DA EL TIEMPO!!!!!!!!

resultado = sudoku_sumas(matriz, objetivo)
for i in resultado:
    print(i)
