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

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

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
from matplotlib import dates as mdates

###############################

from pandastable import Table,TableModel

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
        contenedor_principal.grid( padx = 5, pady = 5 , sticky = "nsew")

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
        
        
        
        self.frameDerecha = tk.Frame(self,borderwidth=1,relief="ridge",bg = 'steel blue')
        self.frameContenido = tk.Frame(self.frameDerecha,borderwidth=1,relief="ridge",bg = 'gray94')
        

        self.frameDatos=tk.Frame(self.frameContenido,borderwidth=1,relief="ridge",bg="gray94")
        self.frameDatos.rowconfigure(0,weight=0)
        self.frameDatos.rowconfigure(1,weight=1)
        self.frameDatos.columnconfigure(0,weight=1)
        self.frameResultados=tk.Frame(self.frameContenido,borderwidth=1,relief="ridge",bg="gray94")
        self.frameResultados.rowconfigure(0,weight=0)
        self.frameResultados.rowconfigure(1,weight=1)
        self.frameResultados.columnconfigure(0,weight=1)
        
        self.contenidoDatos=tk.Frame(self.frameDatos,bg="gray94")
        self.contenidoDatos.grid(column=0,row=1,sticky="NSEW")
        self.contenidoDatos.columnconfigure(0,weight=1)
        self.contenidoDatos.rowconfigure(0,weight=1,uniform="frmDatos")
        self.contenidoDatos.rowconfigure(1,weight=1,uniform="frmDatos")
        
        self.contenidoResultados=tk.Frame(self.frameResultados,bg="gray94")
        self.contenidoResultados.grid(column=0,row=1,sticky="NSEW")
        self.contenidoResultados.columnconfigure(0,weight=1)
        self.contenidoResultados.rowconfigure(0,weight=1)
        
        
        
        self.frameTablaDatos=tk.Frame(self.contenidoDatos,bg="gray94")
        self.frameGraficoDatos=tk.Frame(self.contenidoDatos,bg="gray94")
        
        
        self.frameTablaDatos.grid(column=0,row=0,sticky="NSEW")
        self.frameGraficoDatos.grid(column=0,row=1,sticky="NSEW")
        self.frameGraficoDatos.rowconfigure(0,weight=1)
        self.frameGraficoDatos.rowconfigure(1,weight=0)
        self.frameGraficoDatos.columnconfigure(0,weight=1)
        
        self.plotFigura=Figure(figsize=(2,2))
        
        self.canvasPlot=FigureCanvasTkAgg(self.plotFigura,master=self.frameGraficoDatos)
        self.canvasPlot.get_tk_widget().grid(column=0,row=0,sticky="NSEW")
        
        self.toolbarFrame = tk.Frame(master=self.frameGraficoDatos)
        self.toolbarFrame.grid(row=1,column=0)
        self.toolbar = NavigationToolbar2Tk(self.canvasPlot, self.toolbarFrame)
        
        self.subPlotFigura=self.plotFigura.add_subplot()
        
        
        

        
        
        # self.frameDatosTabla=tk.Frame(self.frameDerecha,bg="gray94")
        # self.frameDatosGraficas=tk.Frame(self.frameDerecha,bg="gray94")
        # self.frameResultadosGraficos=tk.Frame(self.frameDerecha,bg="gray94")
        # self.frameResultadosTabla=tk.Frame(self.frameDerecha,bg="gray94")

        self.frameIzquierda = tk.Frame(self,borderwidth=1,relief="ridge",bg = 'steel blue',padx=5,pady=5)

        self.estiloTabs = ttk.Style()
        self.estiloTabs.configure('TNotebook.Tab', font=('Arial','12','bold') )

        self.tabsDatos=tk.Frame(self.frameDatos,bg="gray94")
        self.contenidoResultado=tk.Frame(self.frameDatos,bg="gray94")
        
        
        self.btnTabsDatos1=tk.Button(self.tabsDatos,text="Irradiancia",command=self.plotIrradDatos)
        self.btnTabsDatos2=tk.Button(self.tabsDatos,text="Velocidad Viento",command=self.plotVelDatos)
        self.btnTabsDatos3=tk.Button(self.tabsDatos,text="Dirección Viento",command=self.plotDirDatos)
        self.btnTabsDatos4=tk.Button(self.tabsDatos,text="Temperatura",command=self.plotTempDatos)
        
        self.tabsDatos.grid(column=0,row=0,sticky="NEW")
        self.btnTabsDatos1.grid(column=0,row=0)
        self.btnTabsDatos2.grid(column=1,row=0)
        self.btnTabsDatos3.grid(column=2,row=0)
        self.btnTabsDatos4.grid(column=3,row=0)
        ######################################
        
        self.tabsResultados=tk.Frame(self.frameResultados,bg="gray94")
        self.contenidoResultado=tk.Frame(self.frameDatos,bg="gray94")
        
        self.btnTabsResultados1=tk.Button(self.tabsResultados,text="Tab 11",command=self.abrirmapa)
        self.btnTabsResultados2=tk.Button(self.tabsResultados,text="Tab 12",command=self.abrirmapa)
        self.btnTabsResultados3=tk.Button(self.tabsResultados,text="Tab 13",command=self.abrirmapa)
        self.btnTabsResultados4=tk.Button(self.tabsResultados,text="Tab 14",command=self.abrirmapa)
        
        self.tabsResultados.grid(column=0,row=0,sticky="NEW")
        self.btnTabsResultados1.grid(column=0,row=0)
        self.btnTabsResultados2.grid(column=1,row=0)
        self.btnTabsResultados3.grid(column=2,row=0)
        self.btnTabsResultados4.grid(column=3,row=0)
        
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

        self.btnAbrirMapa=tk.Button(self.frameIzquierda,text="Escoger Coordenadas\n en Mapa",command=self.abrirmapa)
        
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

        self.labelEscogerMetodo=tk.Label(self.frameIzquierda,text="Escoger Método\nde Evaluación: ",bg = 'steel blue',fg= 'white',font=('times', 10, 'bold'))

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


        self.labelRho=tk.Label(self.frameRho,text="Rho (ρ):",bg = 'steel blue',fg= 'white',font=('times', 8, 'bold'),anchor="e")
        self.labelAnguloInc=tk.Label(self.frameAnguloInc,text="Ángulo\nPanel:",bg = 'steel blue',fg= 'white',font=('times', 8, 'bold'),anchor="e")
        self.labelG=tk.Label(self.frameG,text="g (%/ºC):",bg = 'steel blue',fg= 'white',font=('times', 8, 'bold'),anchor="e")
        self.labelTONC=tk.Label(self.frameTONC,text="TONC:",bg = 'steel blue',fg= 'white',font=('times', 8, 'bold'),anchor="e")
        self.labelPmaxSTC=tk.Label(self.framePmaxSTC,text="Pmax STC:",bg = 'steel blue',fg= 'white',font=('times', 8, 'bold'),anchor="e")
        
        self.entryRho = tk.Entry(self.frameRho,width=10,textvariable=self.varRho)  

        self.entryAnguloInc = tk.Entry(self.frameAnguloInc,width=10,textvariable=self.varAnguloInc)  
        self.entryG = tk.Entry(self.frameG, width=10,textvariable=self.varG)  
        self.entryTONC = tk.Entry(self.frameTONC, width=10,textvariable=self.varTONC)  
        self.entryPmaxSTC = tk.Entry(self.framePmaxSTC, width=10,textvariable=self.varPmaxSTC)  

        self.labelRho.grid(column=0,row=0,sticky="EW",padx=2)  
        self.entryRho.grid(column=1,row=0,padx=2,sticky="EW")  
        self.frameRho.columnconfigure(0,weight=1,uniform="solar")
        self.frameRho.columnconfigure(1,weight=1,uniform="solar")
        self.frameRho.rowconfigure(0,weight=1)

        self.labelAnguloInc.grid(column=0,row=0,sticky="EW",padx=[2,0])  
        self.entryAnguloInc.grid(column=1,row=0,sticky="EW",padx=2)  
        self.frameAnguloInc.columnconfigure(0,weight=1,uniform="solar")
        self.frameAnguloInc.columnconfigure(1,weight=1,uniform="solar")
        self.frameAnguloInc.rowconfigure(0,weight=1)

        self.labelG.grid(column=0,row=0,sticky="EW",padx=[2,0])  
        self.entryG.grid(column=1,row=0,sticky="EW",padx=2)  
        self.frameG.columnconfigure(0,weight=1,uniform="solar")
        self.frameG.columnconfigure(1,weight=1,uniform="solar")
        self.frameG.rowconfigure(0,weight=1)

        self.labelTONC.grid(column=0,row=0,sticky="EW",padx=[2,0])  
        self.entryTONC.grid(column=1,row=0,sticky="EW",padx=2)  
        self.frameTONC.columnconfigure(0,weight=1,uniform="solar")
        self.frameTONC.columnconfigure(1,weight=1,uniform="solar")
        self.frameTONC.rowconfigure(0,weight=1)

        self.labelPmaxSTC.grid(column=0,row=0,sticky="EW",padx=[2,0])  
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

        self.frameIzquierda.grid(column=0,row=0,columnspan=2, sticky="NSEW")
        self.frameDerecha.grid(column=2,row=0,columnspan=8, sticky="NSEW")
        
        self.frameContenido.grid(column=0,row=1, sticky="NSEW")
        self.frameContenido.columnconfigure(0,weight=1,uniform="contenido")
        self.frameContenido.columnconfigure(1,weight=1,uniform="contenido")
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

        self.columnconfigure(0, weight=0,uniform="colsSelf")
        self.columnconfigure(1, weight=0,uniform="colsSelf")
        self.columnconfigure(2, weight=1,uniform="colsSelf")
        self.columnconfigure(3, weight=1,uniform="colsSelf")
        self.columnconfigure(4, weight=1,uniform="colsSelf")
        self.columnconfigure(5, weight=1,uniform="colsSelf")
        self.columnconfigure(6, weight=1,uniform="colsSelf")
        self.columnconfigure(7, weight=1,uniform="colsSelf")
        self.columnconfigure(8, weight=1,uniform="colsSelf")
        self.columnconfigure(9, weight=1,uniform="colsSelf")
        

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

        self.frameMapa = tk.Frame(self.ventanaMapa,borderwidth=1,relief="ridge",bg = 'steel blue')

        

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
        
        
        x=np.linspace(0,30,1000) 
        y=np.power(x,3)
        self.subPlotFigura.clear()
                            
        self.subPlotFigura.plot(x, y, label='Curva Aerogenerador')               # grafica los alores de (y) y de (x)
        self.subPlotFigura.set_title('(Potencia - Velocidad) del Aerogenerador', fontsize=16)
        self.subPlotFigura.set_ylabel('Potencia [W] ', fontsize=15)
        self.subPlotFigura.set_xlabel('Velocidad [m/s] ', fontsize=15)
        self.canvasPlot.draw()
        
        
    def plotIrradDatos(self):        
        self.subPlotFigura.clear()
        self.subPlotFigura.plot(self.INTER_irrad, label='Curva Aerogenerador')      
        self.subPlotFigura.set_title('Distribución Temporal "IRRADIANCIA"', fontsize=12)
        self.subPlotFigura.set_ylabel('Irradiancia [W/m^2]', fontsize=12)
        self.subPlotFigura.set_xlabel(self.varAnio.get(), fontsize=12)
        fmt = mdates.DateFormatter('%d-%b')
        self.subPlotFigura.xaxis.set_major_formatter(fmt)
        self.plotFigura.subplots_adjust(bottom=0.2)
        
        
        self.canvasPlot.draw()
        
    def plotVelDatos(self):
        self.subPlotFigura.clear()
        self.subPlotFigura.plot(self.INTER_vel, label='Curva Aerogenerador')     
        self.subPlotFigura.set_title('Distribución Temporal "Velocidad del Viento"', fontsize=12)
        self.subPlotFigura.set_ylabel('Velocidad del Viento [m/s]', fontsize=12) 
        self.subPlotFigura.set_xlabel(self.varAnio.get(), fontsize=12)
        fmt = mdates.DateFormatter('%d-%b')
        self.subPlotFigura.xaxis.set_major_formatter(fmt)
        self.plotFigura.subplots_adjust(bottom=0.2)
        
        
        self.canvasPlot.draw()
    def plotDirDatos(self):
        self.subPlotFigura.clear()
        self.subPlotFigura.plot(self.INTER_direc, label='Curva Aerogenerador')      
        self.subPlotFigura.set_title('Distribución Temporal "Dirección del Viento"', fontsize=12)
        self.subPlotFigura.set_ylabel('Dirección del Viento [°]', fontsize=12)
        self.subPlotFigura.set_xlabel(self.varAnio.get(), fontsize=12)
        fmt = mdates.DateFormatter('%d-%b')
        self.subPlotFigura.xaxis.set_major_formatter(fmt)
        self.plotFigura.subplots_adjust(bottom=0.2)
        
        
        self.canvasPlot.draw()
    def plotTempDatos(self):
        self.subPlotFigura.clear()
        self.subPlotFigura.plot(self.INTER_temp, label='Curva Aerogenerador')      
        self.subPlotFigura.set_title('Distribución Temporal "Temperatura"', fontsize=12)
        self.subPlotFigura.set_ylabel('Temperatura [°C]', fontsize=12)
        self.subPlotFigura.set_xlabel(self.varAnio.get(), fontsize=12)
        fmt = mdates.DateFormatter('%d-%b')
        self.subPlotFigura.xaxis.set_major_formatter(fmt)
        self.plotFigura.subplots_adjust(bottom=0.2)
        
        
        self.canvasPlot.draw()
    
    
    #####################################################################################################################
    ###########################################     Metodos Globales    #################################################
    def cargarNREL(self):
        lat, lon, year = -3.99, -79.26, 2019
        # self.lat
        # self.lng
        # self.anio
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
        
        url = 'https://developer.nrel.gov/api/nsrdb/v2/solar/psm3-download.csv?api_key=WT0MS4JUkh59reR6YxisV0WpybhCyfjhzTrGexNO&full_name=Juan+Cisneros&email=juan.cisneros@epn.edu.ec&affiliation=National+Polytechnic+School&reason=Thesis+research&mailing_list=true&wkt=POINT({lng}+{lat})&names={anio}&attributes=dhi,dni,ghi,clearsky_dhi,clearsky_dni,clearsky_ghi,cloud_type,dew_point,air_temperature,surface_pressure,relative_humidity,solar_zenith_angle,total_precipitable_water,wind_direction,wind_speed,fill_flag&leap_day=false&utc=false&interval=60'.format(anio=self.varAnio.get(), lat=self.lat, lng=self.lng)

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
            df = df.set_index(pd.date_range('1/1/{yr}'.format(yr=self.varAnio.get()), freq=interval+'Min', periods=525600/int(interval)))
            df=df.filter(items=['Wind Speed','Relative Humidity','Temperature','GHI','Wind Direction'])
            #df['Fecha']=df.index
            
            
            self.labelEscogerMetodo.grid(column=0,row=11,sticky="NEW",pady=2)
            self.comboMetodos.grid(column=0,row=12,sticky="NEW",pady=2)
            
            self.bdd_float=df
            print(self.bdd_float)
            
            self.L=self.lat
                        
            self.n, self.fechas, self.fecha_ini, self.f = self.fechas_horas(self.bdd_float)        # Valores que retorna la funcion
            
            #-----------------seno, coseno y tangente de L (latitud)---------------------
            self.cos_L=math.cos(self.L* math.pi/180)                           # se aplica la formula para calcular coseno de latitud
            self.sin_L=math.sin(self.L* math.pi/180)                           # se aplica la formula para calcular seno de latitud
            self.tan_L=math.tan(self.L* math.pi/180)                           # se aplica la formula para calcular tangente de latitud
            #----------------declaro el angulo de inclinacion del panel------------------
            self.E=25                                                     # Tanto para Masters como para Tiwari
            self.cos_E=math.cos(self.E* math.pi/180)                           # se aplica la formula para calcular coseno de inclinacion de panel
            self.sin_E=math.sin(self.E* math.pi/180) 
            self.L_E=self.L-self.E  
            self.tan_LE= math.tan(self.L_E*math.pi/180)                        # se aplica la formula para calcular tangente de resta de angulos de panel  
            self.cos_LE= math.cos(self.L_E*math.pi/180)                        # se aplica la formula para calcular coseno de resta de angulos de panel 
            self.sin_LE= math.sin(self.L_E*math.pi/180)                        # se aplica la formula para calcular seno de resta de angulos de panel 
            #----------------factores de conversion de plano inclinado-------------------
            self.Rd = (1+self.cos_E)/2                                         # Factor de conversion de radiacion difusa Rd
            self.Rr = (1-self.cos_E)/2                                         # Factor de conversion de radiacion reflejada Rr
            self.Ro = 0.2                                                 # Coeficiente de reflexion para suelo ordinario  
            #--------------------DEFINICION DE ORIENTACION DEL PANEL---------------------
            if self.L > 0:                                                # Condicion para escoger el ángulo acimut de orientacion del panel (PARA TIWARI)
                self.GAMA =  0                                            # si el panel esta en el hemisferio norte
            else:
                self.GAMA = 180                                           # si el panel esta en el hemisferio sur
            self.GAMA_rad= math.radians(self.GAMA)                             # transformacion de grados a radianes
            self.cos_GAMA=math.cos(self.GAMA_rad)                              # coseno de angulo acimutal GAMA
            self.sin_GAMA=math.sin(self.GAMA_rad)      

            
            self.ang, self.ang_concat, self.cos_d, self.sin_d, self.cos_H, self.sin_H, self.co_H, self.bet, self.aci, self.BETA, self.sin_Hsr, self.num_dia, self.sin_Hsrc = self.angulos(self.n)    # Valores que retorna la funcion
            
            self.bdd_inter = self.interpolacion_bdd(self.bdd_float)
            
            
            self.BDD_irad, self.BDD_vel_v, self.BDD_direc_v, self.BDD_temp = self.BDD_independientes (self.bdd_float)  # Valores que retorna la funcion

            self.INTER_irrad, self.INTER_vel, self.INTER_direc, self.INTER_temp = self.INTER_independientes (self.bdd_inter) 
            
            
            print("**********************************************************************************")
            print("**********************  bdd_inter  ************************")
            print(self.bdd_inter)
            
            self.bdd_float['Fecha']=self.bdd_float.index
            cols = list(self.bdd_float.columns)
            cols = [cols[-1]] + cols[:-1]
            self.bdd_float=self.bdd_float[cols]
            
            
            
            self.L=self.lng
            
            self.tablaDatos=Table(self.frameTablaDatos,dataframe=self.bdd_float,showtoolbar=False,
            showstatusbar=True,
            editable=False)
            self.tablaDatos.contractColumns()
            self.tablaDatos.show()
            
            self.plotIrradDatos()
            #self.pt1=Table()
        except Exception as e:
            print(e)
            messagebox.showinfo(message="No existen datos para la coordenada seleccionada", title="Error")

    def fechas_horas (self,bdd_float):
        #-------------------Adquiere las fechas del DataTime---------------------
        print("/////////////////////////////////")
        print(bdd_float)
        fechas=bdd_float.index                               # adquiere todas las dechas del DataFrame bdd_float
        print(fechas)
        
        f_inicio=fechas[0]                                   # adquiere la fecha en la que inicio la toma de datos variable type TimeStamp
        fecha_ini=str(f_inicio)                              # fecha inicial se pasa a tipo str
        #f_fin=fechas[-1]                                    # adquiere la fecha en la que finalizo la toma de datos variable type TimeStamp
        #----se extrae el numero de dia "n" para las formulas de declinacion----
        f=fechas.to_frame()                                  # Se crea una variable que contenga las fechas de la base de datos pero en formato DataFrame  

        f=f.rename(columns={ f.columns[0]: "Fecha" })

        f['n_dia'] = f.Fecha.dt.strftime('%j')               # Se cre una columna con nombre n_dia que adquiere el numero de dia del año de la columna Fecha, a traves de (.dt.strftime('%j'))

        f['N hora'] = f.Fecha.dt.strftime('%H')              # Se cre una columna con nombre hora que adquiere el numero de horas del dia de la columna Fecha, a traves de (.dt.strftime('%H'))
        f['N minutos'] = f.Fecha.dt.strftime('%M')           # Se cre una columna con nombre minutos que adquiere los minutos del dia de la columna Fecha, a traves de (.dt.strftime('%M'))
        #-----------------------------HORAS DEL DIA-----------------------------
        n=f.drop(['Fecha'],axis=1)                           # se elimina la columna Fecha 
        col=['n_dia','N hora', 'N minutos']                  # se enlista el nombre de las nuevas columnas
        n[col]=n[col].apply(pd.to_numeric, errors='coerce', axis=1) # se transforma a formato numerico las columnas que se introducen anteriormente
        #n=n.resample('D').mean()                            # se saca el numero del dia de todas las mediciones diarias
        n['N minutos'] = n['N minutos']/60                   # se divide para 60 la columna de los minutos para poder sumar las horas en fracciones
        n['Horas dia'] = n['N hora'] + n['N minutos']        # se suma las horas los minutos en fracciones en la nueva columna de nombre'Horas dia'
        
        return n,fechas, fecha_ini , f                     # Valores que retorna la funcion

    def angulos (self,n):
        #---------------------- Se calcula la declinacion-----------------------
        ang=lambda x : 23.45*math.sin(((360/365)*(x-81)* math.pi)/180)      # se aplica la formula para calcular la declinacion
        delta=n['n_dia'].apply(ang).to_frame()                              # la formula devuelve un tipo series, por lo tanto se transforma a frame
        delta.columns=['Declinación (δ°)']                                  # se cambia el nombre de la columna
        #----------------horas del dia (H) antes del medio dia------------------
        ang_concat=pd.concat([n,delta], axis=1)                                # se concatena todos los valores calculados
        ang_concat=ang_concat.drop(['N hora','N minutos'],axis=1)              # se elimina las columnas 'N minutos','N minutos'
        ang_concat['H antes del medio dia'] = 12+ang_concat['Horas dia']*-1    # se determina las horas antes del medio dia 
        ang_concat['∡ horario (H°)'] = ang_concat['H antes del medio dia']*15  # se determina el angulo horario H
        #------------------------ Se calcula COSENO (H) ------------------------
        co_H=ang_concat.filter(items=['∡ horario (H°)'])                    # se filtra la columna deseada
        coseno_H=lambda co_H : math.cos(co_H* math.pi/180)                  # se aplica la formula para calcular coseno de H de la columna filtrada
        cos_H=ang_concat['∡ horario (H°)'].apply(coseno_H).to_frame()       # la formula devuelve un tipo series, por lo tanto se transforma a frame
        cos_H.columns=['coseno (H°)']                                       # se cambia el nombre de la columna
        #-------------------------- Se calcula SENO (H) ------------------------
        seno_H=lambda co_H : math.sin(co_H* math.pi/180)                    # se aplica la formula para calcular coseno de H de la columna filtrada
        sin_H=ang_concat['∡ horario (H°)'].apply(seno_H).to_frame()         # la formula devuelve un tipo series, por lo tanto se transforma a frame
        sin_H.columns=['seno (H°)']                                         # se cambia el nombre de la columna
        #----------------------- Se calcula coseno (δ°) ------------------------
        coseno_d=lambda delta : math.cos(delta* math.pi/180)                # se aplica la formula para calcular coseno de delta
        cos_d=ang_concat['Declinación (δ°)'].apply(coseno_d).to_frame()     # la formula devuelve un tipo series, por lo tanto se transforma a frame
        cos_d.columns=['coseno (δ°)']                                       # se cambia el nombre de la columna
        #------------------------ Se calcula SENO (δ°) -------------------------
        seno_d=lambda delta : math.sin(delta* math.pi/180)                  # se aplica la formula para calcular seno de delta
        sin_d=ang_concat['Declinación (δ°)'].apply(seno_d).to_frame()       # la formula devuelve un tipo series, por lo tanto se transforma a frame
        sin_d.columns=['seno (δ°)']                                         # se cambia el nombre de la columna
        #------------------------- Se calcula TAN (δ°) -------------------------
        tangente_d=lambda delta : math.tan(delta* math.pi/180)              # se aplica la formula para calcular tangente de delta
        tan_d=ang_concat['Declinación (δ°)'].apply(tangente_d).to_frame()   # la formula devuelve un tipo series, por lo tanto se transforma a frame
        tan_d.columns=['tan (δ°)']                                          # se cambia el nombre de la columna
        #----------H_SR ángulo horario de salida del sol (en radianes)---------- 
        H_amanecer=lambda tan_d : math.acos(-self.tan_L*tan_d* math.pi/180)      # se aplica la formula para calcular angulo H_SR°
        H_SR=ang_concat['Declinación (δ°)'].apply(H_amanecer).to_frame()    # la formula devuelve un tipo series, por lo tanto se transforma a frame
        H_SR.columns=['H_SR (Radianes)']                                    # se cambia el nombre de la columna 
        H_SR['(H_SR°)'] = H_SR['H_SR (Radianes)']*180/math.pi               # se transforma de radianes a grados la columna 'Radianes (H_SR)'
        ang_concat=pd.concat([ang_concat,cos_H,sin_H,cos_d, sin_d, tan_d,H_SR], axis=1)   # se concatena todos los valores calculados
        #-------------seno H_SR ángulo horario de salida del sol ---------------
        sin_Hsr=ang_concat.filter(items=['H_SR (Radianes)'])  
        seno_HSR =lambda sin_Hsr : math.sin(sin_Hsr)                        # se aplica la formula para calcular angulo H_SR°
        sin_H_SR=ang_concat['H_SR (Radianes)'].apply(seno_HSR).to_frame()   # la formula devuelve un tipo series, por lo tanto se transforma a frame
        sin_H_SR.columns=['seno (H_SR)']                                    # se cambia el nombre de la columna 
        ang_concat=pd.concat([ang_concat,sin_H_SR], axis=1)                 # se concatena todos los valores calculados
        #----------------------------SENO de (β°)-------------------------------  
        ang_concat['seno (β°)'] = ang_concat['coseno (δ°)']*ang_concat['coseno (H°)']*self.cos_L + self.sin_L*ang_concat['seno (δ°)'] # se calcula el seno(β°)
        #------------- Se calcula la altitud β (A cualquier hora)---------------  
        bet=ang_concat.filter(items=['seno (β°)'])                          # saca los valores de la columna a ser calculada posteriormente
        beta_H=lambda bet : math.asin(bet)                                  # se aplica la formula para calcular seno de β
        B_H=ang_concat['seno (β°)'].apply(beta_H).to_frame()                # la formula devuelve un tipo series, por lo tanto se transforma a frame
        B_H.columns=['Beta (β°)']                                           # se cambia el nombre de la columna
        B_H['Beta (β°)'] = B_H['Beta (β°)']* 180/math.pi                    # se transforma a grados el angulo β
        ang_concat=pd.concat([ang_concat, B_H], axis=1)                     # se concatena la nueva columna calculada al dataframe anterior
        #-----------------------COSENO β (A cualquier hora)---------------------  
        BETA=ang_concat.filter(items=['Beta (β°)'])                         # saca los valores de la columna a ser calculada posteriormente
        beta_B=lambda BETA : math.cos(BETA* math.pi/180)                    # se aplica la formula para calcular seno de β
        BET=ang_concat['Beta (β°)'].apply(beta_B).to_frame()                # la formula devuelve un tipo series, por lo tanto se transforma a frame
        BET.columns=['cos (β°)']                                            # se cambia el nombre de la columna
        ang_concat=pd.concat([ang_concat, BET], axis=1)                     # se concatena la nueva columna calculada al dataframe anterior
        #--------Insolación extraterrestre media diaria Io (kWh/m^2-día)--------  
        num_dia=ang_concat.filter(items=['n_dia'])                          # saca los valores de la columna a ser calculada posteriormente
        I_ex=lambda num_dia : math.cos(((num_dia*360)/365)* math.pi/180)    # se aplica la formula para calcular auxiliar de formula
        Io_aux=ang_concat['n_dia'].apply(I_ex).to_frame()                   # la formula devuelve un tipo series, por lo tanto se transforma a frame
        Io_aux.columns=['Aux_ndia']                                         # se cambia el nombre de la columna
        #Io_aux['Aux_ndia'] = Io_aux['Aux_ndia']* 180/math.pi               # se transforma a grados el angulo β
        ang_concat=pd.concat([ang_concat, Io_aux], axis=1)                  # se concatena la nueva columna calculada al dataframe anterior
        SC=1.37                                                            # kW/m^2 constante solar SC=1.377 kW/m^2,   puede ser SC=1.367 kWh/m^2
        ang_concat['Io (kWh/m^2)'] = (24/math.pi)*SC*(1+0.034*ang_concat['Aux_ndia'] )*(self.cos_L*ang_concat['coseno (δ°)']*ang_concat['seno (H_SR)']+ ang_concat['H_SR (Radianes)']* self.sin_L*ang_concat['seno (δ°)'] )   # se calcula el Io(kW/m^2)
        #---------------------Ángulo de acimut solar (Φs)---------------------- 
        ang_concat['seno (Φs)'] = ang_concat['coseno (δ°)']*ang_concat['seno (H°)']/ang_concat['cos (β°)'] # se calcula el seno (Φs)
        aci=ang_concat.filter(items=['seno (Φs)'])                          # saca los valores de la columna a ser calculada posteriormente
        acimu=lambda aci : math.asin(aci)                                   # se aplica la formula para calcular arcseno (Φs)
        acimut_s = ang_concat['seno (Φs)'].apply(acimu).to_frame()          # la formula devuelve un tipo series, por lo tanto se transforma a frame
        acimut_s.columns = ['(Φs1)']                                        # se cambia el nombre de la columna
        acimut_s['(Φs1)'] = acimut_s['(Φs1)']* 180/math.pi                  # se transforma a grados el angulo Φs1
        ang_concat = pd.concat([ang_concat, acimut_s], axis=1)              # se concatena la nueva columna calculada al dataframe anterior
        ang_concat['(Φs2)'] = 180 - (ang_concat['(Φs1)'])                   # se aumenta una nueva columna (Φs2), ya que el seno del acimut es ambiguo
        #------------------------Relacion tg(δ) / tg(L) ----------------------- 
        ang_concat['tg(δ)/tg(L)'] = ang_concat['tan (δ°)']/self.tan_L            # se calcula el relacion tg(δ)/tg(L)
        #------------------------filtrar columnas (Φs)------------------------- 
        ang_concat['Φs'] = np.where(ang_concat['coseno (H°)']>= ang_concat['tg(δ)/tg(L)'], ang_concat['(Φs1)'], ang_concat['(Φs2)'] )  # creacion de una columna 'Φs' para rellenar con nuevos valores bajo las condiciones de la ambiguedaddel seno
        #--------H_SRC ángulo horario; salida del sol (PARA EL COLECTOR)------- 
        H_amanecer_c=lambda tan_d : math.acos(-self.tan_LE*tan_d* math.pi/180)    # se aplica la formula para calcular angulo H_SRC°
        H_SRC=ang_concat['Declinación (δ°)'].apply(H_amanecer_c).to_frame()  # la formula devuelve un tipo series, por lo tanto se transforma a frame
        H_SRC.columns=['H_SRC (Radianes)']                                   # se cambia el nombre de la columna 
        H_SRC['(H_SRC°)'] = H_SRC['H_SRC (Radianes)']*180/math.pi            # se transforma de radianes a grados la columna 'Radianes (H_SRC)'
        ang_concat=pd.concat([ang_concat, H_SRC], axis=1)                    # se concatena todos los valores calculados
        #-------------------H_SRC mínimo (PARA EL COLECTOR)---------------------
        ang_concat['H_SRC min'] = np.where(ang_concat['H_SR (Radianes)'] < ang_concat['H_SRC (Radianes)'] , ang_concat['H_SR (Radianes)'], ang_concat['H_SRC (Radianes)'])        # creacion de una columna 'H_SRC min' para rellenar con las condiciones de H_SRC (mínimo)
        #------------seno H_SRC ángulo horario de salida del sol ---------------
        sin_Hsrc=ang_concat.filter(items=['H_SRC min'])                      # filtra los valores de la columna a ser calculada posteriormente
        seno_HSRC =lambda sin_Hsrc : math.sin(sin_Hsrc)                      # se aplica la formula para calcular angulo H_SR°
        sin_H_SRC=ang_concat['H_SRC min'].apply(seno_HSRC).to_frame()        # la formula devuelve un tipo series, por lo tanto se transforma a frame
        sin_H_SRC.columns=['seno (H_SRC)']                                   # se cambia el nombre de la columna 
        ang_concat=pd.concat([ang_concat,sin_H_SRC], axis=1)                 # se concatena todos los valores calculados
        #---------FACTORES DE CONVERSION SOBRE UNA SUPERFICIE INCLINADA---------
        ang_concat['Rb'] = (self.cos_LE*ang_concat['coseno (δ°)']*ang_concat['seno (H_SRC)'] + ang_concat['H_SRC min']*self.sin_LE*ang_concat['seno (δ°)'])/(self.cos_L*ang_concat['coseno (δ°)']*ang_concat['seno (H_SR)'] + ang_concat['H_SR (Radianes)']*self.sin_L*ang_concat['seno (δ°)']) # Factor de conversion de radiacion de haz Rb
        
        return ang, ang_concat, cos_d, sin_d, cos_H, sin_H, co_H, bet, aci, BETA, sin_Hsr, num_dia, sin_Hsrc      # Valores que retorna la funcion

    def interpolacion_bdd (self,bdd_float):
        bdd_float[bdd_float < 0] = 0                            # se elimina los valores negativos de la primera base de datos 
        sin_nan=bdd_float.interpolate(method='akima', order=3)  # otros metodos spline, polynomial, linear, ojo revisar: CubicSpline
        bdd_inter=sin_nan.fillna(method='ffill')                # completa los valores en la ultima posicion de las columnas debido a que el metodo solo realiza interpolacion, no resuelve extrapolación
        bdd_inter=bdd_inter.fillna(method='bfill')              # completa los valores en la posicion inicial de las columnas debido a que el metodo solo realiza interpolacion, no resuelve extrapolación
        bdd_inter[bdd_inter < 0] = 0                            # se elimina valores negativos nuevamente debido a que los metodos de interpolacion pueden entregar valores negativos en el proceso
        
        return bdd_inter                                        # Valores que retorna la funcion

    def BDD_independientes (self,bdd_float):
        BDD_irad = bdd_float.filter(items=['GHI'])               # se filtran las columnas individuales de la bdd_float
        BDD_vel_v = bdd_float.filter(items=['Wind Speed'])       # se filtran las columnas individuales de la bdd_float
        BDD_direc_v = bdd_float.filter(items=['Wind Direction']) # se filtran las columnas individuales de la bdd_float
        BDD_temp = bdd_float.filter(items=['Temperature'])       # se filtran las columnas individuales de la bdd_float
    
        return BDD_irad, BDD_vel_v, BDD_direc_v, BDD_temp               # Valores que retorna la funcion

    #----------------FUNCIONES INDEPENDIENTES BDD INTERPOLADA-------------------

    def INTER_independientes (self,bdd_inter):
        INTER_irrad = bdd_inter.filter(items=['GHI'])                   # se filtran las columnas individuales de la bdd_inter
        INTER_vel = bdd_inter.filter(items=['Wind Speed'])              # se filtran las columnas individuales de la bdd_inter
        INTER_direc = bdd_inter.filter(items=['Wind Direction'])        # se filtran las columnas individuales de la bdd_inter
        INTER_temp = bdd_inter.filter(items=['Temperature'])            # se filtran las columnas individuales de la bdd_inter
        
        return INTER_irrad, INTER_vel, INTER_direc, INTER_temp                # Valores que retorna la funcion

     # Valores que retorna la funcion

    
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
        self.configure(bg="steel blue")

        self.entrada_usuario = tk.StringVar()

        L_1 = tk.Label(self, text="MI FIRST FRAME WITH OOP AND TKINTER", font=(
            "Times New Roman", 14, "bold"), bg="steel blue", fg="blue")
        L_1.grid(row=0, column=0, columnspan=4, sticky="n")
        L_2 = tk.Label(self, text="Entry name: ", font=(
            "Times New Roman", 12), bg="steel blue")
        L_2.grid(row=1, column=0, sticky="w")

        self.E_1 = ttk.Entry(self, textvariable=self.entrada_usuario)
        self.E_1.focus()
        self.E_1.grid(row=1, column=1, columnspan=2, padx=(0, 10))

        B_1 = ttk.Button(self, text="SAY HI", command=self.saludarme)
        B_1.grid(row=1, column=3, sticky="e")

        self.L_3 = tk.Label(self, textvariable="", font=(
            "Times New Roman", 12, "bold"), bg="steel blue")
        self.L_3.grid(row=2, column=0, columnspan=4, sticky="nsew")

        B_2 = ttk.Button(self, text="espannol",
                         command=lambda: controller.show_frame(Frame_1))
        B_2.grid(row=3, column=0)

    def saludarme(self, *args):
        self.L_3.configure(text="Good Morning, {}.".format(
            self.entrada_usuario.get()))


root = APP()


root.mainloop()
