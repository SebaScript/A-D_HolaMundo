export function factorial(num){
    let respuesta = 1
    for(let i = 1; i <= num;i++){
        respuesta*=i
    }
    return respuesta
}