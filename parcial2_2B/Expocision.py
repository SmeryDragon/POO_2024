#Clases

class Animal:
    def __init__(self, nombre , especie):
        self.nombre= nombre
        self.especie=especie

#Metodos
def hacer_sonido(self):
    print(f"{self.nombre} hace un sonido")

#Objetos
mi_perro=Animal ("Firulais", "Perro")

#Encapsulamiento
class Animal:
    def __init__(self, nombre , especie):
        self.nombre= nombre
        self.especie=especie #atributo privado

    def obtener_especie(self):
        return self.__especie #metodo para acceder a nuestro atributo privado
    

#Herencia
class Perro(Animal):
    def __init__(self,nombre,raza):
        super().__init__(nombre, "Perro")
        self.raza=raza

#Polimorfismo
class gato(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} maulla")

def hacer_sonido_animal(animal):
    animal.hacer_sonido()

mi_perro=Perro ("Firulais" , "labrador")
mi_gato=gato ("Misu")

hacer_sonido_animal(mi_perro)
hacer_sonido_animal(mi_gato)

#Manejo de excepciones
try:
    resultado=10/0
except ZeroDivisionError as e:
    print("Error:Division por cero")
else:
    print("La division se realizo correctamente")
finally:
    print("Operacion Finalizada")