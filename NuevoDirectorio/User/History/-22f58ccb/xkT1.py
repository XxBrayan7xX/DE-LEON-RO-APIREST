import os
def contarPalabras(archivo, PB):
    archivo = os.path.abspath(archivo)

    if not os.path.exists(archivo):
        return f"El archivo '{archivo}' no se encuentra."

    try:
        with open(archivo, 'r', encoding='utf-8') as archivo_texto:
            texto = archivo_texto.read()
    except FileNotFoundError:
        return "Error al abrir el archivo."

    palabras = texto.split()
    
    posiciones = []

    for i, palabra in enumerate(palabras):
        palabra = palabra.strip('.,!?').lower()
        
        if palabra == PB.lower():
            posiciones.append(i + 1)

    c = len(posiciones)

    return f'La palabra "{PB}" se repite {c} veces en las posiciones: {posiciones}'


archivo = "miTexto.txt"  
PB = "cambio"  
resultado = contarPalabras(archivo, PB)
print(resultado)
