from conexionBD import *

try:
   micursor=conexion.cursor()

   sql="update clientes set tel='6181112233' where id='4'"
   micursor.execute(sql)
   conexion.commit()

except:
      print(f"ocurrio un problema con el servidor...por favor intentelo mas tarde")   
else:
     print(f"Registro Insertado Correctamente")