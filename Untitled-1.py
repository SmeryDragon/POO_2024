print("Bienvenido al sistema de IMC")

repetir = True 
while repetir:
    peso = float(input("Ingrese su peso en kilogramos: "))
    altura = float(input("Ingrese su altura en metros: "))

    IMC = peso / (altura ** 2)

    print(f"Su Índice de Masa Corporal es {IMC:.2f}")

    if IMC < 18.5:
        print("Peso inferior al normal")
    elif 18.5 <= IMC < 24.9:
        print("Peso normal")
    elif 25.0 <= IMC < 29.9:
        print("Peso superior al normal")
    elif IMC >= 30:
        print("Obesidad")

    respuesta = input("¿Desea calcular el IMC nuevamente? (s/n): ")
    if respuesta.lower() != "s":
        repetir = False