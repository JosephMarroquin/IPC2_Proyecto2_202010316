import re

class Reportehtml:

    def __init__(self,nombre): 
        self.nombre = nombre
    
    def repHtml(self,lista,lista2):

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
                contenido+="""<tr>
                <td>"""+str(contTiempo)+""". Segundo</td>"""

                for td in range(1,int(lp)):
                    contenido+="""<td>No hacer nada</td>"""

                contenido+="""
                <td>Mover brazo-componente """+str(nComp)+"""</td>
                </tr>
                """
                contTiempo+=1
                contTH+=1
                    
            else:
                contComp+=1
                nComp+=1

            if int(contTH)==1:
                contenido+="""<tr>
                <td>"""+str(contTiempo)+""". Segundo</td>"""

                for td in range(1,int(lp)):
                    contenido+="""<td>No hacer nada</td>"""
                    
                contenido+="""
                <td>Ensamblar componente """+str(nComp)+"""</td></tr>
                """
                nComp+=1
                contTiempo+=1
                contTH=0
                
            if int(contComp)==int(mayor):
                contComp=0
                nComp=1
                lp+=1
                
                
        
        contenido+="""
        </tbody>
        """
        file.write(contenido)




        pieDePagina="""
            </table>
             </div>
             </body>
                    </html>
            """
        file.write(pieDePagina)
        file.close()
