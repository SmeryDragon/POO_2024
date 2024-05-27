#Una funcion es un conjunto de instrucciones agrupadas bajo un nombre en particular como un programa mas pequeño que cumple una funcion especifica.
#La funcion se puede reutilizar con el simple hecho de invocarla es decir mandarla llamar

#Sintaxis

def nombredeMifuncion(Parametros):
    Bloque o conjunto de instrucciones

    nombredeMifuncion(Parametros)

    # Las funciones pueden ser 4 tipos
    # 1.Funcion que no recibe parametros y no regresa valor
    # 2.Funcion que no recibe parametros y regresa valor
    # 3.Funcion que recibe parametros y no regresa valor
    # 4.Funcion que recibe parametros y regresa valor

#""""

#Ejemplo 1 Crear una funcion para imprimir nombres de personas

# 1.Funcion que no recibe parametros y no regresa valor
def solicitarnombres():
    nombre=input("Ingresa el nombre completo: ")

    solicitarnombres()

#Ejemplo 2 sumar dos numeros
    def suma():
        n1=int(input("Numero #1: "))
        n2=int(input("Numero #2: "))
        suma=n1+n2
        print(f"{n1}+{n2}={suma}")

suma()

#Ejemplo 3 sumar dos numeros
#2. Funcion que no recibe parametros y regresa valor
 def suma():
        n1=int(input("Numero #1: "))
        n2=int(input("Numero #2: "))
        suma=n1+n2
        resultado="{n1}+{n2}={suma}"
        return suma

resultado_suma=suma()
print(f"la suma es: {suma}")

#Ejemplo 4 sumar dos numeros
#3. Funcion que recibe parametros y no regresa valor
def suma(n1,n2):
    suma=n1+n2
    print(f"La suma es: {suma}")

n1=int(input("numero #1: "))
n2=int(input("numero #2: "))
suma(n1,n2)

#Ejemplo 5 sumar dos numeros
#4. Funcion que recibe parametros y  regresa valor
def suma(n1,n2):
    suma=n1+n2
    return suma

n1=int(input("numero #1: "))
n2=int(input("numero #2: "))
resultado_suma=suma(n1,n2)
print(f"La suma es:{resultado_suma}")

#Ejemplo 6 crear un programa que solicite a traves de una funcion la siguiente
#Informacion:nombre del px,edad,Estatura,tipo de sangre
#funcion que utilice los 4 funciones