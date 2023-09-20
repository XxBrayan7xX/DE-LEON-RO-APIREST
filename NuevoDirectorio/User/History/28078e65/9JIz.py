import random
num = int(input("Dame un numero entre 2 y 10: "))
if(num < 2 or num > 10):
    print("Dame un numero entre 2 y 10!")
##lista = [random.randint(0,100) for _ in range(num)]
matriz = [[],[]]
for i in range(num):
    for j in range(num):
        matriz[i][j] = random.randint(0,100)
print(matriz)