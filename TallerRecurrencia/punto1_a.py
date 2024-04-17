from decimal import Decimal
from math import ceil

# Punto 1) a) recursivo

def punto_1_a_recursivo(n):
    if n == 0:
        return 2
    else:
        return 5 * punto_1_a_recursivo(n-1)

try:
    # Ingresar n
    n: int = 100
    if n < 0:
        print("n debe ser mayor o igual a cero")
    else:
        print("1) a) Recursivo: ", punto_1_a_recursivo(n)) # 15777218104420236108234571305655724593464128702180460095405578613281250
except TypeError:
    print("Ingrese un n entero positivo mayor o igual que cero")
except RecursionError:
    print("Se ha ingresado un numero muy grande que supera la profundidad de recursión")

# Punto 1) a) no recursivo:

def punto_1_a_no_recursivo(n):
    if n < 0:
        return "n debe ser mayor o igual a cero"
    
    resultado = (Decimal(5) ** Decimal(n)) * Decimal(2)

    # Se hace esta comprobación ya que el módulo Decimal a veces retorna valores incorrectos demasiado cercanos al número esperado
    if (resultado - Decimal(0.00000001)) < resultado or (resultado + Decimal(0.00000001)) > resultado:
        return ceil(resultado)
    
    return resultado

""" En este caso si es posible ingresar n muy grandes, ya que la recursión no es un limitante en este caso y con el
 módulo decimal se pueden obtener números muy grandes """

try:
    # Ingresar n
    n: int = 100
    if n < 0:
        print("n debe ser mayor o igual a cero")
    else:
        print("1) a) No recursivo: ", punto_1_a_no_recursivo(n)) # 1.577721810442023610823457131E+70
except TypeError:
    print("Ingrese un n entero positivo mayor o igual que cero")
