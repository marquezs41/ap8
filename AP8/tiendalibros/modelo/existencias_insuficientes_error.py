from tiendalibros.modelo.libro_error import LibroError
from tiendalibros.modelo.libro import Libro

class ExistenciasInsuficientesError(LibroError):

     def __init__(self, cantidad_a_comprar: int):
        super().__init__()
        self.cantidad_a_comprar: int = cantidad_a_comprar

     def __str__(self) -> str:
        return (f"El libro con titulo {Libro.titulo} y isbn {Libro.isbn} no tiene suficientes existencias para realizar la compra: cantidad a comprar: {self.cantidad_a_comprar}, existencias: {Libro.existencias}")

     pass

    # Defina metodo inicializador

    # Defina metodo espcial
