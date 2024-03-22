import { factorial } from "./factorial.js";

export function combinacionesConRepeticion(m, n) {
    //combinaciones con repetición
    return factorial(m + n - 1) / (factorial(n) * factorial(m - 1)); // Complejidad en tiempo: O(n); Complejidad Espacial: O(1)
}
// Ecuación: 3 O(n) + O(1)
// O(n)


export function combinacionesSinRepeticion(m, n) {
    //combinaciones sin repetición
    return factorial(m) / (factorial(n) * factorial(m - n)); // Complejidad en tiempo: O(n); Complejidad Espacial: O(1)
}
// Ecuación: 3 O(n) + O(1)
// O(n)
