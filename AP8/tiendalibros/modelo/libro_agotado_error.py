from tiendalibros.modelo.libro_error import LibroError


class LibroAgotadoError(LibroError):
    def __init__(self):
        super().__init__()

    def __str__(self) -> str:
        return (f"El libro con titulo {Libro.titulo} y isbn {Libro.isbn} esta agotado")

    

    # Defina metodo inicializador

    # Defina metodo especial
