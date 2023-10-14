from modelo.libro import Libro
from modelo.carro_compra import CarroCompras
from modelo.libro_existente_error import LibroExistenteError
from modelo.libro_agotado_error import LibroAgotadoError
from modelo.existencias_insuficientes_error import ExistenciasInsuficientesError

class TiendaLibros:

     def __init__(self):
        self.catalogo = {}
        self.carrito = CarroCompras()

    

     def adicionar_libro_a_catalogo(self, isbn: str, titulo: str, precio: float, existencias: int) -> Libro():
        if isbn in self.catalogo:
            raise LibroExistenteError()
        libro = Libro(isbn, titulo, precio, existencias)
        self.catalogo[isbn] = libro
        return libro


     pass
    # Defina metodo inicializador __init__

    # Defina metodo adicionar_libro_a_catalogo

    # Defina metodo agregar_libro_a_carrito

    # Defina metodo retirar_item_de_carrito
