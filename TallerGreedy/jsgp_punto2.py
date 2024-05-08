""" Dado un número N. Encuentra el número mínimo de operaciones necesarias 
para llegar a N  a partir de 0 . Tienes 2 operaciones disponibles:
1. Duplicar el numero
2. Añadir uno al número"""

# Juan Sebastian García Perez - Función Greedy. 
# Retorna el número mínimo de operaciones necesarias en la mayoría de los casos, pero en algunos casos el reusltado es
# Ligeramente mayor al esperado.
def punto2(N, resultado = 0, operaciones = 0):
    if resultado == N:
        return operaciones
    
    if resultado == 0 or (resultado * 2) > N:
        return punto2(N, resultado+1, operaciones+1)
    else:
        return punto2(N, resultado*2, operaciones+1)


#Interfaz por consola
print("""Algoritmo Greedy para encontrar el número mínimo de operaciones necesarias para llegar a un número N a partir de 0 con 2 operaciones:
        1. Duplicar el numero
        2. Añadir uno al número\n""")

while True:
    print("Menú de opciones") 

    try:
        opcion: int = int(input("""1) Ingresar un numero N\n2) Salir del programa\n: """))
        
        if opcion not in (1,2):
            print("\nIngrese 1 o 2\n")
            continue

    except:
        print("\nIngrese 1 o 2\n")
        continue
    
    if opcion == 1:
        try:
            N: int = int(input("Ingresa el número N: "))
            print("\n")

            if N <= 0:
                print("Ingrese un número entero mayor a cero")
                print("\n")
                continue
            
            print(f"El resultado es: {punto2(N)}\n")

        except Exception:
            print("\nIngrese un número entero mayor a cero\n")
            continue
    else:
        exit()
