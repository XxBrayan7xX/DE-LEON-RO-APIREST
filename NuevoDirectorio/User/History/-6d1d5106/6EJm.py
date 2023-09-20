numero = int(input("Dame el numero:  "))
i = 0
while i < 10:
    if pow(2,i) >= numero:
        print(pow(2,i))
        break
    i + 1
    print(i)
if 2^1 == numero:
    print (numero)