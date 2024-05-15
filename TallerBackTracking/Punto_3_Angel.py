#Punto 3
#Programación dinamica

def minDifference(arr, n):
    sumaArr = sum(arr)

    mitad_sum = sumaArr // 2
    dp = [[False] * (mitad_sum + 1) for _ in range(n + 1)]

    for i in range(n + 1):
       dp[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, mitad_sum + 1):
            dp[i][j] = dp[i-1][j]
            if arr[i-1] <= j:
                dp[i][j] = dp[i][j] or dp[i-1][j-arr[i-1]]
    
    for j in range(mitad_sum, -1, -1):
        if dp[n][j]:
            subset1 = j
            break
    
    subset2 = sumaArr - subset1

    return abs(subset2 - subset1)

N = 4
arr = [1, 6, 11, 5] 
print(minDifference(arr, N))

N = 2
arr = [1, 4]
print(minDifference(arr, N))

N = 15
arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print(minDifference(arr, N))