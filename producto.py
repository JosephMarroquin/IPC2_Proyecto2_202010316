from lista import ListaNoOrdenada
class ListaProducto:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = ListaNoOrdenada()
    
    def agregaMatriz(self, elabo):
        self.productos.agregar({"elaboracion":elabo})
    




