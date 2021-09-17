from nodo import Nodo

class ListaNoOrdenada:

    def __init__(self):      
        self.cabeza = None

    def estaVacia(self):    
        return self.cabeza == None

    def agregar(self,item):    
        temp = Nodo(item)      
        temp.asignarSiguiente(self.cabeza) 
        self.cabeza = temp     

    def buscar(self,item):     
        actual = self.cabeza    
        encontrado = False     
        while actual != None and not encontrado:  
            if actual.obtenerDato() == item:     
                encontrado = True                 
            else:
                actual = actual.obtenerSiguiente() 
        return encontrado    

