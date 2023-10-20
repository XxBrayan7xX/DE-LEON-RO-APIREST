/**
 * @
 */
let frases=[
    "El único lugar en que el éxito viene antes que el trabajo es en el diccionario",
 "No cuentes los días, haz que los días cuenten",
"El destino mezcla las cartas, y nosotros las jugamos",
"Las convicciones tienen el poder de crear y el poder de destruir",
"El mejor placer de la vida es hacer las cosas que la gente dice que no podemos hacer"
]
/**
 * Esta funcion obtiene espera como parametroo indice y retorona algo en base a eso
 * @param {Number} indice Debe ser un numero entero.
 * @returns Esta funcio regresa un frase, segun el indice que reciba.
 */
function obtenerFrase(indice){
    return frases[indice]
}

module.exports.obtenerFrase = obtenerFrase;
//console.log(module);