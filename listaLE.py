from nodoLE import NodoLE

class ListaNoOrdenadaLE:

    def __init__(self):      
        self.cabeza = None

    def agregar(self,item):
        if not self.cabeza:
            self.cabeza=NodoLE(item)
            return True
        else:
            current=self.cabeza
            while current.siguiente:
                current=current.siguiente
            current.siguiente=NodoLE(item)
            return True   

    def buscar(self,item):     
        actual = self.cabeza    
        encontrado = False     
        while actual != None and not encontrado:  
            if actual.obtenerDato() == item:     
                encontrado = True                 
            else:
                actual = actual.obtenerSiguiente() 
        return encontrado    

