import { factorial } from "./factorial.js";

export function permutacionRepetida(n,stringNum){
    console.log("llamada a la perm")
    const numeros = stringNum.split(",").map(numero => parseInt(numero));

    if (contieneNoNumerico(numeros)){
        return "Error, ingresaste un valor no numérico"
    }
    let denominador = 1
    
    for(let i = 0;i<numeros.length;i++){
        let num = factorial(numeros[i])

        denominador*=num
        
    }
    return factorial(n)/denominador
}

function contieneNoNumerico(array) {
    return array.some(elemento => isNaN(elemento));
}