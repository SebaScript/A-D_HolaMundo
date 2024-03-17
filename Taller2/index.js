import {factorial} from "./factorial.js";
import { permutacionRepetida } from "./permutacion.js";

// Calculadora de permutación sin repetición
document.getElementById('btn_perm_sin_rep').addEventListener('click', function PermutacionSinRep() {
    let n = parseInt(document.getElementById('n_perm_sin_rep').value);
    console.log("llamando funcion perm")
    let resultado = factorial(n);
    document.getElementById('res_perm_sin_rep').textContent = resultado;
});

// Calculadora de permutación con repetición
document.getElementById('btn_perm_con_rep').addEventListener('click', function PermutacionConRep() {
    let n = parseInt(document.getElementById('n_perm_rep').value);
    let numeros = document.getElementById("numeros_perm_rep").value;
    let resultado = permutacionRepetida(n,numeros)
    document.getElementById("res_perm_rep").textContent = resultado;
});