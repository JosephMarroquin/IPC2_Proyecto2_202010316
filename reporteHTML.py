import re
import xml.etree.ElementTree as ET

class Reportehtml:

    def __init__(self,nombre): 
        self.nombre = nombre
    
    def repHtml(self,nombree,lista,lista2):

        reporte = ET.Element('SalidaSimulacion')
        ListadoProductos = ET.SubElement(reporte, 'ListadoProductos')
        Producto = ET.SubElement(ListadoProductos, 'Producto')
        Nom = ET.SubElement(Producto, 'Nombre')
        Nom.text=str(nombree)
        ElaboracionOptima = ET.SubElement(Producto, 'ElaboracionOptima')
        
        

        file=open("reporteHTML.html","w")
        cabecera="""
        <!DOCTYPE HTML PUBLIC"
    <html>
    <head>
        <title>REPORTE SIMULACION</title>
     <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>    
    </head>
    <body>
    <div class="container">
  <h2>Reporte Simulacion</h2>
  <table class="table">
    <thead>
      <tr>
       <th>Tiempo</th>"""
        actual2 = lista.cabeza
        index = 1
        while actual2 != None:
            n=actual2.dato.numero
            index += 1
            actual2 = actual2.siguiente
        print("n es: "+str(n))

        for th in range(1,int(n)+1):
            cabecera+="""
            <th id="""+str(th)+""">Linea de ensamblaje """+str(th)+"""</th>"""
        
        cabecera+="""</tr>
    </thead>
        """
        file.write(cabecera)
        
        actual3 = lista2.cabeza
        index2 = 1
        mayor=None
        menor=None
        while actual3 != None:
            if menor==None and mayor==None:
                menor=int(actual3.dato.numero)
                mayor=int(actual3.dato.numero)
            else:
                if int(actual3.dato.numero)<menor:
                    menor=int(actual3.dato.numero)
                if int(actual3.dato.numero)>mayor:
                    mayor=int(actual3.dato.numero)
            index2 += 1
            actual3 = actual3.siguiente
        print("Mayor es: "+str(mayor))

        lp=1
        contComp=0
        nComp=1
        contTiempo=1
        contTH=0
        
        cadena=""
        actual = self.nombre.productos.cabeza
        while actual != None:
            cadena+=str(actual.dato)+" "
            actual = actual.siguiente
        print(cadena)

        contenido="""
        <tbody>
        """

        while lp<=int(n):
            datosElaboracion="L"+str(lp)+"p"+"C"+str(nComp)+"p"

            
            if re.search(str(datosElaboracion),str(cadena)) and contTH==0:
                print(str(lp)+" , "+str(nComp))
                print(datosElaboracion)
                contComp+=1 

                tiempoElab=ET.SubElement(ElaboracionOptima, 'Tiempo',NoSegundo=str(contTiempo))
                lineaEsam=ET.SubElement(tiempoElab, 'LineaEnsamblaje',NoLinea=str(lp))
                lineaEsam.text="Mover brazo-componente "+str(nComp)

                contenido+="""<tr>
                <td>"""+str(contTiempo)+""". Segundo</td>"""

                for td in range(1,int(lp)):
                    contenido+="""<td>No hacer nada</td>"""

                contenido+="""
                <td>Mover brazo-componente """+str(nComp)+"""</td>
                """
                

                for td in range(int(lp),int(n)):
                    contenido+="""<td>No hacer nada</td>"""
                
                contenido+="""
                </tr>
                """              

                contTiempo+=1
                contTH+=1
                    
            else:
                contComp+=1
                nComp+=1

            if int(contTH)==1:

                tiempoElab2=ET.SubElement(ElaboracionOptima, 'Tiempo',NoSegundo=str(contTiempo))
                lineaEsam2=ET.SubElement(tiempoElab2, 'LineaEnsamblaje',NoLinea=str(lp))
                lineaEsam2.text="Ensamblar componente "+str(nComp)

                contenido+="""<tr>
                <td>"""+str(contTiempo)+""". Segundo</td>"""

                for td in range(1,int(lp)):
                    contenido+="""<td>No hacer nada</td>"""
                    
                contenido+="""
                <td>Ensamblar componente """+str(nComp)+"""</td>
                """

                for td in range(int(lp),int(n)):
                    contenido+="""<td>No hacer nada</td>"""
                
                contenido+="""
                </tr>
                """

                
                    
                nComp+=1
                contTiempo+=1
                contTH=0
                
            if int(contComp)==int(mayor):
                contComp=0
                nComp=1
                lp+=1
                
                
        colspan=int(n)+1
        tiempo=int(contTiempo)-1
        contenido+="""
        <tr>
        <th colspan="""+str(colspan)+""">El producto """+str(nombree)+""" se puede elaborar optimamente en """+str(tiempo)+""" segundos</th>
        </tr>
        </tbody>
        """
        file.write(contenido)

        tiemp = ET.SubElement(Producto, 'TiempoTotal')
        tiemp.text=str(tiempo)




        pieDePagina="""
            </table>
             </div>
             </body>
                    </html>
            """
        file.write(pieDePagina)
        file.close()

        datosXML = ET.tostring(reporte)
        with open("salida.xml",'w') as f:
            f.write(datosXML.decode('utf-8'))
