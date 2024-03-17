import {factorial} from "./factorial.js";
import { permutacionRepetida } from "./permutacion.js";
function calcular() {
    var m = document.getElementById('m_comb_rep').value;
    var n = document.getElementById('n_comb_rep').value;
    var resultado = Number(m) + Number(n); // Suma los valores de los inputs
    document.getElementById('res_comb_rep').innerText = resultado; // Muestra el resultado en el span
}

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