reprobado=0
aprobado=0
for contador in range(1,16):

     calif=float(input(f"Ingrese la calificación del alumno {contador} (ej. 100): "))
     
     if calif<=79:
        reprobado+=1
     if calif>=80:
        aprobado+=1

print(f"{aprobado} aprobados en total")
print(f"{reprobado} reprobados en total")