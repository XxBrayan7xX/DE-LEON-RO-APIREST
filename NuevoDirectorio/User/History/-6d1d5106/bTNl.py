numero = int(input("Dame el numero:  "))
i = 0
while i < 10:
    if pow(2,i) >= numero:
        print(pow(2,i))
        break
    i = i + 1
if 2^1 == numero:
    print (numero)