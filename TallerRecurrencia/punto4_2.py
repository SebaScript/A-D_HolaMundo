from gmpy2 import mpz # pip install gmpy2
from math import ceil

# N SIEMPRE DEBE SER MAYOR O IGUAL A 2

# Las posibles minimas diferencias entre el resultado de la función recursiva y la no recursiva
# Se deben a que la elevacion en python pierde precision cada que el exponente va aumentando.

# Punto 4) 1) recursivo

def punto_4_2_recursivo(n):
    if n == 0:
        return 8
    
    if n == 1:
        return -32
    
    else:
        return (((11 * (punto_4_2_recursivo(n-1))) - (5 * (punto_4_2_recursivo(n-2))))/2)

try:
    # Ingresar n
    n: int = 3
    if n < 0:
        print("n debe ser mayor o igual a cero")
    else:
        print("4) 1) Recursivo (n = 3): ", ceil(punto_4_2_recursivo(n))) # -998
except TypeError:
    print("Ingrese un n entero positivo mayor o igual que dos")
except RecursionError:
    print("Se ha ingresado un numero muy grande que supera la profundidad de recursión")



# Punto 4) 1) no recursivo

def punto_4_2_no_recursivo(n):

    if n > 1000:    
        resultado = ((16) * (mpz(1/2) ** (n)) + ((-8) * (mpz(5) ** (n))))
    
    else: 
        resultado = ceil((16) * ((1/2) ** (n))) + ((-8) * ((5) ** (n)))
    
    return resultado


try:
    # Ingresar n
    n: int = 3
    if n < 0:
        print("n debe ser mayor o igual a cero")
    else:
        print("4) 1) No recursivo (n = 3): ", punto_4_2_no_recursivo(n)) # -998
except TypeError:
    print("Ingrese un n entero positivo mayor o igual que dos")

#Se demora un poquito y retorna un numero gigantesco
print("4) 1) para n = 151’145.018: ", punto_4_2_no_recursivo(151145018))
