nombre = "Panchito"
nombreInvertido = nombre[::-1]
salida = " ".join(nombreInvertido)
cadena_modificada = ""
for i in range(len(salida)):
    if i % 2 == 0:  # Comprueba si la posición es par (0, 2, 4, ...)
        cadena_modificada += salida[i].upper()  # Convierte a mayúscula el carácter en la posición par
    else:
        cadena_modificada += salida[i] 
print(salida)
print(cadena_modificada)