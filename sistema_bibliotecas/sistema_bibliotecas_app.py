from sistema_bibliotecas.biblioteca import Biblioteca
from sistema_bibliotecas.libro import Libro

bibliotecaNacional = Biblioteca('Biblioteca Nacional')
print(f'*** Bienvenidos a la {bibliotecaNacional.nombre}')

# Definicion de Libros
libro1 = Libro('El amor en los tiempos del colera', 'Gabriel Garcia Marquez', 'Ficcion')
libro2 = Libro('Cien años de soledad', 'Gabriel Garcia Marquez', 'Ficcion')
libro3 = Libro('Don Quijote', 'Miguel de Cervantes', 'Comedia')
libro4 = Libro('Pedro Paramo', 'Juan Rulfo', 'Ficcion')
libro5 = Libro('Pantaleon y los visitadores', 'Mario Vargas Llosa', 'Comedia')

# Agregar los libros a la biblioteca
bibliotecaNacional.agregar_libro(libro1)
bibliotecaNacional.agregar_libro(libro2)
bibliotecaNacional.agregar_libro(libro3)
bibliotecaNacional.agregar_libro(libro4)
bibliotecaNacional.agregar_libro(libro5)

# Buscar libros por autor
autor = 'Gabriel Garcia Marquez'
print(f'\nLibros de {autor}')
bibliotecaNacional.buscar_libros_por_autor(autor)

# Buscar libros por generos
genero = 'Ficcion'
print(f'\n Libros de {genero}')
bibliotecaNacional.buscar_libros_por_genero(genero)

# Mostrar todos los libros
bibliotecaNacional.mostrar_todos_los_libros()