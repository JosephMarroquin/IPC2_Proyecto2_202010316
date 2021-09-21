from listaLP import ListaNoOrdenadaLP
class ListaLineaProduccion:
    def __init__(self, numero):
        self.numero = numero
        self.lineaproduccion = ListaNoOrdenadaLP()
    
    def agregarDatosLP(self, componenetes):
        self.lineaproduccion.agregar(componenetes)
    

