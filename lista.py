from nodo import Nodo

class ListaNoOrdenada:

    def __init__(self):      
        self.cabeza = None
    
    def agregar(self,item):
        if not self.cabeza:
            self.cabeza=Nodo(item)
            return True
        else:
            current=self.cabeza
            while current.siguiente:
                current=current.siguiente
            current.siguiente=Nodo(item)
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

