from conexionBD import *

micursor=conexion.cursor()

sql="select nombre,direccion,tel from clientes"
micursor.execute(sql)
resultado=micursor.fetchall()

if len(resultado)>0:
    print(f"Registros de la tabla: {len(resultado)}")
    for x in resultado:
      print(x)

except:
      print(f"ocurrio un problema con el servidor...por favor intentelo mas tarde")   
else:
     print(f"Registro Insertado Correctamente")
