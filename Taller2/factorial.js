export function factorial(num){ //Complejidad en tiempo de la función: O(n)

    let respuesta = 1 //Complejidad en tiempo: O(1); Complejidad Espacial O(1)

    for(let i = 1; i <= num;i++){ // Complejidad en tiempo: O(n)
        
        respuesta*=i // Complejidad en tiempo: O(n); Complejidad Espacial O(1)
    }
    return respuesta // Complejidad en tiempo: O(1)
}
// Ecuación: 2 O(n) + 2 O(1)
// O(n)