# Resuelve el problema de las Torres de Hanoi sin usar recursión.

def resolver_hanoi(n, origen, auxiliar, objetivo): # O(n)
    mov_totales = 2**n -1 # O(1)

    for i in range(1, mov_totales + 1): # O(n)
        if i % 3 == 1: # O(n)
            mover(origen, objetivo) # O(n)
        elif i % 3 == 2: # O(n)
            mover(origen, auxiliar) # O(n)
        else: # O(n)
            mover(auxiliar, objetivo) # O(n)
        
        print(origen, objetivo, auxiliar) # O(n)


def mover(desde, hasta): # O(1)
    if desde and (not hasta or desde[-1] < hasta[-1]): # O(1)
        hasta.append(desde.pop()) # O(1)
    else: # O(1)
        desde.append(hasta.pop()) # O(1)


origen = [5, 4, 3, 2, 1] # complejidad tiempo: O(1) ; complejidad espacial: O(n)
objetivo = [] # complejidad tiempo: O(1) ; complejidad espacial: O(n)
auxiliar = [] # complejidad tiempo: O(1) ; complejidad espacial: O(n)

print(origen, objetivo, auxiliar) # O(1)
resolver_hanoi(len(origen), origen, auxiliar, objetivo) # O(n)

# Ecuación: 2 O(n) + 5 O(1)
# Complejidad del algoritmo: O(n)
