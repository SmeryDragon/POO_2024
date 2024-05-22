# Escribir un programa que muestre los cuadrados 
#(un numero multiplicado por si mismo) de los 60 primeros 
#numeros naturales. Resolverlo con while y for

#Ejemplo for
for contador in range(1,61):
     cuadrado=contador*contador
     print(cuadrado)
print(f"El cuadrado de {contador} es {cuadrado}")

#Ejemplo why
numero = 1
while numero <= 60:
    cuadrado = numero * numero
    print(f"El cuadrado de {numero} es {cuadrado}")
    numero += 1
