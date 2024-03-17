import { factorial } from "./factorial.js";

export function permutacionRepetida(n,stringNum){ //Complejidad en tiempo de la función: O(n**2);
    
    const numeros = stringNum.split(",").map(numero => parseInt(numero)); //Complejidad en tiempo: O(1); Complejidad Espacial O(n)

    if (contieneNoNumerico(numeros)){ //Complejidad en tiempo: O(1);

        return "Error, ingresaste un valor no numérico" //Complejidad en tiempo: O(1);
    }
    let denominador = 1 //Complejidad en tiempo: O(1); Complejidad Espacial O(1)
    
    for(let i = 0;i<numeros.length;i++){ //Complejidad en tiempo: O(n);

        let num = factorial(numeros[i]) //Complejidad en tiempo: O(n**2); Complejidad Espacial O(1)

        denominador*=num //Complejidad en tiempo: O(n); Complejidad Espacial O(1)
        
    }
    return factorial(n)/denominador //Complejidad en tiempo: O(1);
}
//Ecuación: O(n**2) + 2 O(n) + 5 O(1)
// O(n**2)



export function contieneNoNumerico(array) { //Complejidad en tiempo de la función: O(1);
    
    return array.some(elemento => isNaN(elemento)); //Complejidad en tiempo: O(1);
}
//Ecuación: 2 O(1)
// O(1)