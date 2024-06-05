#REGEX
#^Inicio de una cadena
#$fin de la cadena
#[u conjunto de caracteres]
#\ escape de caracter para tratarlo como literal

#1.Buscar un patron en una cadena
# import re

# texto= "Hola,mi numero de telefono es 123-456-7890"
# patron=r"\d{4}-\d{3}-\d{4}"

# resultado= re.search(patron, texto)
# if resultado:
#     print(f"encontrado: {resultado.group()}")
# else:
#     print("No encontrado")

#2.Encontrar todas las ocurrencias de un patron
import re
texto= "Hay varias fechas: 2021-01-01, 2022-02-02, 2023-03-03"
patron=r"\d{4}-\d{2}-\d{2}"

resultados= re.findall(patron, texto)
print(f"Fechas encontradas:{resultados}")