import tkinter
from tkinter import Label, filedialog,messagebox
from tkinter import *
import tkinter as tk
import xml.etree.ElementTree as xml
import xml.etree.ElementTree as ET
from lista import *
from producto import ListaProducto
import gestor
from maquina import *

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

def cargarMaquina():
    ventana.filename=filedialog.askopenfilename(title="Configuracion de maquina",filetypes=(("xml files", "*.xml"),("all files","*.*")))
    direccion=ventana.filename
    objetoTree=xml.parse(direccion)
    root=objetoTree.getroot()
    
    for nLineasProduccion in root.findall("CantidadLineasProduccion"):
        print(nLineasProduccion.text)
        
    for ListadoLineasProduccion in root.findall("ListadoLineasProduccion"):
        for LineaProduccion in ListadoLineasProduccion.findall("LineaProduccion"):
            for numero in LineaProduccion.findall("Numero"):
                for cantidad in LineaProduccion.findall("CantidadComponentes"):
                    for tiempo in LineaProduccion.findall("TiempoEnsamblaje"):
                        print("Numero: "+numero.text+" Cantidad: "+cantidad.text+" Tiempo: "+tiempo.text)
    
    for ListadoProductos in root.findall("ListadoProductos"):
        for Producto in ListadoProductos.findall("Producto"):

            for nombre in Producto.findall("nombre"):
                nombreProducto=ListaProducto(nombre.text)

                for elaboracion in Producto.findall("elaboracion"):
                    print("Nombre: "+nombre.text+" Elaboracion: "+elaboracion.text)
                    string_list=elaboracion.text.split()
                    string_list=string_list[::-1]
                    for e in range(0,len(string_list)):
                        nombreProducto.agregaMatriz(string_list[e])

                productosMaquina.agregar(nombreProducto)

barraMenu=Menu(ventana)
menuArchivo=Menu(barraMenu)
menuArchivo.add_command(label="Configuracion de maquina",command=cargarMaquina)
menuArchivo.add_command(label="Simulacion",command=cargarSimulacion)
barraMenu.add_cascade(label="Cargar Archivo",menu=menuArchivo)
ventana.config(menu=barraMenu)

def campoTexto():
    resultado=campo_texto.get()
    gestor.mostrarLista(productosMaquina)
    elaboracion = gestor.buscarNodo(productosMaquina,resultado)
    maq = Maquina(elaboracion)
    maq.elaboracionMaquina()
    maq.generarGraphviz()
    img=tkinter.PhotoImage(file="graphviz.png")
    lbl_img=tkinter.Label(ventana,image=img).place(x=30,y=350)
    lbl_img.pack()



Label(ventana, text="Ingrese el nombre del producto a procesar").place(x=30,y=200)
campo_texto=tk.StringVar()
campTxt=tk.Entry(ventana,textvariable=campo_texto).place(x=30,y=230)


btnCarga=tkinter.Button(ventana,text="Cargar",padx=15,pady=10, command=campoTexto).place(x=30,y=260)





ventana.mainloop()