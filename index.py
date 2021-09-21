from listaLE import ListaNoOrdenadaLE
from lineaP import ListaLineaProduccion
from nlineaEnsamblaje import ListLE
import tkinter
from tkinter import Label, filedialog,messagebox
from tkinter import *
import tkinter as tk
import xml.etree.ElementTree as xml
import xml.etree.ElementTree as ET
from lista import *
from listaLP import *
from producto import ListaProducto
import gestor
from maquina import *
from reporteHTML import *
import re

ventana=tkinter.Tk()
ventana.geometry("900x620")
cont=0
Label(ventana, text="Listado de productos:").place(x=30,y=0)
lista_productos=Listbox(ventana,width=50)

def cargarSimulacion():
    ventana.filename=filedialog.askopenfilename(title="Archivo de Simulacion",filetypes=(("xml files", "*.xml"),("all files","*.*")))
    direccion=ventana.filename
    objetoTree=xml.parse(direccion)
    root=objetoTree.getroot()
    lista_productos.place(x=30,y=20)
    global cont

    for listaproducto in root.findall("ListadoProductos"):
        for producto in listaproducto.findall("Producto"):
            lista_productos.insert(cont,producto.text)
            cont+=1

productosMaquina=ListaNoOrdenada()
DatoslineaProduccion=ListaNoOrdenadaLP()
nEnsamblaje=ListaNoOrdenadaLE()


def cargarMaquina():
    ventana.filename=filedialog.askopenfilename(title="Configuracion de maquina",filetypes=(("xml files", "*.xml"),("all files","*.*")))
    direccion=ventana.filename
    objetoTree=xml.parse(direccion)
    root=objetoTree.getroot()
    
    for nLineasProduccion in root.findall("CantidadLineasProduccion"):
        print(nLineasProduccion.text)
        nEm=ListLE(nLineasProduccion.text)
        nEnsamblaje.agregar(nEm)
        
    for ListadoLineasProduccion in root.findall("ListadoLineasProduccion"):
        for LineaProduccion in ListadoLineasProduccion.findall("LineaProduccion"):
            for numero in LineaProduccion.findall("Numero"):              
                for cantidad in LineaProduccion.findall("CantidadComponentes"):
                    for tiempo in LineaProduccion.findall("TiempoEnsamblaje"):
                        print("Numero: "+numero.text+" Cantidad: "+cantidad.text+" Tiempo: "+tiempo.text)
                        nlineasp=ListaLineaProduccion(cantidad.text)

                    DatoslineaProduccion.agregar(nlineasp)

    actual = DatoslineaProduccion.cabeza
    index = 1
    mayor=None
    menor=None

    while actual != None:
        if menor==None and mayor==None:
            menor=int(actual.dato.numero)
            mayor=int(actual.dato.numero)
        else:
            if int(actual.dato.numero)<menor:
                menor=int(actual.dato.numero)
            if int(actual.dato.numero)>mayor:
                mayor=int(actual.dato.numero)
        index += 1
        actual = actual.siguiente
    print(mayor)

    lp=1
    contComp=0
    nComp=1

    for nLineasProduccion in root.findall("CantidadLineasProduccion"):
        for ListadoProductos in root.findall("ListadoProductos"):
            for Producto in ListadoProductos.findall("Producto"):
                for nombre in Producto.findall("nombre"):
                    nombreProducto=ListaProducto(nombre.text)                                   
                    
                    for elaboracion in Producto.findall("elaboracion"):
                        print("Nombre: "+nombre.text+" Elaboracion: "+elaboracion.text)
                        lp=1
                        
                        while lp<=int(nLineasProduccion.text): 
                            datosElaboracion="L"+str(lp)+"p"+"C"+str(nComp)+"p"

                            if re.search(str(datosElaboracion),str(elaboracion.text)):
                                contComp+=1
                                nComp+=1
                                nombreProducto.agregaMatriz(datosElaboracion)
                            else:
                                contComp+=1
                                nComp+=1
                            
                            if int(contComp)==int(mayor):
                                contComp=0
                                nComp=1
                                lp+=1
                            
                    
                    productosMaquina.agregar(nombreProducto)
    


def mostrarGrafo(): 
    img=tkinter.PhotoImage(file="graphviz.png")
    lbl_img=tkinter.Label(ventana,image=img).place(x=30,y=350)
    lbl_img.pack()   


barraMenu=Menu(ventana)
menuArchivo=Menu(barraMenu)
menuReporte=Menu(barraMenu)
menuArchivo.add_command(label="Configuracion de maquina",command=cargarMaquina)
menuArchivo.add_command(label="Simulacion",command=cargarSimulacion)
barraMenu.add_cascade(label="Cargar Archivo",menu=menuArchivo)

menuReporte.add_command(label="Reporte HTML")
menuReporte.add_command(label="Reporte cola de secuencia",command=mostrarGrafo)
barraMenu.add_cascade(label="Reportes",menu=menuReporte)
ventana.config(menu=barraMenu)

def campoTexto():
    resultado=campo_texto.get()
    gestor.mostrarLista(productosMaquina)
    gestor.mostrarListaLP(DatoslineaProduccion)
    gestor.mostrarListaLE(nEnsamblaje)
    elaboracion = gestor.buscarNodo(productosMaquina,resultado)
    maq = Maquina(elaboracion)
    nle=Reportehtml(elaboracion)
    nle.repHtml(nEnsamblaje,DatoslineaProduccion)
    #maq.elaboracionMaquina()
    maq.generarGraphviz()

    


Label(ventana, text="Ingrese el nombre del producto a procesar").place(x=30,y=200)
campo_texto=tk.StringVar()
campTxt=tk.Entry(ventana,textvariable=campo_texto).place(x=30,y=230)


btnCarga=tkinter.Button(ventana,text="Cargar",padx=15,pady=10, command=campoTexto).place(x=30,y=260)





ventana.mainloop()