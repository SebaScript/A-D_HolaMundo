#Crea una función recursiva que sume todos los elementos de un array

def sumar_array(array):
    if len(array) == 0:
        return 0
    if len(array) == 1:
        return array[0]
    else:
        return array[0] + sumar_array(array[1:])

numeros = [1, 2, 3, 4, 5, 7]
resultado = sumar_array(numeros)
print(f"La suma de los valores del Array {numeros} es {resultado}")