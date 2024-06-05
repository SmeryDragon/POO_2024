# peliculas.py

peliculas = []

def agregar_pelicula(nombre):
    """Agrega una película a la lista."""
    peliculas.append(nombre)
    print(f'La película "{nombre}" ha sido agregada.')

def remover_pelicula(nombre):
    """Remueve una película de la lista."""
    if nombre in peliculas:
        peliculas.remove(nombre)
        print(f'La película "{nombre}" ha sido removida.')
    else:
        print(f'La película "{nombre}" no se encuentra en la lista.')

def consultar_peliculas():
    """Muestra todas las películas en la lista."""
    if peliculas:
        print("Lista de películas:")
        for pelicula in peliculas:
            print(f'- {pelicula}')
    else:
        print("No hay películas en la lista.")
