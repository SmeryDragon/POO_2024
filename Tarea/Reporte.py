# Clase base Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo):
        self._marca = marca
        self._modelo = modelo
    
    def descripcion(self):
        return f"{self._marca} {self._modelo}"
    
    def tipo(self):
        return "Vehiculo"

# Clase derivada Coche
class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self._puertas = puertas

    def descripcion(self):
        return f"{super().descripcion()}, {self._puertas} puertas"

    def tipo(self):
        return "Coche"

# Clase derivada Motocicleta
class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)
        self._cilindrada = cilindrada

    def descripcion(self):
        return f"{super().descripcion()}, {self._cilindrada} cc"

    def tipo(self):
        return "Motocicleta"

# Ejecución y salida
vehiculos = [
    Coche("Toyota", "Corolla", 4),
    Motocicleta("Yamaha", "MT-07", 689),
    Coche("Honda", "Civic", 4),
    Motocicleta("Kawasaki", "Ninja", 998)
]

for vehiculo in vehiculos:
    print(f"Tipo: {vehiculo.tipo()}, Descripción: {vehiculo.descripcion()}")
