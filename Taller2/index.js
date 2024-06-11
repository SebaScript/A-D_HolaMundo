import {factorial} from "./factorial.js";
import {permutacionRepetida} from "./permutacion.js";
import {principioAditivo} from "./principioAditivo.js";
import { principioMultiplicativo } from "./principioMultiplicativo.js";
import {combinacionesConRepeticion, combinacionesSinRepeticion} from "./combinacion.js"
import { variacionNoRepetida, variacionRepetida } from "./variacion.js";


// Calculadora de permutación sin repetición
document.getElementById('btn_perm_sin_rep').addEventListener('click', function PermutacionSinRep() {

    let n = document.getElementById('n_perm_sin_rep').value; //Complejidad en tiempo: O(1); Complejidad Espacial O(1)

    if (validarInput(n)){
        n = parseInt(n)
        let resultado = factorial(n); //Complejidad en tiempo: O(n); Complejidad Espacial O(1)

        document.getElementById('res_perm_sin_rep').textContent = resultado; //Complejidad en tiempo: O(1); Complejidad Espacial O(1)
    } else {
        alert("Por favor, ingrese un valor válido que sea un número entero mayor o igual a 1 y tenga como máximo 3 cifras.")
    }
});


// Calculadora de permutación con repetición
document.getElementById('btn_perm_con_rep').addEventListener('click', function PermutacionConRep() {

    let n = document.getElementById('n_perm_rep').value; //Complejidad en tiempo: O(1); Complejidad Espacial O(1)
    let numeros = document.getElementById("numeros_perm_rep").value; //Complejidad en tiempo: O(1); Complejidad Espacial O(1)

    if (validarInput(n)){
        n = parseInt(n)
        if (validarListaNumeros(numeros)) {  
            if (validarRepeticionPermutacion(n, numeros)){
                let resultado = permutacionRepetida(n,numeros) //Complejidad en tiempo: O(n**2); Complejidad Espacial O(1)
                document.getElementById("res_perm_rep").textContent = resultado; //Complejidad en tiempo: O(1); Complejidad Espacial O(1)
            } else {
                alert("los numeros a,b,c... sumados deben ser menores que n")
            }
        } else {
            alert("Por favor, ingrese un valor válido que sea un número entero mayor o igual a 1 y tenga como máximo 3 cifras. Ingrese los números separados por 1 coma.")
        }
    } else {
        alert("Por favor, ingrese un valor válido que sea un número entero mayor o igual a 1 y tenga como máximo 3 cifras.")
    }
});


// Calculadora Principio aditivo
document.getElementById("btn_prin_aditivo").addEventListener('click', function aditivo(){
    let numeros = document.getElementById("numeros_aditivo").value; //Complejidad en tiempo: O(1); Complejidad Espacial O(1)

    if (validarListaNumeros(numeros)) {
        let resultado = principioAditivo(numeros) //Complejidad en tiempo: O(n); Complejidad Espacial O(1)
        document.getElementById("res_aditivo").textContent = resultado; //Complejidad en tiempo: O(1); Complejidad Espacial O(1)
    } else {
        alert("Por favor, ingrese un valor válido que sea un número entero mayor o igual a 1 y tenga como máximo 3 cifras. Ingrese los números separados por 1 coma.")
    }
});


//Calculadora Principio Multiplicativo
document.getElementById("btn_prin_multiplicativo").addEventListener('click', function multiplicativo(){
    let numeros = document.getElementById("numeros_multiplicativo").value; //Complejidad en tiempo: O(1); Complejidad Espacial O(1)

    if (validarListaNumeros(numeros)) {
        let resultado = principioMultiplicativo(numeros) //Complejidad en tiempo: O(n); Complejidad Espacial O(1)
        document.getElementById("res_multiplicativo").textContent = resultado; //Complejidad en tiempo: O(1); Complejidad Espacial O(1)
    } else {
        alert("Por favor, ingrese un valor válido que sea un número entero mayor o igual a 1 y tenga como máximo 3 cifras. Ingrese los números separados por 1 coma.")
    }
});


//Calculadora Combinación con repetición
document.getElementById("btn_comb_rep").addEventListener('click', function combinacionRep(){
    let m = document.getElementById("m_comb_rep").value; //Complejidad en tiempo: O(1); Complejidad Espacial O(1)
    

    let n = document.getElementById("n_comb_rep").value; //Complejidad en tiempo: O(1); Complejidad Espacial O(1)

    if (validarInput(m) && validarInput(n)) {
        m = parseInt(m)
        n = parseInt(n)
        if (m > n) {
            let resultado = combinacionesConRepeticion(parseInt(m), parseInt(n)) //Complejidad en tiempo: O(1); Complejidad Espacial O(1)

            document.getElementById("res_comb_rep").textContent = resultado; //Complejidad en tiempo: O(1); Complejidad Espacial O(1)
        } else {
            alert("m debe ser mayor que n.")
        }
    } else {
        alert("Por favor, ingrese un valor válido que sea un número entero mayor o igual a 1 y tenga como máximo 3 cifras.")
    }
});


//Calculadora Combinación sin repetición
document.getElementById("btn_comb_sin_rep").addEventListener('click', function combinacionSinRep(){

    let m = document.getElementById("m_comb_sin_rep").value; //Complejidad en tiempo: O(1); Complejidad Espacial O(1)

    let n = document.getElementById("n_comb_sin_rep").value; //Complejidad en tiempo: O(1); Complejidad Espacial O(1)

    if (validarInput(m) && validarInput(n)) {
        m = parseInt(m)
        n = parseInt(n)

        if (m > n){
            let resultado = combinacionesSinRepeticion(m, n) //Complejidad en tiempo: O(1); Complejidad Espacial O(1)

            document.getElementById("res_comb_sin_rep").textContent = resultado; //Complejidad en tiempo: O(1); Complejidad Espacial O(1)
        } else {
            alert("m debe ser mayor que n")
        }
    } else {
        alert("Por favor, ingrese un valor válido que sea un número entero mayor o igual a 1 y tenga como máximo 3 cifras.")
    }
});


// Calculadora variación con repetición
document.getElementById("btn_var_rep").addEventListener('click', function variacionRep(){

    let m = document.getElementById("m_var_rep").value; //Complejidad en tiempo: O(1); Complejidad Espacial O(1)

    let n = document.getElementById("n_var_rep").value; //Complejidad en tiempo: O(1); Complejidad Espacial O(1)

    if (validarInput(m) && validarInput(n)) {
        m = parseInt(m)
        n = parseInt(n)
        if (m > n){
            let resultado = variacionRepetida(m, n) //Complejidad en tiempo: O(1); Complejidad Espacial O(1)

            document.getElementById("res_var_rep").textContent = resultado; //Complejidad en tiempo: O(1); Complejidad Espacial O(1)
        } else {
            alert("m debe ser mayor que n")
        }
    } else {
        alert("Por favor, ingrese un valor válido que sea un número entero mayor o igual a 1 y tenga como máximo 3 cifras.")
    }
});



// Calculadora variación sin repetición
document.getElementById("btn_var_sin_rep").addEventListener('click', function variacionSinRep(){

    let m = document.getElementById("m_var_sin_rep").value; //Complejidad en tiempo: O(1); Complejidad Espacial O(1)

    let n = document.getElementById("n_var_sin_rep").value; //Complejidad en tiempo: O(1); Complejidad Espacial O(1)

    if (validarInput(m) && validarInput(n)) {
        m = parseInt(m)
        n = parseInt(n)
        if (m > n){
            let resultado = variacionNoRepetida(m, n) //Complejidad en tiempo: O(1); Complejidad Espacial O(1)

            document.getElementById("res_var_sin_rep").textContent = resultado; //Complejidad en tiempo: O(1); Complejidad Espacial O(1)
        } else {
            alert("m debe ser mayor que n")
        }
    } else {
        alert("Por favor, ingrese un valor válido que sea un número entero mayor o igual a 1 y tenga como máximo 3 cifras.")
    }
});


function validarInput(valor) {
    return !(valor.length > 3 || isNaN(valor) || !Number.isInteger(parseFloat(valor)) || parseFloat(valor) < 1)
};


function validarListaNumeros(lista) {
    const numeros = lista.split(',')

    for (let i = 0; i < numeros.length; i++) {
        const numero = numeros[i].trim()
        if (!validarInput(numero)) {
            return false
        }
    }

    return true;
};


function validarRepeticionPermutacion(n, lista) {
    const numeros = lista.split(',')
    let suma = 0
    for (let i = 0; i < numeros.length; i++) {
        console.log(suma)
        const numero = parseInt(numeros[i].trim())
        suma += numero
        if (suma > n) {
            return false
        }
    }

    return true;
};
