try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

from doctest import master
import tkinter as tk
from tkinter import Toplevel, ttk
import tkinter.font as font
from turtle import width

import PIL.Image, PIL.ImageTk
from numpy import pad

from tkinter import filedialog as fd
import matplotlib
import matplotlib.cm as cm
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import numpy as np
import math
from scipy import integrate
from scipy import stats
from windrose import WindroseAxes

#############################
########### Test imports

import seaborn as sbn
sbn.set(rc={'figure.figsize':(10, 5)})
import pandas as pd

from scipy.interpolate import splrep, BSpline, splev  

import os

###############################
from tkintermapview import TkinterMapView
from asyncio.windows_events import NULL
from tkinter import messagebox

###############################

from pandastable import Table

import ssl
ssl._create_default_https_context = ssl._create_unverified_context     # IMPORTANTE: permite la certificacion del enlace


class APP(tk.Tk):
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.geometry("980x690")
        self.minsize(1020, 630)

        self.title("HERRAMIENTA COMPUTACIONAL PARA EVALUACIÓN DE POTENCIAL DE GENERACIÓN ELÉCTRICA CON RECURSOS EÓLICO Y SOLAR")

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        contenedor_principal = tk.Frame( self ,bg = "deep sky blue" )
        contenedor_principal.grid( padx = 10, pady = 10 , sticky = "nsew")

        contenedor_principal.columnconfigure(0,weight=1)
        contenedor_principal.rowconfigure(0, weight=1)

        self.all_frame_dict = dict()

        for F in (Frame_1, Frame_2,Frame_Inicio,Frame_Ayuda,FrameExcel):
            frame = F(contenedor_principal, self)
            self.all_frame_dict[F] = frame
            frame.grid(row=0, column=0, sticky="NSEW")
        self.show_frame(Frame_Inicio)

    def show_frame(self, contenedor_llamado):

        frame = self.all_frame_dict[contenedor_llamado]
        # self.bind("<Return>", frame.saludarme)
        # self.bind("<KP_Enter>", frame.saludarme)

        # frame.L_3.configure(text="")
        # frame.entrada_usuario.set("")
        # frame.E_1.focus()

        frame.tkraise()


class Frame_Inicio(tk.Frame):

    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.config(bg = 'steel blue',padx=10,pady=10)

        self.logoEPN = PIL.Image.open("logoEPN.png")
        self.logoEPN = self.logoEPN.resize((150,100),PIL.Image.LANCZOS)
        self.logoEPN = PIL.ImageTk.PhotoImage(self.logoEPN)
        self.label_logoEPN=tk.Label(self,image=self.logoEPN,bg = 'steel blue')
        self.label_logoEPN.grid(column=0,row=1,sticky="NEW")


        self.logoFIEE = PIL.Image.open("selloElectrica.png")
        self.logoFIEE = self.logoFIEE.resize((100,100),PIL.Image.Resampling.LANCZOS)
        self.logoFIEE = PIL.ImageTk.PhotoImage(self.logoFIEE)
        self.label_logoFIEE=tk.Label(self,image=self.logoFIEE,bg = 'steel blue')
        self.label_logoFIEE.grid(column=6,row=1,sticky="NEW")


        self.label_titulo = tk.Label(self, text = "HERRAMIENTA COMPUTACIONAL PARA \n EVALUACIÓN DE POTENCIAL DE GENERACIÓN ELÉCTRICA \n CON RECURSOS EÓLICO Y SOLAR",font = ("Times New Roman",18,), fg= 'white', bg = 'steel blue')
        self.label_titulo.grid(column=1,row=0,columnspan=5,rowspan=2,sticky="NSEW")

        self.label_autor = tk.Label(self, text = "Autor: Juan Pablo Cisneros",font = ("Times New Roman",15), fg= 'white', bg = 'steel blue')
        self.label_autor.grid(column=1,row=2,columnspan=5,rowspan=1,sticky="NEW")

        self.btn_siguiente = ttk.Button( self, text = "Siguiente", command = lambda:controller.show_frame(FrameExcel) )
        self.btn_ayuda = ttk.Button( self, text = "Ayuda", command = lambda:controller.show_frame(Frame_Ayuda) )

        self.btn_siguiente.grid(column=6,row=6)
        self.btn_ayuda.grid(column=0,row=6)


        
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)
        self.columnconfigure(2, weight=2)
        self.columnconfigure(3, weight=2)
        self.columnconfigure(4, weight=1)
        self.columnconfigure(5, weight=1)
        self.columnconfigure(6, weight=1)
        
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, weight=1)
        

class Frame_Ayuda(tk.Frame):

    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.config(bg = 'steel blue',padx=10,pady=10)

        self.logoEPN = PIL.Image.open("logoEPN.png")
        self.logoEPN = self.logoEPN.resize((150,100),PIL.Image.LANCZOS)
        self.logoEPN = PIL.ImageTk.PhotoImage(self.logoEPN)
        self.label_logoEPN=tk.Label(self,image=self.logoEPN,bg = 'steel blue')
        self.label_logoEPN.grid(column=0,row=1,sticky="NEW")


        self.logoFIEE = PIL.Image.open("selloElectrica.png")
        self.logoFIEE = self.logoFIEE.resize((100,100),PIL.Image.Resampling.LANCZOS)
        self.logoFIEE = PIL.ImageTk.PhotoImage(self.logoFIEE)
        self.label_logoFIEE=tk.Label(self,image=self.logoFIEE,bg = 'steel blue')
        self.label_logoFIEE.grid(column=6,row=1,sticky="NEW")


        self.label_titulo = tk.Label(self, text = "Ayuda:",font = ("Times New Roman",18,), fg= 'white', bg = 'steel blue')
        self.label_titulo.grid(column=1,row=0,columnspan=5,rowspan=2,sticky="NSEW")

        self.label_autor = tk.Label(self, text = "Autor: Juan Pablo Cisneros",font = ("Times New Roman",15), fg= 'white', bg = 'steel blue')
        self.label_autor.grid(column=1,row=2,columnspan=5,rowspan=1,sticky="NEW")

        
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)
        self.columnconfigure(2, weight=2)
        self.columnconfigure(3, weight=2)
        self.columnconfigure(4, weight=2)
        self.columnconfigure(5, weight=2)
        self.columnconfigure(6, weight=2)
        
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, weight=1)
        
class FrameExcel(tk.Frame):
    def __init__(self, container, controller, *args, **kwargs):

        super().__init__(container, *args, **kwargs)
        
        ######################################
        ######### Variables Globales #########
        self.nombreArchivoExcel="GoldWind GW70-1500.xlsx"
        self.nombreArchivoCSV=""

        self.lat=-0.2129026
        self.lng=-78.492215
        self.anio=2020

        self.varLat=tk.StringVar()
        self.varLng=tk.StringVar()
        self.varAnio=tk.StringVar()
        self.varNombreArchivoExcel=tk.StringVar()

        self.varLat.set("-0.2129026")
        self.varLng.set("-78.492215")
        self.varAnio.set("2020")
        self.varNombreArchivoExcel.set(self.nombreArchivoExcel)
        
        self.varRho=tk.StringVar()
        self.varAnguloInc=tk.StringVar()
        self.varG=tk.StringVar()
        self.varTONC=tk.StringVar()
        self.varPmaxSTC=tk.StringVar()

        self.varRho.set("01")
        self.varAnguloInc.set("02")
        self.varG.set("03")
        self.varTONC.set("04")
        self.varPmaxSTC.set("05")
        
        
        
        self.frameDerecha = tk.Frame(self,borderwidth=5,relief="ridge",bg = 'green')
        self.frameContenido = tk.Frame(self.frameDerecha,borderwidth=5,relief="ridge",bg = 'cyan')
        

        self.frameDatos=tk.Frame(self.frameContenido,borderwidth=5,relief="ridge",bg="yellow")
        self.frameDatos.rowconfigure(0,weight=0)
        self.frameDatos.rowconfigure(1,weight=1)
        self.frameDatos.columnconfigure(0,weight=1)
        self.frameResultados=tk.Frame(self.frameContenido,borderwidth=5,relief="ridge",bg="red")
        
        self.contenidoDatos=tk.Frame(self.frameDatos,bg="cyan")
        self.contenidoDatos.grid(column=0,row=1,sticky="NSEW")
        self.contenidoDatos.columnconfigure(0,weight=1)
        self.contenidoDatos.rowconfigure(0,weight=1)
        self.contenidoDatos.rowconfigure(1,weight=1)
        
        self.frameTablaDatos=tk.Frame(self.contenidoDatos,bg="magenta")
        self.frameGraficoDatos=tk.Frame(self.contenidoDatos,bg="black")
        
        self.frameTablaDatos.grid(column=0,row=0,sticky="NSEW")
        self.frameGraficoDatos.grid(column=0,row=1,sticky="NSEW")
        
        # self.frameDatosTabla=tk.Frame(self.frameDerecha,bg="steel blue")
        # self.frameDatosGraficas=tk.Frame(self.frameDerecha,bg="steel blue")
        # self.frameResultadosGraficos=tk.Frame(self.frameDerecha,bg="steel blue")
        # self.frameResultadosTabla=tk.Frame(self.frameDerecha,bg="steel blue")

        self.frameIzquierda = tk.Frame(self,borderwidth=5,relief="ridge",bg = 'steel blue')

        self.estiloTabs = ttk.Style()
        self.estiloTabs.configure('TNotebook.Tab', font=('Arial','12','bold') )

        self.tabsDatos=tk.Frame(self.frameDatos,bg="green")
        self.contenidoResultado=tk.Frame(self.frameDatos,bg="green")
        
        self.btnTabsDatos1=tk.Button(self.tabsDatos,text="Tab 01",command=self.abrirmapa)
        self.btnTabsDatos2=tk.Button(self.tabsDatos,text="Tab 02",command=self.abrirmapa)
        self.btnTabsDatos3=tk.Button(self.tabsDatos,text="Tab 03",command=self.abrirmapa)
        self.btnTabsDatos4=tk.Button(self.tabsDatos,text="Tab 04",command=self.abrirmapa)
        
        self.tabsDatos.grid(column=0,row=0,sticky="NEW")
        self.btnTabsDatos1.grid(column=0,row=0)
        self.btnTabsDatos2.grid(column=1,row=0)
        self.btnTabsDatos3.grid(column=2,row=0)
        self.btnTabsDatos4.grid(column=3,row=0)
        ######################################
        
        
        ########################################################    
        # Frames para tabs
        ########################################################
        
        
        
        ########################################################
        ########################################################
    
        ########################################################
        # Frame Tab1
        ######################################################## Here 0
        # self.contenedorTabs=ttk.Notebook(self.frameDatos)
        
        # self.frameTab1=ttk.Frame(self.contenedorTabs)
        # self.contenedorTabs.add(self.frameTab1,text="Tab 1")
        
        # self.frameTablaDatos=tk.Frame(self.frameTab1)
        
        # self.plotFigura=Figure(figsize=(2,2))
        # self.subPlotFigura=self.plotFigura.add_subplot()
        # self.canvasPlot=FigureCanvasTkAgg(self.plotFigura,master=self.frameTab1)
        # self.canvasPlot.get_tk_widget().grid(column=0,row=1,sticky="NSEW")
        
        # self.frameTablaDatos.grid(column=0,row=0,sticky="EW")
        
        # self.pt = Table(self.frameTablaDatos)
        # self.pt.grid(column=0,row=0,sticky="NSEW")
        # self.pt.show()
        

        # self.contenedorTabs.grid(column=0,row=0,sticky="NSEW")

        # self.contenedorTabs.columnconfigure(0,weight=1)
        # self.contenedorTabs.rowconfigure(0,weight=1)

        # self.frameTab1.columnconfigure(0,weight=1)
        # self.frameTab1.rowconfigure(0,weight=1)
        # self.frameTab1.rowconfigure(1,weight=1)
        
        ################################# Here1
        
        # self.contenedorTabs2=ttk.Notebook(self.frameResultados)
        
        # self.frameTab11=tk.Frame(self,borderwidth=5,relief="ridge",bg = 'magenta')
        # self.contenedorTabs2.add(self.frameTab11,text="Tab 11")
        
        # self.frameTablaDatos2=tk.Frame(self.frameTab11,bg = 'green')
        
        # self.plotFigura11=Figure(figsize=(2,2))
        # self.subPlotFigura11=self.plotFigura11.add_subplot()
        # self.canvasPlot11=FigureCanvasTkAgg(self.plotFigura11,master=self.frameTab11)
        # self.canvasPlot11.get_tk_widget().grid(column=0,row=1,sticky="NSEW")
        
        # self.frameTablaDatos2.grid(column=0,row=0,sticky="EW")
        
        # self.pt = Table(self.frameTablaDatos2)
        # self.pt.grid(column=0,row=0,sticky="NSEW")
        # self.pt.show()
        

        # self.contenedorTabs2.grid(column=0,row=0,sticky="NSEW")

        # self.contenedorTabs2.columnconfigure(0,weight=1)
        # self.contenedorTabs2.rowconfigure(0,weight=1)
        # self.contenedorTabs2.rowconfigure(1,weight=8)

        # self.frameTab11.columnconfigure(0,weight=1)
        # self.frameTab11.rowconfigure(0,weight=1)
        # self.frameTab11.rowconfigure(1,weight=2)
        
        # self.frameResultados.rowconfigure(0,weight=1)
        # self.frameResultados.columnconfigure(0,weight=1)
        
        
        
        #############################
        
        # self.frameTab2=ttk.Frame(self.contenedorTabs)
        # self.frameTab3=ttk.Frame(self.contenedorTabs)
        # self.frameTab4=ttk.Frame(self.contenedorTabs)


        
        # self.contenedorTabs.add(self.frameTab2,text="Tab 2")
        # self.contenedorTabs.add(self.frameTab3,text="Tab 3")
        # self.contenedorTabs.add(self.frameTab4,text="Tab 4")
        
        

        labelTitulo=tk.Label(self.frameDerecha,text='ESCUELA POLITÉCNICA NACIONAL FACULTAD DE INGENIERÍA ELÉCTRICA Y ELECTRÓNICA',font=('times', 10, 'bold'),bg = 'steel blue',fg= 'white')
        labelTitulo.grid(column=0,row=0,sticky="NSEW",pady=5)
        

        self.labelMenu=tk.Label(self.frameIzquierda,text='Menú',font=('times', 10, 'bold'),bg = 'steel blue',fg= 'white')

        self.labelEscogerBase=tk.Label(self.frameIzquierda,text='Escoger Base de Datos',font=('times', 10, 'bold'),bg = 'steel blue',fg= 'white')
        
        self.label3=tk.Label(self.frameIzquierda,text='Tipo Gráfico',font=('times', 10, 'bold'),bg = 'steel blue',fg= 'white')

        self.btnAbrirMapa=tk.Button(self.frameIzquierda,text="Escoger Coordenadas en Mapa",command=self.abrirmapa)
        
        self.btnCargarNREL=tk.Button(self.frameIzquierda,text="Cargar Datos",command=self.cargarNREL)
        
        

        self.comboBases = ttk.Combobox(self.frameIzquierda,
            state="readonly",
            values=["NREL", "Secretaría del Ambiente DMQ"]
        )


        
        self.comboBases.bind('<<ComboboxSelected>>', self.seleccionComboBases)  

        self.labelMenu.grid(column=0,row=0,sticky="NEW",pady=5)
        self.labelEscogerBase.grid(column=0,row=1,sticky="NEW",pady=2)

        self.comboBases.grid(column=0,row=2,sticky="NEW",pady=2)


        # self.btnAbrirExcel.grid(column=0,row=3, sticky="NEW",pady=10)
        # self.botonAbrirCSV.grid(column=0,row=4, sticky="NEW",pady=10)
        # self.label3.grid(column=0,row=5,sticky="NEW",pady=10)
        

        self.labelLatFrameExcel=tk.Label(self.frameIzquierda,text="Latitud: ",bg = 'steel blue',fg= 'white',font=('times', 10, 'bold'))
        self.entryLatFrameExcel = tk.Entry(self.frameIzquierda, width=20,textvariable=self.varLat)  
        self.labelLngFrameExcel=tk.Label(self.frameIzquierda,text="Longitud: ",bg = 'steel blue',fg= 'white',font=('times', 10, 'bold'))
        self.entryLngFrameExcel = tk.Entry(self.frameIzquierda, width=20,textvariable=self.varLng)  
        self.labelAnioFrameExcel=tk.Label(self.frameIzquierda,text="Año: ",bg = 'steel blue',fg= 'white',font=('times', 10, 'bold'))
        self.entryAnioFrameExcel = tk.Entry(self.frameIzquierda, width=20,textvariable=self.varAnio)  

        self.labelEscogerMetodo=tk.Label(self.frameIzquierda,text="Escoger Método de Evaluación: ",bg = 'steel blue',fg= 'white',font=('times', 10, 'bold'))

        self.labelParametros=tk.Label(self.frameIzquierda,text="Parámetros: ",bg = 'steel blue',fg= 'white',font=('times', 10, 'bold'))

        ####controles metodo solar
        
        self.labelTipoMetodoSolar=tk.Label(self.frameIzquierda,text="Tipo Método Solar:",bg = 'steel blue',fg= 'white',font=('times', 10, 'bold'))
        self.comboTipoMetodoSolar = ttk.Combobox(self.frameIzquierda,
            state="readonly",
            values=["Masters", "Tiwari"]
        )
        self.comboTipoMetodoSolar.set("Masters")
        self.comboTipoMetodoSolar.bind('<<ComboboxSelected>>', self.seleccionTipoMetodoSolar)  

        self.labelModeloPanel=tk.Label(self.frameIzquierda,text="Modelo Panel:",bg = 'steel blue',fg= 'white',font=('times', 10, 'bold'))
        self.comboModeloPanel = ttk.Combobox(self.frameIzquierda,
            state="readonly",
           values=["Modelo 1", "Modelo 2","Modelo 3"]
        )

        self.valoresPaneles=[
            {"Rho":1,"AnguloInc":0,"G":3,"TONC":4,"PmaxSTC":5},
            {"Rho":6,"AnguloInc":0,"G":8,"TONC":9,"PmaxSTC":10},
            {"Rho":11,"AnguloInc":0,"G":13,"TONC":14,"PmaxSTC":15}
        ]
        self.comboModeloPanel.set("Modelo 1")
        self.comboModeloPanel.bind('<<ComboboxSelected>>', self.seleccionComboModeloPanel)  

        self.setValoresPanel(0)

        self.frameRho=tk.Frame(self.frameIzquierda,bg = 'steel blue')
        self.frameAnguloInc=tk.Frame(self.frameIzquierda,bg = 'steel blue')
        self.frameG=tk.Frame(self.frameIzquierda,bg = 'steel blue')
        self.frameTONC=tk.Frame(self.frameIzquierda,bg = 'steel blue')
        self.framePmaxSTC=tk.Frame(self.frameIzquierda,bg = 'steel blue')


        self.labelRho=tk.Label(self.frameRho,text="Rho (ρ):",bg = 'steel blue',fg= 'white',font=('times', 10, 'bold'),anchor="e")
        self.labelAnguloInc=tk.Label(self.frameAnguloInc,text="Ángulo Panel:",bg = 'steel blue',fg= 'white',font=('times', 10, 'bold'),anchor="e")
        self.labelG=tk.Label(self.frameG,text="g (%/ºC):",bg = 'steel blue',fg= 'white',font=('times', 10, 'bold'),anchor="e")
        self.labelTONC=tk.Label(self.frameTONC,text="TONC:",bg = 'steel blue',fg= 'white',font=('times', 10, 'bold'),anchor="e")
        self.labelPmaxSTC=tk.Label(self.framePmaxSTC,text="Pmax STC:",bg = 'steel blue',fg= 'white',font=('times', 10, 'bold'),anchor="e")
        
        self.entryRho = tk.Entry(self.frameRho,textvariable=self.varRho)  

        self.entryAnguloInc = tk.Entry(self.frameAnguloInc,textvariable=self.varAnguloInc)  
        self.entryG = tk.Entry(self.frameG, width=20,textvariable=self.varG)  
        self.entryTONC = tk.Entry(self.frameTONC, width=20,textvariable=self.varTONC)  
        self.entryPmaxSTC = tk.Entry(self.framePmaxSTC, width=20,textvariable=self.varPmaxSTC)  

        self.labelRho.grid(column=0,row=0,sticky="EW",padx=4)  
        self.entryRho.grid(column=1,row=0,sticky="EW",padx=2)  
        self.frameRho.columnconfigure(0,weight=1,uniform="solar")
        self.frameRho.columnconfigure(1,weight=1,uniform="solar")
        self.frameRho.rowconfigure(0,weight=1)

        self.labelAnguloInc.grid(column=0,row=0,sticky="EW",padx=4)  
        self.entryAnguloInc.grid(column=1,row=0,sticky="EW",padx=2)  
        self.frameAnguloInc.columnconfigure(0,weight=1,uniform="solar")
        self.frameAnguloInc.columnconfigure(1,weight=1,uniform="solar")
        self.frameAnguloInc.rowconfigure(0,weight=1)

        self.labelG.grid(column=0,row=0,sticky="EW",padx=4)  
        self.entryG.grid(column=1,row=0,sticky="EW",padx=2)  
        self.frameG.columnconfigure(0,weight=1,uniform="solar")
        self.frameG.columnconfigure(1,weight=1,uniform="solar")
        self.frameG.rowconfigure(0,weight=1)

        self.labelTONC.grid(column=0,row=0,sticky="EW",padx=4)  
        self.entryTONC.grid(column=1,row=0,sticky="EW",padx=2)  
        self.frameTONC.columnconfigure(0,weight=1,uniform="solar")
        self.frameTONC.columnconfigure(1,weight=1,uniform="solar")
        self.frameTONC.rowconfigure(0,weight=1)

        self.labelPmaxSTC.grid(column=0,row=0,sticky="EW",padx=4)  
        self.entryPmaxSTC.grid(column=1,row=0,sticky="EW",padx=2)  
        self.framePmaxSTC.columnconfigure(0,weight=1,uniform="solar")
        self.framePmaxSTC.columnconfigure(1,weight=1,uniform="solar")
        self.framePmaxSTC.rowconfigure(0,weight=1)



        ####controles metodo eolico
        self.labelTipoMetodoEolico=tk.Label(self.frameIzquierda,text="Tipo Método Eólico:",bg = 'steel blue',fg= 'white',font=('times', 10, 'bold'))
        self.comboTipoMetodoEolico = ttk.Combobox(self.frameIzquierda,
            state="readonly",
            values=["Cronológico", "Estadístico (Weibull)"]
        )

        self.comboTipoMetodoEolico.set("Cronológico")
        self.comboTipoMetodoEolico.bind('<<ComboboxSelected>>', self.seleccionTipoMetodoEolico)  

        self.labelCargarArchivo=tk.Label(self.frameIzquierda,text="Cargar Archivo Excel",bg = 'steel blue',fg= 'white',font=('times', 10, 'bold'))

        self.entryNombreArchivo = tk.Entry(self.frameIzquierda, width=20,textvariable=self.varNombreArchivoExcel,state='disabled')  

        self.btnAbrirExcel = tk.Button(self.frameIzquierda, text="Abrir Archivo..", command=self.abrirAnalisisExcel)

        

        # self.labelAnguloInc=tk.Label(self.frameIzquierda,text="Ángulo de inclinación del Panel:",bg = 'steel blue',fg= 'white',font=('times', 10, 'bold'))
        # self.labelG=tk.Label(self.frameIzquierda,text="g:",bg = 'steel blue',fg= 'white',font=('times', 10, 'bold'))
        # self.labelTONC=tk.Label(self.frameIzquierda,text="TONC:",bg = 'steel blue',fg= 'white',font=('times', 10, 'bold'))
        # self.labelPmaxSTC=tk.Label(self.frameIzquierda,text="Pmax STC:",bg = 'steel blue',fg= 'white',font=('times', 10, 'bold'))
        
        # self.entryRho = tk.Entry(self.frameIzquierda, width=20,textvariable=self.varRho)  
        # self.entryAnguloInc = tk.Entry(self.frameIzquierda, width=20,textvariable=self.varAnguloInc)  
        # self.entryG = tk.Entry(self.frameIzquierda, width=20,textvariable=self.varG)  
        # self.entryTONC = tk.Entry(self.frameIzquierda, width=20,textvariable=self.varTONC)  
        # self.entryPmaxSTC = tk.Entry(self.frameIzquierda, width=20,textvariable=self.varPmaxSTC)  


        ###########################################
        self.comboMetodos = ttk.Combobox(self.frameIzquierda,
            state="readonly",
            values=["Solar", "Eólico"]
        )
        self.comboMetodos.bind('<<ComboboxSelected>>', self.seleccionMetodo)  

        self.btnGraficar=tk.Button(self.frameIzquierda,text="Graficar",command=self.mainGraficar)        

        self.frameIzquierda.grid(column=0,row=0, sticky="NSEW")
        self.frameDerecha.grid(column=1,row=0,columnspan=9, sticky="NSEW")
        
        self.frameContenido.grid(column=0,row=1, sticky="NSEW")
        self.frameContenido.columnconfigure(0,weight=1)
        self.frameContenido.columnconfigure(1,weight=1)
        self.frameContenido.rowconfigure(0,weight=1)
        
        self.frameDatos.grid(column=0,row=0,sticky="NSEW")
        self.frameResultados.grid(column=1,row=0,sticky="NSEW")

        

        self.frameIzquierda.columnconfigure(0,weight=1)
        self.frameIzquierda.rowconfigure(0,weight=0)
        self.frameIzquierda.rowconfigure(1,weight=0)
        self.frameIzquierda.rowconfigure(2,weight=0)
        self.frameIzquierda.rowconfigure(3,weight=0)
        self.frameIzquierda.rowconfigure(4,weight=0)
        self.frameIzquierda.rowconfigure(5,weight=0)
        self.frameIzquierda.rowconfigure(6,weight=0)

        self.frameDerecha.columnconfigure(0,weight=1)
        self.frameDerecha.rowconfigure(0,weight=0)
        self.frameDerecha.rowconfigure(1,weight=10)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.columnconfigure(4, weight=1)
        self.columnconfigure(5, weight=1)
        self.columnconfigure(6, weight=1)
        self.columnconfigure(7, weight=1)
        self.columnconfigure(8, weight=1)
        self.columnconfigure(9, weight=1)
        

        self.rowconfigure(0, weight=1)

    def seleccionComboBases(self,event):
        print("--------------")
        print(self.comboBases.get())
        if (self.comboBases.get()=="NREL"):    
            # self.btnAbrirExcel.grid(column=0,row=3, sticky="NEW",pady=10)
            # self.botonAbrirCSV.grid(column=0,row=4, sticky="NEW",pady=10)
            # self.label3.grid(column=0,row=5,sticky="NEW",pady=10)
            # self.comboOpciones.grid(column=0,row=6, sticky="NEW",pady=10)
            self.labelLatFrameExcel.grid(column=0,row=3, sticky="NEW",pady=2)
            self.entryLatFrameExcel.grid(column=0,row=4, sticky="NEW",pady=2)
            self.labelLngFrameExcel.grid(column=0,row=5, sticky="NEW",pady=2)
            self.entryLngFrameExcel.grid(column=0,row=6, sticky="NEW",pady=2)

            self.btnAbrirMapa.grid(column=0,row=7, sticky="NEW",pady=[10,0])

            self.labelAnioFrameExcel.grid(column=0,row=8,sticky="NEW",pady=2)
            self.entryAnioFrameExcel.grid(column=0,row=9,sticky="NEW",pady=2)
            
            self.btnCargarNREL.grid(column=0,row=10, sticky="NEW",pady=[10,0])
            
            

    def setValoresPanel(self,index):
        self.varRho.set(str(self.valoresPaneles[index]["Rho"]))
        self.varAnguloInc.set(str(self.valoresPaneles[index]["AnguloInc"]))
        self.varG.set(str(self.valoresPaneles[index]["G"]))
        self.varTONC.set(str(self.valoresPaneles[index]["TONC"]))
        self.varPmaxSTC.set(str(self.valoresPaneles[index]["PmaxSTC"]))

    def seleccionComboModeloPanel(self,event):
        if self.comboModeloPanel.get()=="Modelo 1":
            self.setValoresPanel(0)
        if self.comboModeloPanel.get()=="Modelo 2":
            self.setValoresPanel(1)
        if self.comboModeloPanel.get()=="Modelo 3":
            self.setValoresPanel(2)

    def seleccionMetodo(self,event):
        if self.comboMetodos.get()=="Solar":
            self.labelTipoMetodoEolico.grid_forget()
            self.comboTipoMetodoEolico.grid_forget()
            self.labelCargarArchivo.grid_forget()
            self.entryNombreArchivo.grid_forget()
            self.btnAbrirExcel.grid_forget()
            self.btnGraficar.grid_forget()
            ##########################
            self.labelTipoMetodoSolar.grid(column=0,row=12,sticky="NEW",pady=2)
            self.comboTipoMetodoSolar.grid(column=0,row=13,sticky="NEW",pady=2)

            #self.labelRho.grid(column=0,row=14,sticky="NEW",pady=2)
            # self.labelAnguloInc.grid(column=0,row=16,sticky="NEW",pady=2)
            # self.labelG.grid(column=0,row=18,sticky="NEW",pady=2)
            # self.labelTONC.grid(column=0,row=20,sticky="NEW",pady=2)
            # self.labelPmaxSTC.grid(column=0,row=22,sticky="NEW",pady=2)
            
            self.labelModeloPanel.grid(column=0,row=15,sticky="NEW",pady=2)
            self.comboModeloPanel.grid(column=0,row=16,sticky="NEW",pady=2)

            
            self.frameRho.grid(column=0,row=17,sticky="NSEW",pady=2)
            self.frameAnguloInc.grid(column=0,row=18,sticky="NSEW",pady=2)
            self.frameG.grid(column=0,row=19,sticky="NSEW",pady=2)
            self.frameTONC.grid(column=0,row=20,sticky="NSEW",pady=2)
            self.framePmaxSTC.grid(column=0,row=21,sticky="NSEW",pady=2)

            self.btnGraficar.grid(column=0,row=22,sticky="NEW",pady=10)


        if self.comboMetodos.get()=="Eólico":
            self.labelTipoMetodoSolar.grid_forget()
            self.comboTipoMetodoSolar.grid_forget()

            self.labelRho.grid_forget()
            self.labelAnguloInc.grid_forget()
            self.labelG.grid_forget()
            self.labelTONC.grid_forget()
            self.labelPmaxSTC.grid_forget()
            
            self.entryRho.grid_forget()
            self.entryAnguloInc.grid_forget()
            self.entryG.grid_forget()
            self.entryTONC.grid_forget()
            self.entryPmaxSTC.grid_forget()

            self.btnGraficar.grid_forget()

            #######################
            self.labelTipoMetodoEolico.grid(column=0,row=12,sticky="NEW",pady=2)
            self.comboTipoMetodoEolico.grid(column=0,row=13,sticky="NEW",pady=2)
            self.labelCargarArchivo.grid(column=0,row=14,sticky="NEW",pady=2)
            self.entryNombreArchivo.grid(column=0,row=15,sticky="NEW",pady=2)
            self.btnAbrirExcel.grid(column=0,row=16,sticky="NEW",pady=2)
            self.btnGraficar.grid(column=0,row=17,sticky="NEW",pady=10)
        if self.comboMetodos.get()=="":
            print("Vaciooooo")

            
    def seleccionTipoMetodoSolar(self,event):
        pass

    def seleccionTipoMetodoEolico(self,event):
        pass

    def mainGraficar(self):
        print("Graficar main")
        self.plotCurvaAerogenerador()

    def abrirmapa(self):
        self.ventanaMapa=Toplevel()
        self.ventanaMapa.geometry("800x600")
        self.ventanaMapa.title("Escoger Coordenadas")

        self.frameMapa = tk.Frame(self.ventanaMapa,borderwidth=5,relief="ridge",bg = 'steel blue')

        

        self.labelOrdenes=tk.Label(self.frameMapa,text="Ingrese coordenadas o seleccionelas con el mouse",bg = 'steel blue',fg= 'white',font=('times', 14, 'bold'))

        self.map_widget = TkinterMapView(self.frameMapa, width=400, height=300, corner_radius=0,pady=2.2,padx=5)
        self.map_widget.grid(column=0,row=1,columnspan=6,sticky="NSEW")
        self.map_widget.set_position(self.lat,self.lng)
        self.map_widget.add_right_click_menu_command(label="Seleccionar Coordenadas",
                                        command=self.add_marker_event,
                                        pass_coords=True)
        
        
    
        self.map_widget.add_left_click_map_command(self.left_click_event)

        self.lastMarker=NULL

        self.map_widget.set_zoom(int(7))
        self.map_widget.set_position(self.lat, self.lng)
        self.lastMarker=self.map_widget.set_marker(self.lat, self.lng)

        

        self.labelLat=tk.Label(self.frameMapa,text="Latitud: ",bg = 'steel blue',fg= 'white',font=('times', 10, 'bold'))
        self.entryLat = tk.Entry(self.frameMapa, width=20,textvariable=self.varLat)  
        self.labelLng=tk.Label(self.frameMapa,text="Longitud: ",bg = 'steel blue',fg= 'white',font=('times', 10, 'bold'))
        self.entryLng = tk.Entry(self.frameMapa, width=20,textvariable=self.varLng)  
        self.btnUbicar=tk.Button(self.frameMapa,text="Ubicar Marcador",command=self.ubicarMarcador)
        self.btnEscoger=tk.Button(self.frameMapa,text="Escoger coordenadas",command=self.escogerCoord)

        self.labelOrdenes.grid(column=0,row=0,sticky="EW",columnspan=6)
        self.labelLat.grid(column=0,row=2,sticky="EW",pady=5,padx=5)
        self.entryLat.grid(column=1,row=2,sticky="EW",pady=5,padx=5)
        self.labelLng.grid(column=2,row=2,sticky="EW",pady=5,padx=5)
        self.entryLng.grid(column=3,row=2,sticky="EW",pady=5,padx=5)
        self.btnUbicar.grid(column=4,row=2,sticky="EW",pady=5,padx=5)
        self.btnEscoger.grid(column=5,row=2,sticky="EW",pady=5,padx=5)



        self.frameMapa.grid(column=0,row=0,sticky="NSEW")
        
        self.frameMapa.rowconfigure(0,weight=0)
        self.frameMapa.rowconfigure(1,weight=9)
        self.frameMapa.rowconfigure(2,weight=1)
        self.frameMapa.columnconfigure(0,weight=1)
        self.frameMapa.columnconfigure(1,weight=1)
        self.frameMapa.columnconfigure(2,weight=1)
        self.frameMapa.columnconfigure(3,weight=1)
        self.frameMapa.columnconfigure(4,weight=1)
        self.frameMapa.columnconfigure(5,weight=1)

        self.ventanaMapa.rowconfigure(0,weight=1)
        self.ventanaMapa.columnconfigure(0,weight=1)

    def ubicarMarcador(self):
        self.lat=float(self.varLat.get())
        self.lng=float(self.varLng.get())
        if self.lastMarker!=NULL:
            self.lastMarker.delete()
            self.lastMarker=self.map_widget.set_marker(self.lat, self.lng)
            


    def add_marker_event(self,coords):
        if self.lastMarker!=NULL:
            self.lastMarker.delete()
            self.lastMarker=self.map_widget.set_marker(coords[0], coords[1])
            self.varLat.set(str(coords[0]))
            self.varLng.set(str(coords[1]))
            self.lat=float(self.varLat.get())
            self.lng=float(self.varLng.get())

    def left_click_event(self,coords):
        if self.lastMarker!=NULL:
            self.lastMarker.delete()
            self.lastMarker=self.map_widget.set_marker(coords[0], coords[1])
            self.varLat.set(str(coords[0]))
            self.varLng.set(str(coords[1]))
            self.lat=float(self.varLat.get())
            self.lng=float(self.varLng.get())

    def escogerCoord(self):
        self.ventanaMapa.destroy()
        self.ventanaMapa.update()

    def abrirAnalisisExcel(self):
        
        filetypes = (
            ('Archivos Excel', '*.xlsx'),
            ('Todos los Archivos', '*.*')
        ) 
        self.nombreArchivoExcel = fd.askopenfilename( 
        title='Abrir Archivo',
        filetypes=filetypes)  

        self.pathInfo=os.path.split(os.path.abspath(self.nombreArchivoExcel))

        self.varNombreArchivoExcel.set(self.pathInfo[1])

        self.plotCurvaAerogenerador()



    def plot1(self):
        print("plot 1")
        self.subPlotFigura.clear()
        x=np.linspace(-100,100,num=200)
        y=np.sin(0.002*x**2)
        self.subPlotFigura.plot(x,y)
        self.canvasPlot.draw()

    def plotCurvaAerogenerador(self):
        spline, gold_filt, vel_arranque, vel_parada = curva_Goldwind('GoldWind GW70-1500.xlsx')
        
        x=np.linspace(0,30,1000)                                          # se define los limitesde velocidad para la grafica de, 1000 valores desde (0 m/s) hasta (30 m/s) 
        self.subPlotFigura.clear()
                            
        self.subPlotFigura.plot(x, spline(x), label='Curva Aerogenerador')               # grafica los alores de (y) y de (x)
        self.subPlotFigura.set_title('(Potencia - Velocidad) del Aerogenerador', fontsize=16)
        self.subPlotFigura.set_ylabel('Potencia [W] ', fontsize=15)
        self.subPlotFigura.set_xlabel('Velocidad [m/s] ', fontsize=15)
        self.canvasPlot.draw()
        
    #####################################################################################################################
    ###########################################     Metodos Globales    #################################################
    def cargarNREL(self):
        lat, lon, year = -3.99, -79.26, 2019
        # self.lat
        # self.lng
        # self.anio
        lat, lng, year = -3.99, -79.26, 2019                      # latitud, longitud y el año
        api_key = '{{WT0MS4JUkh59reR6YxisV0WpybhCyfjhzTrGexNO}}'  # clave api de la NSRDB
        attributes = 'ghi,dhi,wind_speed,air_temperature,wind_direction,relative_humidity'    # Establezca los atributos a extraer   
        leap_year = 'false'                                       # año bisiesto como verdadero o falso. 
        interval = '60'                                           # intervalo de tiempo en minutos
        utc = 'false'                                             # Especifique el Tiempo Universal Coordinado (UTC), 'true' utilizará el UTC, 'false' utilizará la zona 
        your_name = 'Juan+Cisneros'
        reason_for_use = 'Thesis+research'
        your_affiliation = 'National+Polytechnic+School'
        your_email = 'juan.cisneros@epn.edu.ec'
        mailing_list = 'true'
        
        url = 'https://developer.nrel.gov/api/nsrdb/v2/solar/psm3-download.csv?api_key=WT0MS4JUkh59reR6YxisV0WpybhCyfjhzTrGexNO&full_name=Juan+Cisneros&email=juan.cisneros@epn.edu.ec&affiliation=National+Polytechnic+School&reason=Thesis+research&mailing_list=true&wkt=POINT({lng}+{lat})&names={year}&attributes=dhi,dni,ghi,clearsky_dhi,clearsky_dni,clearsky_ghi,cloud_type,dew_point,air_temperature,surface_pressure,relative_humidity,solar_zenith_angle,total_precipitable_water,wind_direction,wind_speed,fill_flag&leap_day=false&utc=false&interval=60'.format(year=self.anio, lat=self.lat, lng=self.lng)

        print(url)

        try:
            info = pd.read_csv(url, nrows=1)                                   # Devuelve informacion del de la base de datos

            timezone, elevation = info['Local Time Zone'], info['Elevation'] 
            
            print(info)
            print("-------------------------------------------------------------------------")
            print(timezone)
            print("-------------------------------------------------------------------------")
            print(elevation)
            print("-------------------------------------------------------------------------")
            print("-------------------------------------------------------------------------")
            
            df = pd.read_csv(url, skiprows=2)
            #(Establece el índice de tiempo en el marco de datos de pandas:)
            df = df.set_index(pd.date_range('1/1/{yr}'.format(yr=year), freq=interval+'Min', periods=525600/int(interval)))

            print(df)
            
            self.labelEscogerMetodo.grid(column=0,row=11,sticky="NEW",pady=2)
            self.comboMetodos.grid(column=0,row=12,sticky="NEW",pady=2)
            
            self.bdd_float=df
            self.L=self.lng
            #self.pt1=Table()
        except:
            messagebox.showinfo(message="No existen datos para la coordenada seleccionada", title="Error")


        
    
    #####################################################################################################################


class Frame_1(tk.Frame):

    def __init__(self, container, controller, *args, **kwargs):

        super().__init__(container, *args, **kwargs)
        
        #self.entrada_usuario = tk.StringVar()

        labelTitulo=tk.Label(self,text='ESCUELA POLITÉCNICA NACIONAL FACULTAD DE INGENIERÍA ELÉCTRICA Y ELECTRÓNICA\nDETERMINACIÓN DE CURVA DE RENDIMIENTO AEROGENERADOR\nCENTRAL VILLONACO',font=('times', 10, 'bold'))
        labelTitulo.grid(column=0,row=0,sticky="nsew")

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)


class Frame_2(tk.Frame):

    def __init__(self, container, controller, *args, **kwargs):

        super().__init__(container, *args, **kwargs)
        self.configure(bg="black")

        self.entrada_usuario = tk.StringVar()

        L_1 = tk.Label(self, text="MI FIRST FRAME WITH OOP AND TKINTER", font=(
            "Times New Roman", 14, "bold"), bg="yellow", fg="blue")
        L_1.grid(row=0, column=0, columnspan=4, sticky="n")
        L_2 = tk.Label(self, text="Entry name: ", font=(
            "Times New Roman", 12), bg="yellow")
        L_2.grid(row=1, column=0, sticky="w")

        self.E_1 = ttk.Entry(self, textvariable=self.entrada_usuario)
        self.E_1.focus()
        self.E_1.grid(row=1, column=1, columnspan=2, padx=(0, 10))

        B_1 = ttk.Button(self, text="SAY HI", command=self.saludarme)
        B_1.grid(row=1, column=3, sticky="e")

        self.L_3 = tk.Label(self, textvariable="", font=(
            "Times New Roman", 12, "bold"), bg="yellow")
        self.L_3.grid(row=2, column=0, columnspan=4, sticky="nsew")

        B_2 = ttk.Button(self, text="espannol",
                         command=lambda: controller.show_frame(Frame_1))
        B_2.grid(row=3, column=0)

    def saludarme(self, *args):
        self.L_3.configure(text="Good Morning, {}.".format(
            self.entrada_usuario.get()))


root = APP()


root.mainloop()
