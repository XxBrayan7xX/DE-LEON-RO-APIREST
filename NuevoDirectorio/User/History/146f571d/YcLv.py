num1 = int(input("Dame el primer numero: "))
num2 = int(input("Dame el segundo numero: "))
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