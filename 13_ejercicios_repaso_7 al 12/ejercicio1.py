# Hacer un programa que tenga una lista de 8 numeros enteros y realice lo siguiente: 

#  a.- Recorrer la lista y mostrarla
#  b.- hacer una funcion que recorra la lista de numeros y devuelva un string
#  c.- ordenarla y mostrarla
#  d.- mostrar su longitud
#  e.- buscar algun elemento que el usuario pida por teclado

numeros = [1, 2, 3, 4, 5, 6, 7, 8]

#A:
print("Recorrer la lista y mostrarla:")
for numero in numeros:
    print(numero)

#B:
def recorrer_lista(lista):
    return ", ".join(map(str, lista))

print("\n Función que recorre la lista y devuelve un string:")
print(recorrer_lista(numeros))

#C:
numeros_ordenados = sorted(numeros)
print("\nLista ordenada:")
print(numeros_ordenados)

#D:
print("\nLongitud de la lista:")
print(len(numeros))

#E:
def buscar_elemento(lista, elemento):
    if elemento in lista:
        return f"El elemento {elemento} se encuentra en la lista."
    else:
        return f"El elemento {elemento} NO se encuentra en la lista."

elemento_buscado = int(input("\nIntroduzca el elemento a buscar: "))
print(buscar_elemento(numeros, elemento_buscado))
