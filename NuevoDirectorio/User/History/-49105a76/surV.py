import random
try:
    numero = int(input("Escribe un numero entre el 4 y el 100: "))
except:
    print("el numero es invalido")
if numero <= 4 or numero >= 100:
    print("Teclea un numero dentro del rango")
    exit()
##list lista = new list[numero]
i = 0
lista = []
while i <= numero:
    n = random.randint(4,100)
    lista.append(n)
    i+1
print(lista)
