num1=int(input("Ingrese el primer numero: "))
num2=int(input("ingrese el segundo numero: "))


num1+=1
for num in range(num1,num2):
    if num%2!=0:
       print(num)