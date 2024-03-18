const { factorial } = require('./factorial.js');

// Función para calcular las combinaciones con repetición
function combinacionesConRepeticion(n, r) {
    return factorial(m + n - 1) / (factorial(n) * factorial(m - 1));
}


// Función para calcular las combinaciones sin repetición
function combinacionesSinRepeticion(n, r) {
    return factorial(m) / (factorial(n) * factorial(m - n));
}
