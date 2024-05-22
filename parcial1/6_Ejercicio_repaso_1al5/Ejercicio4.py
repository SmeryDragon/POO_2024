#Solicitar 2 numeros al usuario
# y realizar todas las operaciones
# basicas de una calculadora (+,-,*,/)
# y mostrar por pantalla el resultado

 
num1=int(input("Ingrese el primer numero:"))
num2=int(input("Ingrese el segundo numero:"))

suma=num1+num2
resta=num1-num2
div=num1/num2
mul=num1*num2

print(f"RESULTADO SUMA: {suma}")
print(f"RESULTADO RESTA: {resta}")
print(f"RESULTADO DIVISIÓN: {div}")
print(f"RESULTADO MULTIPLICACION: {mul}")