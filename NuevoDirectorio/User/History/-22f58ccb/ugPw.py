def contar_palabra_y_posiciones(archivo, palabra_buscada):
    try:
        with open(archivo, 'r', encoding='utf-8') as archivo_texto:
            texto = archivo_texto.read()
    except FileNotFoundError:
        return "El archivo no se encuentra."

    # Dividir el texto en palabras
    palabras = texto.split()
    
    # Inicializar una lista para almacenar las posiciones de la palabra
    posiciones = []

    for i, palabra in enumerate(palabras):
        # Eliminar puntuación al final de la palabra y convertirla a minúsculas
        palabra = palabra.strip('.,!?').lower()
        
        if palabra == palabra_buscada.lower():
            # Guardar la posición de la palabra (indice + 1)
            posiciones.append(i + 1)

    cantidad_repeticiones = len(posiciones)

    return f'La palabra "{palabra_buscada}" se repite {cantidad_repeticiones} veces en las posiciones: {posiciones}'


# Uso de la función
archivo = "miTexto.txt"  
# Reemplaza con el nombre de tu archivo de texto
palabra_buscada = "cambio"  # Reemplaza con la palabra que deseas buscar
resultado = contar_palabra_y_posiciones(archivo, palabra_buscada)
print(resultado)
