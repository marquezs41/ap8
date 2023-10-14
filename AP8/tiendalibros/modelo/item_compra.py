from modelo.libro import Libro

class ItemCompra:
    def __init__(self, libro, cantidad):
        self.libro : str = libro
        self.cantidad : int = cantidad

    def calcular_subtotal(self):
        return self.cantidad * self.libro.precio

        
    pass
 