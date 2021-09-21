class NodoLE:
    def __init__(self,datoInicial):  
        self.dato = datoInicial     
        self.siguiente = None       

    def obtenerDato(self):        
        return self.dato

    def obtenerSiguiente(self):   
        return self.siguiente