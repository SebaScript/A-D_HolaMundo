#Tienes dos arreglos A  y B  de igual longitud N.
#Su tarea es emparejar cada elemento de la matriz A  
#con un elemento de la matriz B , de modo que la suma de las  
#diferencias absolutas de todos los pares sea mínima.


#Metodo Greedy
def minima_diferencia(A, B):
    if not isinstance(A, list) or not isinstance(B, list):
        return "Error: Ambos argumentos deben ser listas."
        
    if len(A) != len(B):
        return "Error: Ambas listas deben tener la misma longitud."
    
    for i in range(len(A)):
        if not isinstance(A[i], (int, float)) or not isinstance(B[i], (int, float)):
            return "Error: Todos los elementos en las listas deben ser números."
    
    A.sort()
    B.sort()

    suma = 0

    for i in range(len(A)):
        suma += abs(A[i] - B[i])

    return suma

A = [4.2, 1, 8, 7]
B = [2, 3, 6, 5]

print(f"La minima suma es: {minima_diferencia(A, B)}")