#Implementa una función que encuentre el MCD de dos números utilizando el algoritmo de Euclides sin recursión.

def algoritmo_euclides(a, b):
    if a > b:
        while b != 0:
            c = a
            a = b
            b = c % b
        return a
    else:
        print("El numero a debe ser mayor al b")

a = 48
b = 18
mcd = algoritmo_euclides(a, b)
print(f"El MCD es {mcd}")