#Implementa una función que encuentre el MCD de dos números utilizando el algoritmo de Euclides sin recursión.

def algoritmo_euclides(a, b): # O(n)
    if a > b: # O(1)
        while b != 0: # complejidad tiempo: O(n) ; complejidad espacial: O(1)
            c = a # complejidad tiempo: O(n) ; complejidad espacial: O(1)
            a = b # complejidad tiempo: O(n) ; complejidad espacial: O(1)
            b = c % b # complejidad tiempo: O(n) ; complejidad espacial: O(1)
        return a # O(1)
    else: # O(1)
        print("El numero a debe ser mayor al b") # O(1)

a = 48 # O(1)
b = 18 # O(1)
mcd = algoritmo_euclides(a, b) # complejidad tiempo: O(n) ; complejidad espacial: O(1)
print(f"El MCD es {mcd}") # O(1)

# Ecuación: 5 O(n) + 7 O(1)
# Complejidad del algoritmo: O(n)