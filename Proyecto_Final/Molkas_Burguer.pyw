import tkinter as tk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
from datetime import datetime

def conectar():
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='molkas_burguer'
        )
        if conexion.is_connected():
            return conexion
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def cerrar_conexion(conexion):
    if conexion.is_connected():
        conexion.close()

class MolkasBurguer:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.empleados = []
        self.productos = []
        self.pedidos = []

class Empleado:
    def __init__(self, id_empleado, nombre, puesto, salario):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.puesto = puesto
        self.salario = salario

class Cliente:
    def __init__(self, id_cliente, nombre, telefono, email):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

class Producto:
    def __init__(self, id_producto, nombre, descripcion, precio, stock):
        self.id_producto = id_producto
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
    
    def actualizar_stock(self, cantidad):
        if self.stock >= cantidad:
            self.stock -= cantidad
        else:
            print("Stock insuficiente")

class Pedido:
    def __init__(self, id_pedido, cliente, empleado, fecha):
        self.id_pedido = id_pedido
        self.cliente = cliente
        self.empleado = empleado
        self.detalles = []
        self.fecha = fecha

    def calcular_total(self):
        total = sum(detalle.cantidad * detalle.producto.precio for detalle in self.detalles)
        return total

class DetallePedido:
    def __init__(self, pedido, producto, cantidad):
        self.pedido = pedido
        self.producto = producto
        self.cantidad = cantidad

class MolkasBurguerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Molkas Burguer")
        self.root.geometry("800x600")
        self.root.configure(bg="#f7f7f7")

        # Conectar a la base de datos
        self.conexion = conectar()

        # Título principal
        title = tk.Label(root, text="Molkas Burguer", font=("Helvetica", 16, "bold"), bg="#ff5733", fg="white")
        title.pack(fill=tk.X, pady=10)

        # Frame para los botones
        button_frame = tk.Frame(root, bg="#f7f7f7")
        button_frame.pack(pady=20)

        # Botones
        add_order_button = tk.Button(button_frame, text="Añadir Pedido", font=("Helvetica", 12), bg="#ff5733", fg="white", relief=tk.RAISED, command=self.add_order_window)
        add_order_button.pack(side=tk.LEFT, pady=5, padx=10)

        show_products_button = tk.Button(button_frame, text="Mostrar Productos", font=("Helvetica", 12), bg="#ff5733", fg="white", relief=tk.RAISED, command=self.show_products)
        show_products_button.pack(side=tk.LEFT, pady=5, padx=10)

        add_employee_button = tk.Button(button_frame, text="Agregar Empleado", font=("Helvetica", 12), bg="#ff5733", fg="white", relief=tk.RAISED, command=self.add_employee_window)
        add_employee_button.pack(side=tk.LEFT, pady=5, padx=10)

        delete_employee_button = tk.Button(button_frame, text="Eliminar Empleado", font=("Helvetica", 12), bg="#ff5733", fg="white", relief=tk.RAISED, command=self.delete_employee_window)
        delete_employee_button.pack(side=tk.LEFT, pady=5, padx=10)

        add_product_button = tk.Button(button_frame, text="Agregar Producto", font=("Helvetica", 12), bg="#ff5733", fg="white", relief=tk.RAISED, command=self.add_product_window)
        add_product_button.pack(side=tk.LEFT, pady=5, padx=10)

        delete_product_button = tk.Button(button_frame, text="Eliminar Producto", font=("Helvetica", 12), bg="#ff5733", fg="white", relief=tk.RAISED, command=self.delete_product_window)
        delete_product_button.pack(side=tk.LEFT, pady=5, padx=10)

        add_client_button = tk.Button(button_frame, text="Agregar Cliente", font=("Helvetica", 12), bg="#ff5733", fg="white", relief=tk.RAISED, command=self.add_client_window)
        add_client_button.pack(side=tk.LEFT, pady=5, padx=10)

        delete_client_button = tk.Button(button_frame, text="Eliminar Cliente", font=("Helvetica", 12), bg="#ff5733", fg="white", relief=tk.RAISED, command=self.delete_client_window)
        delete_client_button.pack(side=tk.LEFT, pady=5, padx=10)

    def add_order_window(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Añadir Pedido")
        add_window.geometry("400x400")

        tk.Label(add_window, text="Nombre del Cliente:").pack(pady=5)
        nombre_cliente_entry = tk.Entry(add_window)
        nombre_cliente_entry.pack(pady=5)

        tk.Label(add_window, text="Nombre del Empleado:").pack(pady=5)
        nombre_empleado_entry = tk.Entry(add_window)
        nombre_empleado_entry.pack(pady=5)

        tk.Label(add_window, text="Fecha (YYYY-MM-DD):").pack(pady=5)
        fecha_entry = tk.Entry(add_window)
        fecha_entry.pack(pady=5)

        tk.Label(add_window, text="Producto:").pack(pady=5)
        producto_entry = tk.Entry(add_window)
        producto_entry.pack(pady=5)

        tk.Label(add_window, text="Cantidad:").pack(pady=5)
        cantidad_entry = tk.Entry(add_window)
        cantidad_entry.pack(pady=5)

        def save_order():
            nombre_cliente = nombre_cliente_entry.get()
            nombre_empleado = nombre_empleado_entry.get()
            fecha = datetime.now().strftime('%Y-%m-%d')
            producto = producto_entry.get()
            cantidad = cantidad_entry.get()

            if not (nombre_cliente and nombre_empleado and fecha and producto and cantidad):
                messagebox.showerror("Error", "Por favor complete todos los campos.")
                return

            try:
                cantidad = int(cantidad)
                fecha = datetime.now().strftime('%Y-%m-%d')

                cursor = self.conexion.cursor()

                # Buscar cliente por nombre
                cursor.execute("SELECT ID_Cliente FROM Cliente WHERE Nombre = %s", (nombre_cliente,))
                cliente_id = cursor.fetchone()
                if not cliente_id:
                    messagebox.showerror("Error", "Cliente no encontrado.")
                    return
                cliente_id = cliente_id[0]

                # Buscar empleado por nombre
                cursor.execute("SELECT ID_Empleado FROM Empleado WHERE Nombre = %s", (nombre_empleado,))
                empleado_id = cursor.fetchone()
                if not empleado_id:
                    messagebox.showerror("Error", "Empleado no encontrado.")
                    return
                empleado_id = empleado_id[0]

                # Buscar producto por nombre
                cursor.execute("SELECT ID_Producto, Precio, Stock FROM Producto WHERE Nombre = %s", (producto,))
                producto_data = cursor.fetchone()
                if not producto_data:
                    messagebox.showerror("Error", "Producto no encontrado.")
                    return
                producto_id, precio, stock = producto_data

                if stock < cantidad:
                    messagebox.showerror("Error", "Stock insuficiente.")
                    return

                # Insertar pedido
                cursor.execute("INSERT INTO Pedido (ID_Cliente, ID_Empleado, Fecha) VALUES (%s, %s, %s)", (cliente_id, empleado_id, fecha))
                pedido_id = cursor.lastrowid

                # Insertar detalle de pedido
                cursor.execute("INSERT INTO Detalle_Pedido (ID_Pedido, ID_Producto, Cantidad) VALUES (%s, %s, %s)", (pedido_id, producto_id, cantidad))
                self.conexion.commit()

                # Actualizar stock
                cursor.execute("UPDATE Producto SET Stock = Stock - %s WHERE ID_Producto = %s", (cantidad, producto_id))
                self.conexion.commit()

                messagebox.showinfo("Éxito", "Pedido agregado correctamente.")
                add_window.destroy()
            except ValueError:
                messagebox.showerror("Error", "Cantidad debe ser un número entero.")
            except Error as e:
                messagebox.showerror("Error", f"Error al agregar pedido: {e}")

        tk.Button(add_window, text="Guardar Pedido", command=save_order).pack(pady=20)

    def show_products(self):
        show_window = tk.Toplevel(self.root)
        show_window.title("Productos")
        show_window.geometry("600x400")

        cursor = self.conexion.cursor()
        cursor.execute("SELECT * FROM Producto")
        productos = cursor.fetchall()

        if productos:
            for producto in productos:
                tk.Label(show_window, text=f"ID: {producto[0]}, Nombre: {producto[1]}, Descripción: {producto[2]}, Precio: {producto[3]}, Stock: {producto[4]}").pack(pady=5)
        else:
            tk.Label(show_window, text="No hay productos disponibles.").pack(pady=5)

    def add_employee_window(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Agregar Empleado")
        add_window.geometry("300x200")

        tk.Label(add_window, text="Nombre:").pack(pady=5)
        nombre_entry = tk.Entry(add_window)
        nombre_entry.pack(pady=5)

        tk.Label(add_window, text="Puesto:").pack(pady=5)
        puesto_entry = tk.Entry(add_window)
        puesto_entry.pack(pady=5)

        tk.Label(add_window, text="Salario:").pack(pady=5)
        salario_entry = tk.Entry(add_window)
        salario_entry.pack(pady=5)

        def save_employee():
            nombre = nombre_entry.get()
            puesto = puesto_entry.get()
            salario = salario_entry.get()

            if not (nombre and puesto and salario):
                messagebox.showerror("Error", "Por favor complete todos los campos.")
                return

            try:
                salario = float(salario)
                cursor = self.conexion.cursor()
                cursor.execute("INSERT INTO Empleado (Nombre, Puesto, Salario) VALUES (%s, %s, %s)", (nombre, puesto, salario))
                self.conexion.commit()
                messagebox.showinfo("Éxito", "Empleado agregado correctamente.")
                add_window.destroy()
            except ValueError:
                messagebox.showerror("Error", "Salario debe ser un número.")
            except Error as e:
                messagebox.showerror("Error", f"Error al agregar empleado: {e}")

        tk.Button(add_window, text="Guardar", command=save_employee).pack(pady=20)

    def delete_employee_window(self):
        delete_window = tk.Toplevel(self.root)
        delete_window.title("Eliminar Empleado")
        delete_window.geometry("300x150")

        tk.Label(delete_window, text="Nombre del Empleado:").pack(pady=5)
        nombre_entry = tk.Entry(delete_window)
        nombre_entry.pack(pady=5)

        def delete_employee():
            nombre = nombre_entry.get()
            if not nombre:
                messagebox.showerror("Error", "Por favor ingrese el nombre del empleado.")
                return

            try:
                cursor = self.conexion.cursor()
                cursor.execute("DELETE FROM Empleado WHERE Nombre = %s", (nombre,))
                if cursor.rowcount == 0:
                    messagebox.showerror("Error", "Empleado no encontrado.")
                else:
                    self.conexion.commit()
                    messagebox.showinfo("Éxito", "Empleado eliminado correctamente.")
            except Error as e:
                messagebox.showerror("Error", f"Error al eliminar empleado: {e}")

        tk.Button(delete_window, text="Eliminar Empleado", command=delete_employee).pack(pady=20)

    def add_product_window(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Agregar Producto")
        add_window.geometry("300x250")

        tk.Label(add_window, text="Nombre:").pack(pady=5)
        nombre_entry = tk.Entry(add_window)
        nombre_entry.pack(pady=5)

        tk.Label(add_window, text="Descripción:").pack(pady=5)
        descripcion_entry = tk.Entry(add_window)
        descripcion_entry.pack(pady=5)

        tk.Label(add_window, text="Precio:").pack(pady=5)
        precio_entry = tk.Entry(add_window)
        precio_entry.pack(pady=5)

        tk.Label(add_window, text="Stock:").pack(pady=5)
        stock_entry = tk.Entry(add_window)
        stock_entry.pack(pady=5)

        def save_product():
            nombre = nombre_entry.get()
            descripcion = descripcion_entry.get()
            precio = precio_entry.get()
            stock = stock_entry.get()

            if not (nombre and descripcion and precio and stock):
                messagebox.showerror("Error", "Por favor complete todos los campos.")
                return

            try:
                precio = float(precio)
                stock = int(stock)
                cursor = self.conexion.cursor()
                cursor.execute("INSERT INTO Producto (Nombre, Descripcion, Precio, Stock) VALUES (%s, %s, %s, %s)", (nombre, descripcion, precio, stock))
                self.conexion.commit()
                messagebox.showinfo("Éxito", "Producto agregado correctamente.")
                add_window.destroy()
            except ValueError:
                messagebox.showerror("Error", "Precio y Stock deben ser numéricos.")
            except Error as e:
                messagebox.showerror("Error", f"Error al agregar producto: {e}")

        tk.Button(add_window, text="Guardar", command=save_product).pack(pady=20)

    def delete_product_window(self):
        delete_window = tk.Toplevel(self.root)
        delete_window.title("Eliminar Producto")
        delete_window.geometry("300x150")

        tk.Label(delete_window, text="Nombre del Producto:").pack(pady=5)
        nombre_entry = tk.Entry(delete_window)
        nombre_entry.pack(pady=5)

        def delete_product():
            nombre = nombre_entry.get()
            if not nombre:
                messagebox.showerror("Error", "Por favor ingrese el nombre del producto.")
                return

            try:
                cursor = self.conexion.cursor()
                cursor.execute("DELETE FROM Producto WHERE Nombre = %s", (nombre,))
                if cursor.rowcount == 0:
                    messagebox.showerror("Error", "Producto no encontrado.")
                else:
                    self.conexion.commit()
                    messagebox.showinfo("Éxito", "Producto eliminado correctamente.")
            except Error as e:
                messagebox.showerror("Error", f"Error al eliminar producto: {e}")

        tk.Button(delete_window, text="Eliminar Producto", command=delete_product).pack(pady=20)

    def add_client_window(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Agregar Cliente")
        add_window.geometry("300x200")

        tk.Label(add_window, text="Nombre:").pack(pady=5)
        nombre_entry = tk.Entry(add_window)
        nombre_entry.pack(pady=5)

        tk.Label(add_window, text="Teléfono:").pack(pady=5)
        telefono_entry = tk.Entry(add_window)
        telefono_entry.pack(pady=5)

        tk.Label(add_window, text="Email:").pack(pady=5)
        email_entry = tk.Entry(add_window)
        email_entry.pack(pady=5)

        def save_client():
            nombre = nombre_entry.get()
            telefono = telefono_entry.get()
            email = email_entry.get()

            if not (nombre and telefono and email):
                messagebox.showerror("Error", "Por favor complete todos los campos.")
                return

            try:
                cursor = self.conexion.cursor()
                cursor.execute("INSERT INTO Cliente (Nombre, Telefono, Email) VALUES (%s, %s, %s)", (nombre, telefono, email))
                self.conexion.commit()
                messagebox.showinfo("Éxito", "Cliente agregado correctamente.")
                add_window.destroy()
            except Error as e:
                messagebox.showerror("Error", f"Error al agregar cliente: {e}")

        tk.Button(add_window, text="Guardar", command=save_client).pack(pady=20)

    def delete_client_window(self):
        delete_window = tk.Toplevel(self.root)
        delete_window.title("Eliminar Cliente")
        delete_window.geometry("300x150")

        tk.Label(delete_window, text="Nombre del Cliente:").pack(pady=5)
        nombre_entry = tk.Entry(delete_window)
        nombre_entry.pack(pady=5)

        def delete_client():
            nombre = nombre_entry.get()
            if not nombre:
                messagebox.showerror("Error", "Por favor ingrese el nombre del cliente.")
                return

            try:
                cursor = self.conexion.cursor()
                cursor.execute("DELETE FROM Cliente WHERE Nombre = %s", (nombre,))
                if cursor.rowcount == 0:
                    messagebox.showerror("Error", "Cliente no encontrado.")
                else:
                    self.conexion.commit()
                    messagebox.showinfo("Éxito", "Cliente eliminado correctamente.")
            except Error as e:
                messagebox.showerror("Error", f"Error al eliminar cliente: {e}")

        tk.Button(delete_window, text="Eliminar Cliente", command=delete_client).pack(pady=20)

root = tk.Tk()
app = MolkasBurguerApp(root)
root.mainloop()
