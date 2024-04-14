from decimal import Decimal
from math import ceil

# N SIEMPRE DEBE SER MAYOR O IGUAL A 2

# Punto 4) 1) recursivo

def punto_4_2_recursivo(n):
    if n == 0:
        return 8
    
    if n == 1:
        return 12
    
    else:
        return ((11 * (punto_4_2_recursivo(n-1))) - (5 * (punto_4_2_recursivo(n-2))))/2

try:
    # Ingresar n
    n: int = 3
    if n < 0:
        print("n debe ser mayor o igual a cero")
    else:
        print("4) 1) Recursivo: ", punto_4_2_recursivo(n)) # 223
except TypeError:
    print("Ingrese un n entero positivo mayor o igual que dos")
except RecursionError:
    print("Se ha ingresado un numero muy grande que supera la profundidad de recursión")

# Punto 4) 1) no recursivo

def punto_4_2_no_recursivo(n):
    
    resultado = (Decimal(56/9) * (Decimal(1/2) ** Decimal(n)) + (Decimal(16/9) * Decimal(5) ** Decimal(n)))

    # Se hace esta comprobación ya que el módulo Decimal a veces retorna valores incorrectos demasiado cercanos al número esperado
    if (resultado - Decimal(0.00000001)) < resultado or (resultado + Decimal(0.00000001)) > resultado:
        return ceil(resultado)
    
    return resultado


try:
    # Ingresar n
    n: int = 3
    if n < 0:
        print("n debe ser mayor o igual a cero")
    else:
        print("4) 1) No recursivo: ", punto_4_2_no_recursivo(n)) # 223
except TypeError:
    print("Ingrese un n entero positivo mayor o igual que dos")

# FALTA AGREGAR PARA n = 151’145.018.