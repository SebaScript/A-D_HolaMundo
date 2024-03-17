import {factorial} from "./factorial.js";
import {permutacionRepetida} from "./permutacion.js";
import {principioAditivo} from "./PrincipioAditivo.js";
import { principioMultiplicativo } from "./PrincipioMultiplicativo.js";

// Calculadora de permutación sin repetición
document.getElementById('btn_perm_sin_rep').addEventListener('click', function PermutacionSinRep() {

    let n = parseInt(document.getElementById('n_perm_sin_rep').value); //Complejidad en tiempo: O(1); Complejidad Espacial O(1)

    let resultado = factorial(n); //Complejidad en tiempo: O(n); Complejidad Espacial O(1)

    document.getElementById('res_perm_sin_rep').textContent = resultado; //Complejidad en tiempo: O(1); Complejidad Espacial O(1)
});

// Calculadora de permutación con repetición
document.getElementById('btn_perm_con_rep').addEventListener('click', function PermutacionConRep() {

    let n = parseInt(document.getElementById('n_perm_rep').value); //Complejidad en tiempo: O(1); Complejidad Espacial O(1)

    let numeros = document.getElementById("numeros_perm_rep").value; //Complejidad en tiempo: O(1); Complejidad Espacial O(1)

    let resultado = permutacionRepetida(n,numeros) //Complejidad en tiempo: O(n**2); Complejidad Espacial O(1)
    
    document.getElementById("res_perm_rep").textContent = resultado; //Complejidad en tiempo: O(1); Complejidad Espacial O(1)
});

// Calculadora Principio aditivo
document.getElementById("btn_prin_aditivo").addEventListener('click', function aditivo(){
    let numeros = document.getElementById("numeros_aditivo").value; //Complejidad en tiempo: O(1); Complejidad Espacial O(1)

    let resultado = principioAditivo(numeros) //Complejidad en tiempo: O(n); Complejidad Espacial O(1)

    document.getElementById("res_aditivo").textContent = resultado; //Complejidad en tiempo: O(1); Complejidad Espacial O(1)
})

//Calculadora Principio Multiplicativo
document.getElementById("btn_prin_multiplicativo").addEventListener('click', function multiplicativo(){
    let numeros = document.getElementById("numeros_multiplicativo").value; //Complejidad en tiempo: O(1); Complejidad Espacial O(1)

    let resultado = principioMultiplicativo(numeros) //Complejidad en tiempo: O(n); Complejidad Espacial O(1)

    document.getElementById("res_multiplicativo").textContent = resultado; //Complejidad en tiempo: O(1); Complejidad Espacial O(1)
})
