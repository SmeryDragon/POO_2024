import mysql.connector

try:
#Conectar con la BD MySQL
    conexion=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='bd_python'
)

except Exception as e:
    # print(f"Error"{e})
    # print(f"Tipo de error:{type(e)}")
    print(f"ocurrio un problema con el servidor...por favor intentelo mas tarde")

else:
    print(f"Se creo ka conexion con la BD exitosamente")
#verificar la conexion a la BD
# if conexion.is_connected():
#     print(f"Se creo la conexion con la BD exitosamente")
# else:
#     print(f"No fue posible conectar con la BD ... verifique ...")    