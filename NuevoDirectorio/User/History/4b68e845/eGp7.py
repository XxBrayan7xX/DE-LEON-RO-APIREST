import os

def encontrar_posicion_inicial(archivo, palabra_buscada):
    # Obtener la ruta absoluta del archivo
    archivo = os.path.abspath(archivo)

    if not os.path.exists(archivo):
        return f"El archivo '{archivo}' no se encuentra."

    try:
        with open(archivo, 'r', encoding='utf-8') as archivo_texto:
            texto = archivo_texto.read()
    except FileNotFoundError:
        return "Error al abrir el archivo."

    # Tokenizar el texto en palabras
    palabras = texto.split()

    # Inicializar una lista para almacenar las posiciones iniciales de las palabras
    posiciones_iniciales = []

    # Variable para llevar un seguimiento de la posición actual en el texto
    posicion_actual = 0

    for palabra in palabras:
        # Eliminar puntuación al final de la palabra y convertirla a minúsculas
        palabra = palabra.strip('.,!?').lower()

        if palabra == palabra_buscada.lower():
            # Guardar la posición inicial de la palabra (posición_actual + 1)
            posiciones_iniciales.append(posicion_actual + 1)

        # Actualizar la posición actual agregando la longitud de la palabra más un espacio
        posicion_actual += len(palabra) + 1

    return f'La palabra "{palabra_buscada}" comienza en las posiciones: {posiciones_iniciales}'


# Ejemplo de uso
archivo = "miTexto.txt"  # Reemplaza con el nombre de tu archivo de texto
palabra_buscada = "cambio"  # Reemplaza con la palabra que deseas buscar
resultado = encontrar_posicion_inicial(archivo, palabra_buscada)
print(resultado)
