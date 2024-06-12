# Crear un script que tenga 4 variables, una lista, una cadena, un entero y un logico,  
#   y que imprima un mensaje de acuerdo al tipo de dato de cada variable. Usar funciones

def imprimir_tipo(variable):
    if isinstance(variable, list):
        print("La variable es una lista.")
    elif isinstance(variable, str):
        print("La variable es una cadena de texto.")
    elif isinstance(variable, int):
        print("La variable es un entero.")
    elif isinstance(variable, bool):
        print("La variable es un valor lógico.")
    else:
        print("No se reconoce el tipo de dato de la variable.")

def main():
    mi_lista = [1, 2, 3]
    mi_cadena = "Hola mundo"
    mi_entero = 42
    mi_logico = True
    
    imprimir_tipo(mi_lista)
    imprimir_tipo(mi_cadena)
    imprimir_tipo(mi_entero)
    imprimir_tipo(mi_logico)

if __name__ == "__main__":
    main()
