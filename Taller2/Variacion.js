import { factorial} from "./factorial.js";

export function variacionRepetida(m, n) {

   return Math.pow(m,n) // Complejidad en tiempo: O(n); Complejidad Espacial: O(1)
      
}
// Ecuación: O(n)
// Complejidad del algoritmo: O(n)

export function variacionNoRepetida(m, n){

    let numerador = factorial(m) // Complejidad en tiempo: O(n); Complejidad Espacial: O(1)
    let denominador = factorial(m - n) // Complejidad en tiempo: O(n); Complejidad Espacial: O(1)

    return numerador/denominador // Complejidad en tiempo: O(1)
}
// Ecuación: 2 O(n) + 1 O(1)
// Complejidad del algoritmo: O(n)
