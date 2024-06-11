import { factorial } from "./factorial.js";

export function permutacionRepetida(n, stringNum) { 
    // Complejidad en tiempo de la función: O(n**2)
    
    const numeros = stringNum.split(",").map(numero => parseInt(numero)); 
    // Complejidad en tiempo: O(1); Complejidad Espacial O(n)

    let denominador = 1; 
    // Complejidad en tiempo: O(1); Complejidad Espacial O(1)
    
    for (const numero of numeros) { 
        // Complejidad en tiempo: O(n)

        let num = factorial(numero); 
        // Complejidad en tiempo: O(n**2); Complejidad Espacial O(1)

        denominador *= num; 
        // Complejidad en tiempo: O(n); Complejidad Espacial O(1)
    }
    
    return factorial(n) / denominador; 
    // Complejidad en tiempo: O(1)
}

//Ecuación: O(n**2) + 2 O(n) + 5 O(1)
// O(n**2)