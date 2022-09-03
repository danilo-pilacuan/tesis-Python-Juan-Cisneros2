# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 08:07:10 2022

@author: jan-c
"""

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

from logging import root
import tkinter as tk
from tkinter import ttk
import tkinter.font as font
from tkinter import PhotoImage
from tkinter import *
from tkinter import Scrollbar
from turtle import color



# Se crea clase principal (tk.Tk), la cual es la encargada de manejar los Frames
class APP(tk.Tk):
    def __init__(self,*args,**kwargs):        
        super().__init__(*args,**kwargs)

      #  self.create_scrollbar()

        contenedor_principal = tk.Frame( self ,bg = "deep sky blue" )
        contenedor_principal.grid( padx = 10, pady = 10 , sticky = "nsew")
        

        self.todos_los_frames = dict()

        for F in (pagina1, pagina2, pagina3, pagina4, pagina5, pagina6, pagina7, pagina8, pagina9, pagina10):
            frame = F(contenedor_principal, self)
            self.todos_los_frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")
        self.show_frame(pagina1)

    def show_frame(self,contenedor_llamado):
        frame = self.todos_los_frames[contenedor_llamado]
        frame.tkraise()
        

    # def create_scrollbar(self):
    #    self.scrollbar = Scrollbar(orient='vertical')
    #    self.scrollbar.grid(row=6,column=3,rowspan=10,sticky='sn')

#************************************Pagina 1: Pagina principal************************************     
class pagina1(tk.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.config(bg = 'steel blue')

        self.ln = tk.Label(self, text = " ",bg = 'steel blue')
        self.l1 = tk.Label(self, text = "HERRAMIENTA COMPUTACIONAL PARA \n EVALUACIÓN DE POTENCIAL DE GENERACIÓN ELÉCTRICA \n CON RECURSOS EÓLICO Y SOLAR",font = ("Times New Roman",16,), fg= 'white', bg = 'steel blue')
        self.l2 = tk.Label(self, text = "",font = ("Times New Roman",12), fg= 'white', bg = 'steel blue')
        self.l3 = tk.Label(self, text = " ",font = ("Times New Roman",12), fg= 'white', bg = 'steel blue')
        self.l4 = tk.Label(self, text = "Autor: Juan Pablo Cisneros",font = ("Times New Roman",15), fg= 'white', bg = 'steel blue')
        self.ln2 = tk.Label(self, text = " ",bg = 'steel blue')
        self.b1 = ttk.Button( self, text = "Siguiente", command = lambda:controller.show_frame(pagina3) )
        self.b2 = ttk.Button( self, text = "Ayuda", command = lambda:controller.show_frame(pagina2) )

        self.ln.grid(row = 0, column = 1, padx = 6, pady = 20, columnspan = 2)
        self.l1.grid(row = 1, column = 1, padx = 6, pady = 10, columnspan = 2)
        self.l2.grid(row = 2, column = 1, padx = 6, pady = 10, columnspan = 2)
        self.l3.grid(row = 3, column = 1, padx = 6, pady = 10, columnspan = 2)
        self.l4.grid(row = 5, column = 1, padx = 6, pady = 50, columnspan = 2)
        self.ln2.grid(row = 6, column = 1, padx = 6, pady = 20, columnspan = 2)
        self.b1.grid(row = 7, column = 3, padx=50, pady=15)
        self.b2.grid(row = 7, column = 0, padx=50, pady=15)

#************************************Pagina 2: Manual Usuario************************************  
class pagina2(tk.Frame):
    def __init__(self, container,controller,*args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.config(bg = 'steel blue')

        self.l1 = tk.Label(self, text = "MANUAL DE USUARIO",font = ("Times New Roman",12), fg= 'white', bg = 'steel blue' )
        self.ln = tk.Label(self, text = " ",font = ("Times New Roman",12), bg = 'steel blue' )
        self.b1 = ttk.Button( self, text = "Regresar", command = lambda:controller.show_frame(pagina1) )

        #foto = PhotoImage(file = 'bitmap.png')
        #label = Label(self, image = foto)
        #label.image = foto
        #label.grid(row=0, column=0, padx=10, pady=10, sticky = "nsew")

        self.l1.grid(row = 0, column = 0, padx = 50, pady = 20)
        self.ln.grid(row = 1, column = 1, padx = 150, pady = 150)
        self.b1.grid(row = 2, column = 2, padx=10, pady=15)


#************************************Pagina 3: Seleccion de la base de datos************************************  
class pagina3(tk.Frame):
    def __init__(self, container,controller,*args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.config(bg = 'steel blue')

        #self.ln2 = tk.Label(self, text = " ", bg = 'steel blue')
        self.l1 = tk.Label(self, text = "Seleccione la base de datos con la que desea trabajar:",font = ("Times New Roman",14),fg= 'white', bg = 'steel blue' )
        self.ln = tk.Label(self, text = " ",font = ("Times New Roman",12), bg = 'steel blue' )
        self.b1 = ttk.Button( self, text = "Nasa", command = lambda:controller.show_frame(pagina4))
        self.b2 = ttk.Button( self, text = "Secretaria del Ambiente de Quito", command = lambda:controller.show_frame(pagina10))
        self.b3 = ttk.Button( self, text = "Regresar", command = lambda:controller.show_frame(pagina1))

        #foto = PhotoImage(file='front.png')
        #label = Label(image=foto)
        #label.image = foto
        #label.grid(row=0, column=0, padx=10, pady=10, sticky = "wn")

        #self.ln2.grid(row = 0, column = 0, padx = 50, pady = 100, rowspan = 4)
        self.l1.grid(row = 0, column = 0, padx = 6, pady = 25, columnspan = 4)
        self.ln.grid(row = 1, column = 1, padx = 50, pady = 100, rowspan = 1)
        self.b1.grid(row = 3, column = 1, padx=10, pady=15)
        self.b2.grid(row = 3, column = 4, padx=10, pady=15)
        self.b3.grid(row = 4, column = 0, padx=10, pady=15)

#************************************Pagina 4: Nasa************************************  
class pagina4(tk.Frame):
    def __init__(self, container,controller,*args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.config(bg = 'steel blue')

        self.ln = tk.Label(self, text = "Base de datos selecionada: \n\t\t\t\t Nasa", font = ("Times New Roman",14),fg= 'white', bg = 'green')
        self.l1 = tk.Label(self, text = "Ingrese los parametros:",font = ("Times New Roman",12), fg= 'white', bg = 'steel blue')
        self.l2 = tk.Label(self, text = "Longitud:",font = ("Times New Roman",12), fg= 'white', bg = 'steel blue')
        self.l3 = tk.Label(self, text = "Latitud:",font = ("Times New Roman",12), fg= 'white', bg = 'steel blue')
        self.l4 = tk.Label(self, text = "Año:",font = ("Times New Roman",12), fg= 'white', bg = 'steel blue')
        self.txt1 = Entry(self, bg = 'white')
        self.txt2 = Entry(self, bg = 'white')
        self.txt3 = Entry(self, bg = 'white')
        self.ln2 = tk.Label(self, text = " ", bg = 'steel blue')
        self.b1 = ttk.Button( self, text = "Cargar", command = lambda:controller.show_frame(pagina5))
        self.b2 = ttk.Button( self, text = "Regresar", command = lambda:controller.show_frame(pagina3))

        #foto = PhotoImage(file='front.png')
        #label = Label(image=foto)
        #label.image = foto
        #label.grid(row=0, column=0, padx=10, pady=10, sticky = "wn")

        self.ln.grid(row = 0, column = 0, padx = 6, pady = 5, columnspan = 4)
        self.l1.grid(row = 1, column = 0, padx = 6, pady = 15, columnspan = 2)
        self.l2.grid(row = 2, column = 1, padx = 6, pady = 25)
        self.l3.grid(row = 3, column = 1, padx = 6, pady = 25)
        self.l4.grid(row = 4, column = 1, padx = 6, pady = 25)
        self.txt1.grid(row = 2, column = 3, padx = 6, pady = 25)
        self.txt2.grid(row = 3, column = 3, padx = 6, pady = 25)
        self.txt3.grid(row = 4, column = 3, padx = 6, pady = 25)
        self.ln2.grid(row = 5, column = 0, padx = 6, pady = 5, columnspan = 4)
        self.b1.grid(row = 6, column = 4, padx=10, pady=15)
        self.b2.grid(row = 6, column = 0, padx=10, pady=15)

#************************************Pagina 5: Tipo de generacion************************************  
class pagina5(tk.Frame):
    def __init__(self, container,controller,*args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.config(bg = 'steel blue')

        #self.ln2 = tk.Label(self, text = " ", bg = 'steel blue')
        self.l1 = tk.Label(self, text = "Seleccione el tipo de generacion:",font = ("Times New Roman",12),fg= 'white', bg = 'steel blue' )
        self.ln = tk.Label(self, text = " ",font = ("Times New Roman",12), bg = 'steel blue' )
        self.b1 = ttk.Button( self, text = "Generacion: Eolica", command = lambda:controller.show_frame(pagina6))
        self.b2 = ttk.Button( self, text = "Generacion: Solar", command = lambda:controller.show_frame(pagina8))
        self.b3 = ttk.Button( self, text = "Regresar", command = lambda:controller.show_frame(pagina1))

        #foto = PhotoImage(file='front.png')
        #label = Label(image=foto)
        #label.image = foto
        #label.grid(row=0, column=0, padx=10, pady=10, sticky = "wn")

        #self.ln2.grid(row = 0, column = 0, padx = 50, pady = 100, rowspan = 4)
        self.l1.grid(row = 0, column = 0, padx = 6, pady = 25, columnspan = 4)
        self.ln.grid(row = 1, column = 1, padx = 50, pady = 150, rowspan = 2)
        self.b1.grid(row = 3, column = 1, padx=10, pady=15)
        self.b2.grid(row = 3, column = 4, padx=10, pady=15)
        self.b3.grid(row = 4, column = 0, padx=10, pady=15)

#************************************Pagina 6: Seleccion de tubinas y metodo************************************  
class pagina6(tk.Frame):
    def __init__(self, container,controller,*args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.config(bg = 'steel blue')

        self.ln = tk.Label(self, text = " ", bg = 'steel blue')
        self.l1 = tk.Label(self, text = "Metodo de generacion: Eólica",font = ("Times New Roman",12), fg= 'white', bg = 'steel blue')
        self.l2 = tk.Label(self, text = "Escoja el tipo de turbina:",font = ("Times New Roman",12), fg= 'white', bg = 'steel blue')
        self.l3 = tk.Label(self, text = "Escoja el metodo:",font = ("Times New Roman",12), fg= 'white', bg = 'steel blue')
        self.se1 = ttk.Combobox(self, state="readonly", values=['Turbina 1', 'Turbina 2', "Turbina 3", "Turbina 4"])
        self.se2 = ttk.Combobox(self, state="readonly", values=['Estadistico', 'Cronologico'])
        self.ln2 = tk.Label(self, text = " ", bg = 'steel blue')
        self.b1 = ttk.Button( self, text = "Resultados", command = lambda:controller.show_frame(pagina7))
        self.b2 = ttk.Button( self, text = "Regresar", command = lambda:controller.show_frame(pagina1))

        self.ln.grid(row = 0, column = 0, padx = 6, pady = 5, columnspan = 4)
        self.l1.grid(row = 1, column = 0, padx = 6, pady = 15, columnspan = 2)
        self.l2.grid(row = 2, column = 1, padx = 6, pady = 25)
        self.l3.grid(row = 3, column = 1, padx = 6, pady = 25)
        self.se1.grid(row = 2, column = 3, padx = 6, pady = 25)
        self.se2.grid(row = 3, column = 3, padx = 6, pady = 25)
        self.ln2.grid(row = 5, column = 0, padx = 6, pady = 5, columnspan = 4)
        self.b1.grid(row = 6, column = 4, padx=10, pady=15)
        self.b2.grid(row = 6, column = 0, padx=10, pady=15)

#************************************Pagina 7: Resultado eolica************************************  
class pagina7(tk.Frame):
    def __init__(self, container,controller,*args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.config(bg = 'steel blue')

        self.ln = tk.Label(self, text = " ", bg = 'steel blue')
        self.l1 = tk.Label(self, text = "Resultados Eolica",font = ("Times New Roman",12), fg= 'white', bg = 'steel blue')
        self.b2 = ttk.Button( self, text = "Regresar", command = lambda:controller.show_frame(pagina1))

        self.ln.grid(row = 0, column = 0, padx = 6, pady = 5, columnspan = 4)
        self.l1.grid(row = 1, column = 0, padx = 6, pady = 15, columnspan = 2)
        self.b2.grid(row = 6, column = 0, padx=10, pady=15)

#************************************Pagina 8: Seleccion tipo panel y angulo de inclinacion************************************  
class pagina8(tk.Frame):
    def __init__(self, container,controller,*args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.config(bg = 'steel blue')

        self.ln = tk.Label(self, text = " ", bg = 'steel blue')
        self.l1 = tk.Label(self, text = "Metodo de generacion: Solar",font = ("Times New Roman",12), fg= 'white', bg = 'steel blue')
        self.l2 = tk.Label(self, text = "Escoja el tipo de panel:",font = ("Times New Roman",12), fg= 'white', bg = 'steel blue')
        self.l3 = tk.Label(self, text = "Escoja el angulo de inclinación:",font = ("Times New Roman",12), fg= 'white', bg = 'steel blue')
        self.se1 = ttk.Combobox(self, state="readonly", values=['Panel 1', 'Panel 2', 'Panel 3', 'Panel 4'])
        self.txt1 = Entry(self, bg = 'white')
        self.ln2 = tk.Label(self, text = " ", bg = 'steel blue')
        self.b1 = ttk.Button( self, text = "Resultados", command = lambda:controller.show_frame(pagina9))
        self.b2 = ttk.Button( self, text = "Regresar", command = lambda:controller.show_frame(pagina1))

        self.ln.grid(row = 0, column = 0, padx = 6, pady = 5, columnspan = 4)
        self.l1.grid(row = 1, column = 0, padx = 6, pady = 15, columnspan = 2)
        self.l2.grid(row = 2, column = 1, padx = 6, pady = 25)
        self.l3.grid(row = 3, column = 1, padx = 6, pady = 25)
        self.se1.grid(row = 2, column = 3, padx = 6, pady = 25)
        self.txt1.grid(row = 3, column = 3, padx = 6, pady = 25)
        self.ln2.grid(row = 5, column = 0, padx = 6, pady = 5, columnspan = 4)
        self.b1.grid(row = 6, column = 4, padx=10, pady=15)
        self.b2.grid(row = 6, column = 0, padx=10, pady=15)

#************************************Pagina 9: Resultado solar************************************  
class pagina9(tk.Frame):
    def __init__(self, container,controller,*args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.config(bg = 'steel blue')

        self.ln = tk.Label(self, text = " ", bg = 'steel blue')
        self.l1 = tk.Label(self, text = "Resultados Solar",font = ("Times New Roman",15), fg= 'white', bg = 'steel blue')
        self.b2 = ttk.Button( self, text = "Regresar", command = lambda:controller.show_frame(pagina1))

        self.ln.grid(row = 0, column = 0, padx = 6, pady = 5, columnspan = 4)
        self.l1.grid(row = 1, column = 0, padx = 6, pady = 15, columnspan = 2)
        self.b2.grid(row = 6, column = 0, padx=10, pady=15)

#************************************Pagina 10: Secretaria lugar************************************  
class pagina10(tk.Frame):
    def __init__(self, container,controller,*args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.config(bg = 'steel blue')

        self.ln = tk.Label(self, text = "Base de datos seleccionada: \n\t Secretaria del Ambiente de Quito",font = ("Times New Roman",12), fg= 'white', bg = 'steel blue')
        self.l2 = tk.Label(self, text = "Escoja el lugar de analisis:",font = ("Times New Roman",12), fg= 'white', bg = 'steel blue')
        self.se1 = ttk.Combobox(self, state="readonly", values=['Lugar 1', 'Lugar 2', 'Lugar 3', 'Lugar 4'])
        self.ln2 = tk.Label(self, text = " ", bg = 'steel blue')
        self.b1 = ttk.Button( self, text = "Siguiente", command = lambda:controller.show_frame(pagina5))
        self.b2 = ttk.Button( self, text = "Regresar", command = lambda:controller.show_frame(pagina1))

        self.ln.grid(row = 0, column = 0, padx = 6, pady = 5, columnspan = 4)
        self.l2.grid(row = 2, column = 1, padx = 6, pady = 25)
        self.se1.grid(row = 2, column = 3, padx = 6, pady = 25)
        self.ln2.grid(row = 5, column = 0, padx = 6, pady = 5, columnspan = 4)
        self.b1.grid(row = 6, column = 4, padx=10, pady=15)
        self.b2.grid(row = 6, column = 0, padx=10, pady=15)


if __name__ == '__main__':
    root = APP() 
    root.title('Tesis')
    #root.geometry("950x550")
    root.resizable(width=False, height=False)
    root.mainloop()