import random
try:
    numero = int(input("Escribe un numero entre el 4 y el 100: "))
except:
    print("el numero es invalido")
if numero <= 4 or numero >= 100:
    print("Teclea un numero dentro del rango")
    exit()
lista = [random.randint(0,100) for _ in range(numero)]
matriz = [[0] * numero for _ in range(numero)]
for i in range(numero):
    matriz[i][i] = lista[i]
print(lista)
print("Matriz: ")
for fila in matriz:
    print(fila)

# ##list lista = new list[numero]
# i = 0
# lista = []
# while i <= numero:
#     n = random.randint(4,100)
#     lista.append(n)
#     i+1
# for i in range(0,numero):
#     print(lista[i])