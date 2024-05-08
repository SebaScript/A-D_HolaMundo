#dada una matriz n*n mostrar el camino mas optimo tomando buscando tomar el valor mayor desde la posicion (0,0) a (n,n) (solo se puede desplazar hacia la derecha y abajo de la matriz una a la vez)

campo_de_lechugas = [
    [2, 1, 8, 3],
    [1, 10, 5, 1],
    [4, 2, 9, 1],
    [1, 8, 3, 6]
]

def encontrar_camino_optimo(matriz):
    if not matriz or len(matriz) != len(matriz[0]):
        raise ValueError("La matriz debe ser no vacía y cuadrada.")

    n = len(matriz)

    dp = [[0] * n for _ in range(n)]
    
    dp[0][0] = matriz[0][0]
    
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + matriz[i][0]
        dp[0][i] = dp[0][i-1] + matriz[0][i]
    
    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + matriz[i][j]
    
    camino = []
    i, j = n-1, n-1
    while i > 0 and j > 0:
        camino.append((i, j))
        if dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    camino.append((i, j))
    while i > 0:
        i -= 1
        camino.append((i, j))
    while j > 0:
        j -= 1
        camino.append((i, j))
    
    return camino[::-1]

try:
    camino_optimo = encontrar_camino_optimo(campo_de_lechugas)
    print("El camino más óptimo es:", camino_optimo)
except ValueError as e:
    print("Error:", e)
except Exception as e:
    print("Se produjo un error inesperado:", e)
