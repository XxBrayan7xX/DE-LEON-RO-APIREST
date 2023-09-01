let frases=[
    "El único lugar en que el éxito viene antes que el trabajo es en el diccionario",
 "No cuentes los días, haz que los días cuenten",
"El destino mezcla las cartas, y nosotros las jugamos",
"Las convicciones tienen el poder de crear y el poder de destruir",
"El mejor placer de la vida es hacer las cosas que la gente dice que no podemos hacer"
]
export function obtenerFrase(){
    var numeroAleatorioEntero = Math.floor(Math.random() * 5);
    return frases[numeroAleatorioEntero]
}

