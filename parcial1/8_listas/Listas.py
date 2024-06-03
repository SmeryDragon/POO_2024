# list(Array)
# son colecciones o conjunto de datos/valores bajo un mismo nombre, para acceder a los valores se hace con un indice numerico

# nota: sus valores si son modificables

# La lista es una coleccion ordenada y modificable
# Permite miembros duplicados

#Ejemplo 1 crear una lista de numeros e imprimir el contenido

numeros=[23,34]
print(numeros)

#Recorrer la lista con ciclo for
for i  in numeros:
    print(i)

#Recorrer la lista con cicloo while
i=0
while i<=len(numeros)-1:
    print(numeros[i])
    i+=1

#Ejemplo 2 crear una lista de palabras y posteriormente buscar la coincidencia de una palabra 

palabras=["naranja","utd","saludos","america","azul"]

palabra_buscar=input("ingresa la palabra a buscar: ")

if palabras:
    print("Encontre la palabra")
else:
    print("No encontre la palabra")
