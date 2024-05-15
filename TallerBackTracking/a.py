def minDifference(arr, n):
    if len(arr) != n:
        raise ValueError("El tamaño de la lista no coincide con el valor de N")
    
    # Suma total de los elementos del arreglo
    total_sum = sum(arr)
    
    # Tamaño de la tabla de DP será (n+1) x (total_sum//2 + 1)
    half_sum = total_sum // 2
    dp = [[False] * (half_sum + 1) for _ in range(n + 1)]
    
    # Inicialización
    for i in range(n + 1):
        dp[i][0] = True
    
    # Llenado de la tabla de DP
    for i in range(1, n + 1):
        for j in range(1, half_sum + 1):
            dp[i][j] = dp[i-1][j]
            if arr[i-1] <= j:
                dp[i][j] = dp[i][j] or dp[i-1][j-arr[i-1]]
    
    # Encontrar la suma máxima j <= total_sum//2 que se puede formar
    for j in range(half_sum, -1, -1):
        if dp[n][j]:
            subset_sum1 = j
            break
    
    subset_sum2 = total_sum - subset_sum1
    
    # La diferencia mínima
    return abs(subset_sum2 - subset_sum1)

# Ejemplo de uso
N = 4
arr = [1, 6, 11, 5]  # Asegúrate de usar una lista de longitud N
print(minDifference(arr, N))  # Salida: 1

# Otro ejemplo
N = 2
arr = [1, 4]  # Asegúrate de usar una lista de longitud N
print(minDifference(arr, N))  # Salida: 3
