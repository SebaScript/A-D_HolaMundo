import { factorial} from "./factorial.js";

export function variacionRepetida(m, n) {

   return Math.pow(m,n)
      
}

export function variacionNoRepetida(m, n){
    
    let numerador = factorial(m)
    let denominador = factorial(m - n)

    return numerador/denominador
}