#Formas de concatenar en python

nombre="Joshua Torres"
especialidad="Area de Sw Multiplataforma"
Carrera="Ingenieria en Gestion y desarrollo de SW"

#primer forma
print("Mi nombre es "+nombre+"estoy en la "+especialidad+" y estudio la carrera de "+Carrera)

print("\n")

#2da forma
print("Mi nombre es ",nombre," estoy en la especialidad de ",especialidad," y estudio la carrera de ",Carrera)

print("\n")


#3er dorma mas comun en Python
print(f"Mi nombre es , {nombre} , estoy en la especialidad de , {especialidad} , y estudio la carrera de , {Carrera}")

print("\n")


#4ta forma
print("mi nombre es ,{}, estoyen la especialidad de ,{}, y estudio la carrera de ,{}".format (nombre,especialidad,Carrera))


print("\n")

#5ta forma
print('Mi nombre es '+nombre+' estoy en la especialidad de '+especialidad+' y estudio la carrera de '+Carrera)

print("\n")