from tiendalibros.modelo.libro_error import LibroError
from tiendalibros.modelo.libro import Libro


class LibroExistenteError(LibroError):

     def __init__(self):
        super().__init__()


     def __str__(self) -> str:
        return (f"El libro con titulo {Libro.titulo} y isbn: {Libro.isbn} ya existe en el catalogo")

     pass
    # Defina metodo inicializador

    # Defina metodo especial
