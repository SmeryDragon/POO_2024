# opcion1=True
# while opcion1:
#     print("Calculadora basica")
#     print("Elige la opcion acerca de que operacion gustas hacer")
#     print("\n\t 1.Suma \ 2.Resta \ 3.Multiplicacion \ 4.Division \ 5 salir")
# opcion=input("\t Elige una opcion:").upper()

# if opcion=="1" or opcion=="+" or opcion =="SUMA":

#     n1=int(input("Numero #1: "))
#     n2=int(input("Numero #2 "))
#     suma=n1+n2
#     print(f"{n1}+{n2}={suma}")

# elif opcion=="2" or opcion=="-" or opcion =="RESTA":

#         n1=int(input("Numero #1: "))
#         n2=int(input("Numero #2 "))
#         RESTA=n1-n2
#         print(f"{n1}-{n2}={RESTA}")

# elif opcion=="3" or opcion=="*" or opcion =="MULTIPLICACION":

#     n1=int(input("Numero #1: "))
#     n2=int(input("Numero #2 "))
#     MULTIPLICACION=n1*n2
#     print(f"{n1}*{n2}={MULTIPLICACION}")

# elif opcion=="4" or opcion=="/" or opcion =="DIVISION":

#     n1=int(input("Numero #1: "))
#     n2=int(input("Numero #2 "))
#     DIVISION=n1/n2
#     print(f"{n1}/{n2}={DIVISION}")
# else:
#      print("Terminaste la ejecucion del SW")

#      opcion1=False

# def SolicitarNumeros():
#     n1=int(input("Numero #1: "))
#     n2=int(input("Numero #2: "))

def solicitarNumeros():
  global n1,n2  
  n1=int(input("Numero #1: "))
  n2=int(input("Numero #2: "))
  

def operacionAritmetica(num1,num2,opcion):  
    if opcion=="1" or opcion=="+" or opcion=="SUMA":
      return f"{n1}+{n2}={n1+n2}"
    elif opcion=="2" or opcion=="-" or opcion=="RESTA":
     return f"{n1}-{n2}={n1-n2}"
    elif opcion=="3" or opcion=="*" or opcion=="MULTIPLICACION":
     return f"{n1}*{n2}={n1*n2}"
    elif opcion=="4" or opcion=="/" or opcion=="DIVISION":
     return f"{n1}/{n2}={n1/n2}"  
    else: 
     opcion=False    
     return "Terminaste la ejecucion del SW"

    
opcion=True    
while opcion:
 print("\n\t..::: CALCULADORA BÁSICA :::... \n 1.- Suma \n 2.- Resta \n 3.- Multiplicacion \n 4.- División \n 5.- SALIR ")
 opcion=input("\t Elige una opción: ").upper()

if opcion:
 solicitarNumeros()
 print(operacionAritmetica(n1,n2,opcion))
 keyboard.add_hotkey('F5', clear_screen)
else:
 opcion=False    
 print("Terminaste la ejecucion del SW")