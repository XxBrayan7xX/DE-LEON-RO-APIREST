num1 = input("Dame el primer numero: ")
if(len(num1)> 3 or len(num1)< 3):
    print("Deben ser tres digitos! ")
    exit()
num2 = input("Dame el segundo numero: ")
if(len(num2)> 3 or len(num2)< 3):
    print("Deben ser tres digitos! ")
    exit()
def reverseInteger(number):
    number=str(number)
    result=number[::-1]
    result=(int(result))
    return result
x = reverseInteger(num1)
y = reverseInteger(num2)
if(x > y):
    print(x)
elif(y > x):
    print(y)
else:
    print("Los numeros son igules.")