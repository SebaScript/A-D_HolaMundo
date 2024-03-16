function calcular() {
    var m = document.getElementById('m_comb_rep').value;
    var n = document.getElementById('n_comb_rep').value;
    var resultado = Number(m) + Number(n); // Suma los valores de los inputs
    document.getElementById('res_comb_rep').innerText = resultado; // Muestra el resultado en el span
}
