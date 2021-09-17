from os import startfile, system

class Maquina:
    def __init__(self,nombre): 
        self.nombre = nombre

    def elaboracionMaquina(self):
        actual = self.nombre.productos.cabeza
        while actual != None:
            print(str(actual.dato["elaboracion"]))
            actual = actual.siguiente
    
    def generarGraphviz(self):
        actual = self.nombre.productos.cabeza
        contador=0
        if actual != None:
            graphviz='''
            digraph L{
    node[shape=box fillcolor="#FFEDBB" style=filled]
    
    subgraph cluster_p{
        label="Elaboracion"
        bgcolor="#398D9C"
        raiz[label='''+str(actual.dato["elaboracion"])+''']
        edge[dir="both"]
            '''
            actual = actual.siguiente
        
        while actual!=None:
            contador+=1
            graphviz+='''
        Columna'''+str(contador)+'''[label='''+str(actual.dato["elaboracion"])+''',group='''+str(contador)+''',fillcolor=yellow];

        '''
            actual = actual.siguiente

        for co in range(1,contador):
            graphviz+='''
            Columna'''+str(co)+'''->Columna'''+str(co+1)+'''
            '''

        graphviz+='''
        raiz->Columna1
        {rank=same;raiz;'''
        
        for a in range(1,contador+1):
            graphviz+='''
            Columna'''+str(a)+''';'''
            
        graphviz+='''}
    }
}
            '''

        miArchivo=open('graphviz.dot','w')
        miArchivo.write(graphviz)
        miArchivo.close()
        
        system('dot -Tpng graphviz.dot -o graphviz.png')
        system('cd ./graphviz.png')
