export function principioMultiplicativo(numerosMultiplicativo){ //Complejidad en tiempo de la función: O(n);
    let listaNumeros = numerosMultiplicativo.split(",").map(numero => parseInt(numero)); //Complejidad en tiempo: O(1); Complejidad Espacial O(n)

    let total = 1; //Complejidad en tiempo: O(1); Complejidad Espacial O(1)

    for (let i = 0; i < listaNumeros.length; i++) { //Complejidad en tiempo: O(n)

    total *= listaNumeros[i]; //Complejidad en tiempo: O(n) ; Complejidad Espacial O(1)
    
    }
    return total; //Complejidad en tiempo: O(1)
}
//Ecuacion: 2 O(n) + 5 O(1)
// O(n)