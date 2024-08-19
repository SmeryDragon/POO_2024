import mysql.connector

class Vehiculo:
    def __init__(self, id, marca, modelo, year):
        self._id = id
        self._marca = marca
        self._modelo = modelo
        self._year = year

    def detalles(self):
        return f"ID: {self._id}, Marca: {self._marca}, Modelo: {self._modelo}, Año: {self._year}"

class Coche(Vehiculo):
    def __init__(self, id, marca, modelo, year, puertas, combustible):
        super().__init__(id, marca, modelo, year)
        self._puertas = puertas
        self._combustible = combustible

    def detalles(self):
        return (super().detalles() + f", Puertas: {self._puertas}, Combustible: {self._combustible}")

class Motocicleta(Vehiculo):
    def __init__(self, id, marca, modelo, year, cilindrada, tipo):
        super().__init__(id, marca, modelo, year)
        self._cilindrada = cilindrada
        self._tipo = tipo

    def detalles(self):
        return (super().detalles() + f", Cilindrada: {self._cilindrada} cc, Tipo: {self._tipo}")

class Cliente:
    def __init__(self, id, nombre, email):
        self._id = id
        self._nombre = nombre
        self._email = email
        self._vehiculos = []

    def registrar_vehiculo(self, vehiculo):
        self._vehiculos.append(vehiculo)

    def mostrar_vehiculos(self):
        return [v.detalles() for v in self._vehiculos]

class Servicio:
    def __init__(self, id, nombre, descripcion):
        self._id = id
        self._nombre = nombre
        self._descripcion = descripcion

    def realizar_servicio(self, vehiculo):
        print(f"Realizando servicio: {self._nombre} en {vehiculo.detalles()}")

def conectar_bd():
    return mysql.connector.connect(
        host="localhost",         
        user="root",          
        password="",       
        database="veterinaria"    
    )

def insertar_vehiculo(con, vehiculo):
    cursor = con.cursor()
    if isinstance(vehiculo, Coche):
        tipo = 'Coche'
    elif isinstance(vehiculo, Motocicleta):
        tipo = 'Motocicleta'
    else:
        tipo = 'Desconocido'

    query = ("INSERT INTO vehiculos (id, marca, modelo, year, tipo, detalles) "
             "VALUES (%s, %s, %s, %s, %s, %s)")
    data = (vehiculo._id, vehiculo._marca, vehiculo._modelo, vehiculo._year, tipo, vehiculo.detalles())
    cursor.execute(query, data)
    con.commit()
    cursor.close()

def obtener_vehiculos_cliente(con, cliente_id):
    cursor = con.cursor()
    query = "SELECT * FROM vehiculos WHERE cliente_id = %s"
    cursor.execute(query, (cliente_id,))
    vehiculos = cursor.fetchall()
    cursor.close()
    return vehiculos

def actualizar_vehiculo(con, vehiculo):
    cursor = con.cursor()
    query = ("UPDATE vehiculos SET marca = %s, modelo = %s, year = %s, tipo = %s, detalles = %s "
             "WHERE id = %s")
    data = (vehiculo._marca, vehiculo._modelo, vehiculo._year, vehiculo.tipo, vehiculo.detalles(), vehiculo._id)
    cursor.execute(query, data)
    con.commit()
    cursor.close()

def eliminar_vehiculo(con, vehiculo_id):
    cursor = con.cursor()
    query = "DELETE FROM vehiculos WHERE id = %s"
    cursor.execute(query, (vehiculo_id,))
    con.commit()
    cursor.close()

def mostrar_menu():
    print("1. Registrar nuevo vehículo")
    print("2. Ver vehículos de un cliente")
    print("3. Actualizar un vehículo")
    print("4. Eliminar un vehículo")
    print("5. Salir")

def main():
    try:
        con = conectar_bd()
        print("Conexión exitosa a la base de datos.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            tipo = input("Tipo de vehículo (Coche/Motocicleta): ")
            id = int(input("ID: "))
            marca = input("Marca: ")
            modelo = input("Modelo: ")
            year = int(input("Año: "))

            if tipo.lower() == "coche":
                puertas = int(input("Puertas: "))
                combustible = input("Combustible: ")
                vehiculo = Coche(id, marca, modelo, year, puertas, combustible)
            elif tipo.lower() == "motocicleta":
                cilindrada = int(input("Cilindrada (cc): "))
                tipo_moto = input("Tipo (Deportiva/Cruiser/etc.): ")
                vehiculo = Motocicleta(id, marca, modelo, year, cilindrada, tipo_moto)
            else:
                print("Tipo de vehículo no válido.")
                continue

            insertar_vehiculo(con, vehiculo)
            print("Vehículo registrado exitosamente.")

        elif opcion == "2":
            cliente_id = int(input("ID del cliente: "))
            vehiculos = obtener_vehiculos_cliente(con, cliente_id)
            for vehiculo in vehiculos:
                print(vehiculo)

        elif opcion == "3":
            id = int(input("ID del vehículo a actualizar: "))
            marca = input("Nueva Marca: ")
            modelo = input("Nuevo Modelo: ")
            year = int(input("Nuevo Año: "))
            tipo = input("Nuevo Tipo (Coche/Motocicleta): ")

            if tipo.lower() == "coche":
                puertas = int(input("Puertas: "))
                combustible = input("Combustible: ")
                vehiculo = Coche(id, marca, modelo, year, puertas, combustible)
            elif tipo.lower() == "motocicleta":
                cilindrada = int(input("Cilindrada (cc): "))
                tipo_moto = input("Tipo (Deportiva/Cruiser/etc.): ")
                vehiculo = Motocicleta(id, marca, modelo, year, cilindrada, tipo_moto)
            else:
                print("Tipo de vehículo no válido.")
                continue

            actualizar_vehiculo(con, vehiculo)
            print("Vehículo actualizado exitosamente.")

        elif opcion == "4":
            vehiculo_id = int(input("ID del vehículo a eliminar: "))
            eliminar_vehiculo(con, vehiculo_id)
            print("Vehículo eliminado exitosamente.")

        elif opcion == "5":
            print("Saliendo del sistema.")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")

    con.close()

if __name__ == "__main__":
    main()
