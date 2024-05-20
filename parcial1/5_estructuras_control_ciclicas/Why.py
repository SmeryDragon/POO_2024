#El while es una estructura de control repetitiva o ciclica que funciona con iteraciones X veces 

#Sintaxi

#for variable in elemento_iterable(list,range,etc):
#.....bloque instrucciones

#Ejemplo 1 crear un programa que imprima 5 veces el caracter @

contador=1
while contador<=5:
     r=0
     print("@")
     r+=1


#Ejemplo 2 Crear un programa que imprima los numeros del 1 a 5,,los sume e imprima la suma al final

 suma=0
contador=1
while contador<=5:
     print(contador)
     suma+=1
print(f"La suma es: {suma}")
#      suma+=contador
# print(f"La suma es: {suma}")


# #Ejemplo 3Crear un programa que solicite un numero entero y apartir de este numero genere e imprima la tabla de multiplicarr correspondiente

numero=int(input("Ingrese un numero:"))
multi=0
i=1
while i<=10:
      multi=numero*i
      i+=1
      print(f"{numero} X {i} = {multi}")
      i+=1
