# Resuelve el problema de las Torres de Hanoi sin usar recursión.
def resolver_hanoi(n, origen, auxiliar, objetivo):
    mov_totales = 2**n - 1

    for i in range(1, mov_totales + 1):
        if i % 3 == 1:
            mover(origen, objetivo)
        elif i % 3 == 2:
            mover(origen, auxiliar)
        else:
            mover(auxiliar, objetivo)
        
        print(origen, objetivo, auxiliar)


def mover(desde, hasta):
    if desde and (not hasta or desde[-1] < hasta[-1]):
        hasta.append(desde.pop())
    else:
        desde.append(hasta.pop())


origen = [4, 3, 2, 1]
objetivo = []
auxiliar = []

print(origen, objetivo, auxiliar)
resolver_hanoi(len(origen), origen, auxiliar, objetivo)
