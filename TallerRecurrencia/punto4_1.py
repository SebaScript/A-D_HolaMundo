from gmpy2 import mpz # pip install gmpy2
from math import ceil 

# N SIEMPRE DEBE SER MAYOR O IGUAL A 2

# Las posibles minimas diferencias entre el resultado de la función recursiva y la no recursiva
# Se deben a que la elevacion en python pierde precision cada que el exponente va aumentando.

# Punto 4) 1) recursivo

def punto_4_1_recursivo(n):
    if n == 0:
        return 4
    
    if n == 1:
        return 12
    
    else:
        return (5 * (punto_4_1_recursivo(n-1))) + (6 * (punto_4_1_recursivo(n-2)))

try:
    # Ingresar n
    n: int = 4
    if n < 2:
        print("n debe ser mayor o igual a dos")
    else:
        print("4) 1) Recursivo (n = 4): ", punto_4_1_recursivo(n)) # 2964
except TypeError:
    print("Ingrese un n entero positivo mayor o igual que dos")
except RecursionError:
    print("Se ha ingresado un numero muy grande que supera la profundidad de recursión")



# Punto 4) 1) no recursivo

def punto_4_1_no_recursivo(n):
    
    if n > 1000:
        resultado = (12/7 * (mpz(-1) ** (n)) + ((16/7) * (mpz(6) ** (n))))

    else:
        resultado = ceil(12/7 * ((-1) ** (n)) + ((16/7) * ((6) ** (n))))
    
    return resultado


try:
    # Ingresar n
    n: int = 4
    if n < 2:
        print("n debe ser mayor o igual a dos")
    else:
        print("4) 1) No recursivo (n = 4): ", punto_4_1_no_recursivo(n)) # 2964
except TypeError:
    print("Ingrese un n entero positivo mayor o igual que dos")

#Se demora un poquito y retorna un número gigantesco
print("4) 1) para n = 151’145.018: ", punto_4_1_no_recursivo(151145018))
