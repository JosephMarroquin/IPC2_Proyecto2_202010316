
def mostrarLista(lista): #metodo para mostrar cada terreno en la lista enlazada
    actual = lista.cabeza
    index = 1
    while actual != None:
        print(actual.dato.nombre)
        index += 1
        actual = actual.siguiente

def buscarNodo(lista, nombre): #metedo para devolver el objeto terreno encontrado en una lista enlazada
    actual = lista.cabeza
    while actual != None:
        if actual.dato.nombre == nombre:
            return actual.dato
        actual = actual.siguiente

