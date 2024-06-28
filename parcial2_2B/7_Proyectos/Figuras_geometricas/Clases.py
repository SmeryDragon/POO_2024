class Usuario():
    def _init_(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        
    def info_usuario(self):
        return f'Mostrando info'
    
    def getNombre(self):
        return self.nombre
    def setNombre(self,nombre):
        self.nombre = nombre
        
    def getDireccion(self):
        return self.direccion
    def setDireccion(self, direccion):
        self.direccion = direccion
        
    def getTelefono(self):
        return self.telefono
    def setTelefono(self, telefono):
        self.telefono = telefono

class Cliente(Usuario):
    def _init_(self, nombre, direccion, telefono, num_cliente):
        super()._init_(nombre, direccion, telefono)
        self.num_cliente = num_cliente
        
    def info_usuario(self):
        print(f'\tCliente\nNombre: {self.getNombre()}\nDireccion{self.getDireccion()}\nTelefono: {self.getTelefono()}\nNumero de Cliente: {self.getNumCliente()}')
        
    def getNombre(self):
        return self.nombre
    def setNombre(self,nombre):
        self.nombre = nombre
        
    def getDireccion(self):
        return self.direccion
    def setDireccion(self, direccion):
        self.direccion = direccion
        
    def getTelefono(self):
        return self.telefono
    def setTelefono(self, telefono):
        self.telefono = telefono
        
    def getNumCliente(self):
        return self.num_cliente
    def setNumCliente(self, num_cliente):
        self.num_cliente = num_cliente
        
class Empleado(Usuario):
    def _init_(self, nombre, direccion, telefono, salario, num_empleado, tipo):
        super()._init_(nombre, direccion, telefono)
        self.salario = salario
        self.num_empleado = num_empleado
        self.tipo = tipo
     
    def info_usuario(self):
        print(f'\tEmpleado\nNombre: {self.getNombre()}\nDireccion{self.getDireccion()}\nTelefono: {self.getTelefono()}\nSalario: {self.getSalario()}\nNumero de Cliente: {self.getNumEmpleado()}\nTipo: {self.getTipo()}')
          
    def getNombre(self):
        return self.nombre
    def setNombre(self,nombre):
        self.nombre = nombre
        
    def getDireccion(self):
        return self.direccion
    def setDireccion(self, direccion):
        self.direccion = direccion
        
    def getTelefono(self):
        return self.telefono
    def setTelefono(self, telefono):
        self.telefono = telefono
        
    def getSalario(self):
        return self.salario
    def setSalario(self,salario):
        self.salario = salario
        
    def getNumEmpleado(self):
        return self.num_empleado
    def setNumEmpleado(self, num_empleado):
        self.num_empleado = num_empleado
        
    def getTipo(self):
        return self.tipo
    def setTipo(self,tipo):
        self.tipo = tipo