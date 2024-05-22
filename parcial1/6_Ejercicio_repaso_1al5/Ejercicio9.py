def main(): #punto de entrada
    while True: #Bucle infinito, se ejecutará hasta encontrar una....
        num=int(input("Introduce un número (000 si desea salir):  "))
        if num==000: #......instruccion para salir del bucle
            print("....Saliendo del programa...")
            break

if  "_main_":  #asegura quese ejecute solo si ejecutamos este archivo directamente 
    main()