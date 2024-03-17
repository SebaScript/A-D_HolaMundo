import { contieneNoNumerico } from "./permutacion.js";

export function principioAditivo(numeros){ //Complejidad en tiempo de la función: O(n);
    let listaNumeros = numeros.split(",").map(numero => parseInt(numero)); //Complejidad en tiempo: O(1); Complejidad Espacial O(n)

    if (contieneNoNumerico(listaNumeros)){ //Complejidad en tiempo: O(1)

        return "Error, ingresaste un valor no numérico"//Complejidad en tiempo: O(1)
    }

    let total = 0; //Complejidad en tiempo: O(1); Complejidad Espacial O(1)

    for (let i = 0; i < listaNumeros.length; i++) { //Complejidad en tiempo: O(n)

    total += listaNumeros[i]; //Complejidad en tiempo: O(n); Complejidad Espacial O(1)
    
    }
    return total; //Complejidad en tiempo: O(1)
}

//Ecuacion: 2 O(n) + 5 O(1)
// O(n)