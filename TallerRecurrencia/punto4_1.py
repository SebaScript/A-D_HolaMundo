from decimal import Decimal
from math import ceil

# N SIEMPRE DEBE SER MAYOR O IGUAL A 2

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
        print("4) 1) Recursivo: ", punto_4_1_recursivo(n)) # 2964
except TypeError:
    print("Ingrese un n entero positivo mayor o igual que dos")
except RecursionError:
    print("Se ha ingresado un numero muy grande que supera la profundidad de recursión")

# Punto 4) 1) no recursivo

def punto_4_1_no_recursivo(n):
    
    resultado = (12/7 * (mpz(-1) ** (n)) + ((16/7) * mpz(6) ** (n)))

    # Se hace esta comprobación ya que el módulo Decimal a veces retorna valores incorrectos demasiado cercanos al número esperado
    if (resultado - (0.00000001)) < resultado or (resultado + (0.00000001)) > resultado:
        return ceil(resultado)
    
    return resultado


try:
    # Ingresar n
    n: int = 4
    if n < 2:
        print("n debe ser mayor o igual a dos")
    else:
        print("4) 1) No recursivo: ", punto_4_1_no_recursivo(n)) # 2964
except TypeError:
    print("Ingrese un n entero positivo mayor o igual que dos")

# FALTA AGREGAR PARA n = 151’145.018.