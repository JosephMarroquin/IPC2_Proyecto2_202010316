
def mostrarLista(lista): 
    actual = lista.cabeza
    index = 1
    while actual != None:
        print(actual.dato.nombre)
        index += 1
        actual = actual.siguiente

def buscarNodo(lista, nombre):
    actual = lista.cabeza
    while actual != None:
        if actual.dato.nombre == nombre:
            return actual.dato
        actual = actual.siguiente

#Lineas de produccion


def mostrarListaLP(lista): 
    actual = lista.cabeza
    index = 1
    while actual != None:
        print(actual.dato.numero)
        index += 1
        actual = actual.siguiente

def mostrarListaLE(lista): 
    actual = lista.cabeza
    index = 1
    while actual != None:
        print(actual.dato.numero)
        index += 1
        actual = actual.siguiente

