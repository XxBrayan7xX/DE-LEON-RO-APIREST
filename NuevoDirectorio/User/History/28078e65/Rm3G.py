import random

num = int(input("Dame un numero entre 2 y 10: "))
if(num < 2 or num > 10):
    print("Dame un numero entre 2 y 10!")
##lista = [random.randint(0,100) for _ in range(num)]
matriz = [[0] * num for _ in range(num)]
for i in range(num):
    for j in range(num):
        matriz[i][j] = random.randint(0,100)
matrix = np.sort(matriz)
print(matrix)
ban = False
menor = 0
for i in range(num):
    for j in range(num):
            if(menor > matriz[i][j])
        