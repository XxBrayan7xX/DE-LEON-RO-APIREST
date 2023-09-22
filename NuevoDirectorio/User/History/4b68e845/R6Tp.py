import os

def buscarPalabra(archivo, PB):
    # Obtener la ruta absoluta del archivo
    archivo = os.path.abspath(archivo)

    if not os.path.exists(archivo):
        return f"El archivo '{archivo}' no se encuentra."

    try:
        with open(archivo, 'r', encoding='utf-8') as AT:
            texto = AT.read()
    except FileNotFoundError:
        return "Error al abrir el archivo."

    # Tokenizar el texto en palabras
    palabras = texto.split()

    # Inicializar una lista para almacenar las posiciones iniciales de las palabras
    PI = []

    # Variable para llevar un seguimiento de la posición actual en el texto
    posicion_actual = 0

    for palabra in palabras:
        # Eliminar puntuación al final de la palabra y convertirla a minúsculas
        palabra = palabra.strip('.,!?').lower()

        if palabra == PB.lower():
            # Guardar la posición inicial de la palabra (posición_actual + 1)
            PI.append(posicion_actual)

        # Actualizar la posición actual agregando la longitud de la palabra más un espacio
        posicion_actual += len(palabra) + 1

    return f'La palabra "{PB}" comienza en las posiciones: {PI}'


# Ejemplo de uso
archivo = "miTexto.txt"  # Reemplaza con el nombre de tu archivo de texto
PB = input("Dame una palabra: ") 
if PB == "":
    print("La cadena no debe estar vacia, intenta nuevamente")
    exit()
resultado = buscarPalabra(archivo, PB)
print(resultado)
