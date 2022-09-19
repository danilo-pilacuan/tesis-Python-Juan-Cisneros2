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

        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry("%dx%d+0+0" % (w, h))
        self.state('zoomed')
        #self.geometry("980x690")
        #self.minsize(1020, 630)

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
        self.contenidoDatos.rowconfigure(0,weight=6,uniform="frmDatos")
        self.contenidoDatos.rowconfigure(1,weight=4,uniform="frmDatos")
        
        self.contenidoResultados=tk.Frame(self.frameResultados,bg="gray94")
        self.contenidoResultados.grid(column=0,row=1,sticky="NSEW")
        self.contenidoResultados.columnconfigure(0,weight=1)
        self.contenidoResultados.rowconfigure(0,weight=6,uniform="frmResultados")
        self.contenidoResultados.rowconfigure(1,weight=4,uniform="frmResultados")
        self.frameTablaResultados=tk.Frame(self.contenidoResultados,bg="red")       #@todo self.frameTablaResultados
        
        self.frameTablaResultados.grid(column=0,row=1,sticky="NSEW")
        
        
        
        
        self.frameTablaDatos=tk.Frame(self.contenidoDatos,bg="gray94")
        self.frameGraficoDatos=tk.Frame(self.contenidoDatos,bg="gray94")
        
        
        self.frameTablaDatos.grid(column=0,row=1,sticky="NSEW")
        self.frameGraficoDatos.grid(column=0,row=0,sticky="NSEW")
        self.frameGraficoDatos.rowconfigure(0,weight=1)
        self.frameGraficoDatos.rowconfigure(1,weight=0)
        self.frameGraficoDatos.columnconfigure(0,weight=1)
        
        self.plotFiguraDatos=Figure(figsize=(2,2))
        
        self.canvasPlotDatos=FigureCanvasTkAgg(self.plotFiguraDatos,master=self.frameGraficoDatos)
        self.canvasPlotDatos.get_tk_widget().grid(column=0,row=0,sticky="NSEW")
        
        self.toolbarFrameDatos = tk.Frame(master=self.frameGraficoDatos)
        self.toolbarFrameDatos.grid(row=1,column=0)
        self.toolbarDatos = NavigationToolbar2Tk(self.canvasPlotDatos, self.toolbarFrameDatos)
        
        self.subPlotFiguraDatos=self.plotFiguraDatos.add_subplot()
        
        
        self.frameGraficoResultados=tk.Frame(self.contenidoResultados,bg="gray94")
        self.frameGraficoResultados.grid(column=0,row=0,sticky="NSEW")
        self.frameGraficoResultados.rowconfigure(0,weight=1)
        self.frameGraficoResultados.columnconfigure(0,weight=1)
        
        self.plotFiguraResultados=Figure(figsize=(2,2))
        
        self.canvasPlotResultados=FigureCanvasTkAgg(self.plotFiguraResultados,master=self.frameGraficoResultados)
        self.canvasPlotResultados.get_tk_widget().grid(column=0,row=0,sticky="NSEW")
        
        self.toolbarFrameResultados = tk.Frame(master=self.frameGraficoResultados)
        self.toolbarFrameResultados.grid(row=1,column=0)
        self.toolbarResultados = NavigationToolbar2Tk(self.canvasPlotResultados, self.toolbarFrameResultados)
        
        self.subPlotFiguraResultados=self.plotFiguraResultados.add_subplot()
        
        
        
        
        

        
        
        # self.frameDatosTabla=tk.Frame(self.frameDerecha,bg="gray94")
        # self.frameDatosGraficas=tk.Frame(self.frameDerecha,bg="gray94")
        # self.frameResultadosGraficos=tk.Frame(self.frameDerecha,bg="gray94")
        # self.frameResultadosTabla=tk.Frame(self.frameDerecha,bg="gray94")

        self.frameIzquierda = tk.Frame(self,borderwidth=1,relief="ridge",bg = 'steel blue',padx=5,pady=5)

        self.estiloTabs = ttk.Style()
        self.estiloTabs.configure('TNotebook.Tab', font=('Arial','12','bold') )

        self.tabsDatos=tk.Frame(self.frameDatos,bg="gray94")
        self.tabsDatos.grid(column=0,row=0,sticky="NEW")
        
        self.contenidoResultado=tk.Frame(self.frameDatos,bg="gray94")
        
        self.btnTabsDatosAux=tk.Button(self.tabsDatos,text="Datos")
        
        
        
        self.btnTabsDatosAux.grid(column=0,row=0)
        ######################################
        
        self.tabsResultados=tk.Frame(self.frameResultados,bg="gray94")
        self.contenidoResultado=tk.Frame(self.frameResultados,bg="gray94")
        
        self.btnTabsResultadosAux=tk.Button(self.tabsResultados,text="Resultados")
        # self.btnTabsResultados2=tk.Button(self.tabsResultados,text="Tab 12",command=self.abrirmapa)
        # self.btnTabsResultados3=tk.Button(self.tabsResultados,text="Tab 13",command=self.abrirmapa)
        # self.btnTabsResultados4=tk.Button(self.tabsResultados,text="Tab 14",command=self.abrirmapa)
        
        self.tabsResultados.grid(column=0,row=0,sticky="NSEW")
        self.btnTabsResultadosAux.grid(column=0,row=0)
        
        
        # self.btnTabsResultados2.grid(column=1,row=0)
        # self.btnTabsResultados3.grid(column=2,row=0)
        # self.btnTabsResultados4.grid(column=3,row=0)
        
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
        
        # self.plotFiguraDatos=Figure(figsize=(2,2))
        # self.subPlotFiguraDatos=self.plotFiguraDatos.add_subplot()
        # self.canvasPlotDatos=FigureCanvasTkAgg(self.plotFiguraDatos,master=self.frameTab1)
        # self.canvasPlotDatos.get_tk_widget().grid(column=0,row=1,sticky="NSEW")
        
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
        
        
        ########################### seccion Tabs #############################
        
        self.frameTabsMastersNREL=tk.Frame(self.tabsResultados)
        #self.frameTabsMastersNREL.grid(column=0,row=0)
        
        self.btnTabsMastersNREL1=tk.Button(self.frameTabsMastersNREL,text="Sup. Horizontal",command=self.plotEnergiaMensualSupH)
        self.btnTabsMastersNREL2=tk.Button(self.frameTabsMastersNREL,text="Sup. Inclinada",command=self.plotEnergiaMensualSupInc)
        self.btnTabsMastersNREL3=tk.Button(self.frameTabsMastersNREL,text="Seguidor 1 Eje",command=self.plotEnergiaMensual1Eje)
        self.btnTabsMastersNREL4=tk.Button(self.frameTabsMastersNREL,text="Seguidor 2 Ejes",command=self.plotEnergiaMensual2Ejes)
        self.btnTabsMastersNREL5=tk.Button(self.frameTabsMastersNREL,text="Comparación Mensual",command=self.plotComparacionMensualMasters)
        
        self.btnTabsMastersNREL1.grid(column=0,row=0)
        self.btnTabsMastersNREL2.grid(column=1,row=0)
        self.btnTabsMastersNREL3.grid(column=2,row=0)
        self.btnTabsMastersNREL4.grid(column=3,row=0)
        self.btnTabsMastersNREL5.grid(column=4,row=0)
        
        
        
        #self.btnTabsResultadosAux.grid_forget()
        #self.frameTabsMastersNREL.grid_forget()
        
        self.frameTabsTiwariNREL=tk.Frame(self.tabsResultados)
        #self.frameTabsTiwariNREL.grid(column=0,row=0)
        
        self.btnTabsTiwariNREL1=tk.Button(self.frameTabsTiwariNREL,text="Sup. Horizontal",command=self.plotEnergiaMensualSupHTiwari)
        self.btnTabsTiwariNREL2=tk.Button(self.frameTabsTiwariNREL,text="Sup. Inclinada",command=self.plotEnergiaMensualSupInc)
        self.btnTabsTiwariNREL3=tk.Button(self.frameTabsTiwariNREL,text="Comparación Mensual",command=self.plotEnergiaMensual1Eje)
        
        self.btnTabsTiwariNREL1.grid(column=0,row=0)
        self.btnTabsTiwariNREL2.grid(column=1,row=0)
        self.btnTabsTiwariNREL3.grid(column=2,row=0)
        
        
        
        ####################### Fin seccion Tabs ##################################       

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
        
        
#########################################################################################################################################################################
#########################################################################################################################################################################
    def obtenerDatosGlobal(self):
        
        self.INTER_spl_irrad, self.INTER_spl_vel, self.INTER_spl_temp  = self.spl_de_INTER (self.INTER_irrad, self.INTER_vel, self.INTER_temp)          
        
        self.q = self.numero_dias (self.num_dia) 
        self.Temp_prom_dia, self.Temp_prom_mes = self.temp_promedio ()
        ############################ extrae coseno (δ°)############################
        self.cos_d_hora = self.ang_concat.filter(items=['coseno (δ°)'])
        self.cos_d_dia = self.cos_d_hora.resample('D').mean()
        self.cos_d_mes = self.cos_d_hora.resample('M').mean()
        ############################ extrae coseno (δ°)############################
        self.d_hora = self.ang_concat.filter(items=['Declinación (δ°)'])
        self.d_dia = self.d_hora.resample('D').mean()
        self.d_mes = self.d_hora.resample('M').mean()
        
        self.beta_m, self.bet_prom = self.beta_promedio () 
        
        self.B_hora = self.beta_m.filter(items=['Prom (β°)'])
        self.B_dia = self.B_hora.resample('D').mean()
        self.B_mes = self.B_hora.resample('M').mean()
        
        self.GHI_diario, self.kT_diario, self.kT_mensual, self.Rb_m  = self.kt_bdd_masters ()
        
        self.Ic_incli = self.ener_Ic ()
        self.Energ_IC_anio = self.Ic_incli.resample('Y').sum()
        self.Energ_IC_mes = self.Ic_incli.resample('M').sum()
        
        
            
        
        
        self.potenc_INTER_SPLINE = self.INTER_spl_temp.Temperatura.astype(object).combine(self.INTER_spl_irrad.GHI , func=self.Potencia)
        
        
        self.potenc_INTER_SPLINE = self.potenc_INTER_SPLINE.to_frame()
        self.potenc_INTER_SPLINE.columns = ['Energia [Wh]']                                 # cambio el nombre de la columna
        self.ener_panel_spl = self.potenc_INTER_SPLINE.resample('D').apply(integrate.trapz, dx=1/4) #realiza la integracion diaria de la energia;   dx=1/4 porque la integracion por defecto es de 1 unidad (hora), como tenemos una frecuencia de 15T, se debe especificar que la hora la dividimos en 4 partes de 15 minutos
        
        
        self.ener_panel_spl['Energia [Wh]'] = self.ener_panel_spl['Energia [Wh]']/1000            # paso a kWh/m^2-dia   
        self.ener_panel_spl.columns=['Energia [kWh]']                                        # se cambia el nombre de la columna
        
        
        #suma_spline = self.ener_panel_spl.sum()
        self.ener_suma_año = self.ener_panel_spl.resample('Y').sum()                                             # Energia total producida en el año
        self.ener_mes_horizont = self.ener_panel_spl.resample('M').sum()    
        
        

#########################################################################################################################################################################
#########################################################################################################################################################################

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
            
            self.labelModeloPanel.grid_forget()
            self.comboModeloPanel.grid_forget()
            self.frameRho.grid_forget()
            self.frameAnguloInc.grid_forget()
            self.frameG.grid_forget()
            self.frameTONC.grid_forget()
            self.framePmaxSTC.grid_forget()
            self.btnGraficar.grid_forget()

            # self.labelRho.grid_forget()
            # self.labelAnguloInc.grid_forget()
            # self.labelG.grid_forget()
            # self.labelTONC.grid_forget()
            # self.labelPmaxSTC.grid_forget()
            
            # self.entryRho.grid_forget()
            # self.entryAnguloInc.grid_forget()
            # self.entryG.grid_forget()
            # self.entryTONC.grid_forget()
            # self.entryPmaxSTC.grid_forget()

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
        valorComboBase=self.comboBases.get()
        valorComboMetodo=self.comboMetodos.get()
        valorComboTipoMetodoS=self.comboTipoMetodoSolar.get()
        valorComboTipoMetodoE=self.comboTipoMetodoEolico.get()
        
        if valorComboBase=="NREL":
            if valorComboMetodo=="Solar":
                if valorComboTipoMetodoS=="Masters":
                    self.graficarMastersNREL()
                if valorComboTipoMetodoS=="Tiwari":
                    self.graficarTiwariNREL()
            if valorComboMetodo=="Eólico":
                if valorComboTipoMetodoE=="Cronológico":
                    self.graficarCronoNREL()
                if valorComboTipoMetodoE=="Estadístico (Weibull)":
                    self.graficarWeibullNREL()

    def graficarMastersNREL(self):
        
        self.btnTabsResultadosAux.grid_forget()
        
        #self.btnTabsResultadosAux.grid_forget()
        self.frameTabsTiwariNREL.grid_forget()
        self.frameTabsMastersNREL.grid(column=0,row=0,sticky="NSEW")
        
        
        
        self.plotEnergiaMensualSupH()
        
        
    def graficarTiwariNREL(self):
        
        print("TIIIIIIIIIIIIIIWAAAAAAAAAAAARIIIIIIIIIIIIII")
        
        
        
        self.btnTabsResultadosAux.grid_forget()
        self.frameTabsMastersNREL.grid_forget()
        self.frameTabsTiwariNREL.grid(column=0,row=0,sticky="NSEW")
        
        
        self.ang, self.ang_tiwari, self.cos_d, self.sin_d, self.cos_W, self.sin_W, self.co_w, self.tet, self.sin_Ws, self.num_dia, self.sin_Wsrc = self.angulos_tiwari(self.n) #, aci   # Valores que retorna la funcion
        
        self.kT_diario_t, self.kT_mensual_t  = self.kt_bdd_tiwari (self.GHI_diario, self.num_dia, self.kT_mensual)   
        
        self.plotEnergiaMensualSupHTiwari()
        
        
    def plotEnergiaMensualSupHTiwari(self):
        self.btnTabsTiwariNREL1.config(background="gray70")
        self.btnTabsTiwariNREL2.config(background="gray94")
        self.btnTabsTiwariNREL3.config(background="gray94")
        
        
        self.Ic_tiw = self.ener_Ic_tiw ()
        
        print("//////////////////////////////////////// PF")
        print("Ic_tiw")
        print(self.Ic_tiw)
        
        self.Energ_Ic_tiw_anio = self.Ic_tiw.resample('Y').sum() 
        #self.Energ_Ic_tiw_mes = Ic_tiw.resample('M').sum()
        
        print("//////////////////////////////////////////////////////////////////////////////")
        print("self.Energ_Ic_tiw_anio")
        print(self.Energ_Ic_tiw_anio)
        
        
        np_aux_bar=self.Ic_tiw.iloc[:,0].to_numpy()
        auxTicks=np.linspace(0,len(self.Ic_tiw),len(self.Ic_tiw))
        
        self.subPlotFiguraResultados.clear()
                
        self.subPlotFiguraResultados.bar(x=auxTicks,height=np_aux_bar, width=0.7,color='r',edgecolor='black')          
        
        self.subPlotFiguraResultados.set_title('MÉTODO TIWARI: Energía SOLAR (SUPERFICIE INCLINADA)', fontsize=12)
        self.subPlotFiguraResultados.set_ylabel('Energía generada [kWh]', fontsize=12)
        self.subPlotFiguraResultados.set_xlabel('Fechas [meses]', fontsize=12)
        self.plotFiguraResultados.subplots_adjust(right=0.97)
        self.plotFiguraResultados.subplots_adjust(left=0.15)
        self.plotFiguraResultados.subplots_adjust(bottom=0.27)
        
        listaTicks=[]
        
        for i in self.Ic_tiw.index:
            print(i)
            listaTicks.append(i.strftime('%Y-%m'))
        
        self.subPlotFiguraResultados.set_xticklabels(listaTicks, rotation=90)
               
        self.subPlotFiguraResultados.xaxis.set_major_locator(matplotlib.ticker.FixedLocator(auxTicks))
        
        self.canvasPlotResultados.draw()
        
        
        
        
    def plotComparacionMensualMasters(self):
        self.energias_masters = pd.concat([self.ener_mes_horizont, self.Energ_IC_mes, self.Energ_IC1E_mes, self.Energ_IC2E_mes], axis=1)
        self.subPlotFiguraResultados.clear()
                       
        self.subPlotFiguraResultados.plot(self.energias_masters, label='Curva Aerogenerador777')               # grafica los alores de (y) y de (x)
        self.subPlotFiguraResultados.set_title('Comparación mensual de Energía (MÉTODO DE MASTERS)', fontsize=16)
        self.subPlotFiguraResultados.set_ylabel('Energía generada [kWh]', fontsize=15)
        
        self.plotFiguraResultados.subplots_adjust(right=0.97)
        self.plotFiguraResultados.subplots_adjust(left=0.15)
        self.canvasPlotResultados.draw()
        
        
    def plotEnergiaMensualSupInc(self):
        self.btnTabsMastersNREL1.config(background="gray94")
        self.btnTabsMastersNREL2.config(background="gray70")
        self.btnTabsMastersNREL3.config(background="gray94")
        self.btnTabsMastersNREL4.config(background="gray94")
        self.btnTabsMastersNREL5.config(background="gray94")
        
        
        print(self.Energ_IC_mes)
        
        npEnerg_IC=self.Energ_IC_mes["Energ_IC[kWh]"].to_numpy()
        auxTicks=np.linspace(0,len(npEnerg_IC),len(npEnerg_IC))
               
        
        self.subPlotFiguraResultados.clear()
                
        self.subPlotFiguraResultados.bar(x=auxTicks,height=npEnerg_IC, width=0.7,color='r',edgecolor='black')          
        
        self.subPlotFiguraResultados.set_title('MÉTODO MASTERS: Energía SOLAR (SUPERFICIE INCLINADA)', fontsize=12)
        self.subPlotFiguraResultados.set_ylabel('Energía generada [kWh]', fontsize=12)
        self.subPlotFiguraResultados.set_xlabel('Fechas [meses]', fontsize=12)
        self.plotFiguraResultados.subplots_adjust(right=0.97)
        self.plotFiguraResultados.subplots_adjust(left=0.15)
        self.plotFiguraResultados.subplots_adjust(bottom=0.27)
        
        listaTicks=[]
        
        for i in self.Energ_IC_mes.index:
            print(i)
            listaTicks.append(i.strftime('%Y-%m'))
        
        self.subPlotFiguraResultados.set_xticklabels(listaTicks, rotation=90)
               
        self.subPlotFiguraResultados.xaxis.set_major_locator(matplotlib.ticker.FixedLocator(auxTicks))
        
        self.canvasPlotResultados.draw()
        
        
        
    def plotEnergiaMensual1Eje(self):
        self.btnTabsMastersNREL1.config(background="gray94")
        self.btnTabsMastersNREL2.config(background="gray94")
        self.btnTabsMastersNREL3.config(background="gray70")
        self.btnTabsMastersNREL4.config(background="gray94")
        self.btnTabsMastersNREL5.config(background="gray94")
        
        self.Ic_1E = self.ener_Ic_1E ()
        self.Energ_IC1E_anio = self.Ic_1E.resample('Y').sum() 
        self.Energ_IC1E_mes = self.Ic_1E.resample('M').sum()
        
        print("Energ_IC1E_mes")
        print(self.Energ_IC1E_mes)
        
        self.Ic_2E = self.ener_Ic_2E ()
        self.Energ_IC2E_anio = self.Ic_2E.resample('Y').sum() 
        self.Energ_IC2E_mes = self.Ic_2E.resample('M').sum()
        
        np_aux_bar=self.Energ_IC1E_mes.iloc[:,0].to_numpy()
        auxTicks=np.linspace(0,len(self.Energ_IC1E_mes),len(self.Energ_IC1E_mes))
        
        self.subPlotFiguraResultados.clear()
                
        self.subPlotFiguraResultados.bar(x=auxTicks,height=np_aux_bar, width=0.7,color='r',edgecolor='black')          
        
        self.subPlotFiguraResultados.set_title('MÉTODO MASTERS: Energía SOLAR (SEGUIDOR 1 EJE)', fontsize=12)
        self.subPlotFiguraResultados.set_ylabel('Energía generada [kWh]', fontsize=12)
        self.subPlotFiguraResultados.set_xlabel('Fechas [meses]', fontsize=12)
        self.plotFiguraResultados.subplots_adjust(right=0.97)
        self.plotFiguraResultados.subplots_adjust(left=0.15)
        self.plotFiguraResultados.subplots_adjust(bottom=0.27)
        
        listaTicks=[]
        
        for i in self.Energ_IC1E_mes.index:
            print(i)
            listaTicks.append(i.strftime('%Y-%m'))
        
        self.subPlotFiguraResultados.set_xticklabels(listaTicks, rotation=90)
               
        self.subPlotFiguraResultados.xaxis.set_major_locator(matplotlib.ticker.FixedLocator(auxTicks))
        
        self.canvasPlotResultados.draw()
        
    
    def plotEnergiaMensual2Ejes(self):
        self.btnTabsMastersNREL1.config(background="gray94")
        self.btnTabsMastersNREL2.config(background="gray94")
        self.btnTabsMastersNREL3.config(background="gray94")
        self.btnTabsMastersNREL4.config(background="gray70")
        self.btnTabsMastersNREL5.config(background="gray94")
        
        self.Ic_1E = self.ener_Ic_1E ()
        self.Energ_IC1E_anio = self.Ic_1E.resample('Y').sum() 
        self.Energ_IC1E_mes = self.Ic_1E.resample('M').sum()
        
        print("Energ_IC1E_mes")
        print(self.Energ_IC1E_mes)
        
        self.Ic_2E = self.ener_Ic_2E ()
        self.Energ_IC2E_anio = self.Ic_2E.resample('Y').sum() 
        self.Energ_IC2E_mes = self.Ic_2E.resample('M').sum()
        
        np_aux_bar=self.Energ_IC2E_mes.iloc[:,0].to_numpy()
        auxTicks=np.linspace(0,len(self.Energ_IC2E_mes),len(self.Energ_IC2E_mes))
        
        self.subPlotFiguraResultados.clear()
                
        self.subPlotFiguraResultados.bar(x=auxTicks,height=np_aux_bar, width=0.7,color='r',edgecolor='black')          
        
        self.subPlotFiguraResultados.set_title('MÉTODO MASTERS: Energía SOLAR (SEGUIDOR 2 EJES)', fontsize=12)
        self.subPlotFiguraResultados.set_ylabel('Energía generada [kWh]', fontsize=12)
        self.subPlotFiguraResultados.set_xlabel('Fechas [meses]', fontsize=12)
        self.plotFiguraResultados.subplots_adjust(right=0.97)
        self.plotFiguraResultados.subplots_adjust(left=0.15)
        self.plotFiguraResultados.subplots_adjust(bottom=0.27)
        
        listaTicks=[]
        
        for i in self.Energ_IC2E_mes.index:
            print(i)
            listaTicks.append(i.strftime('%Y-%m'))
        
        self.subPlotFiguraResultados.set_xticklabels(listaTicks, rotation=90)
               
        self.subPlotFiguraResultados.xaxis.set_major_locator(matplotlib.ticker.FixedLocator(auxTicks))
        
        self.canvasPlotResultados.draw()
        
        
        
    def plotEnergiaMensualSupH(self):
        self.btnTabsMastersNREL1.config(background="gray70")
        self.btnTabsMastersNREL2.config(background="gray94")
        self.btnTabsMastersNREL3.config(background="gray94")
        self.btnTabsMastersNREL4.config(background="gray94")
        self.btnTabsMastersNREL5.config(background="gray94")
        
        
        

        
        
        npAEnerMes=self.ener_mes_horizont["Energia [kWh]"].to_numpy()
        npAFechas=self.ener_mes_horizont.index.to_numpy()
        auxTicks=np.linspace(0,len(npAEnerMes),len(npAEnerMes))
        
 
        
        # print("dtypes npAFechas")
        # print(npAFechas.dtype)
                
            
        self.subPlotFiguraResultados.clear()
                
        self.subPlotFiguraResultados.bar(x=auxTicks,height=npAEnerMes, width=0.7,color='r',edgecolor='black')          
        
        self.subPlotFiguraResultados.set_title('Energía SOLAR Generada MENSUAL: sup. HORIZONTAL', fontsize=12)
        self.subPlotFiguraResultados.set_ylabel('Energía generada [kWh]', fontsize=12)
        self.subPlotFiguraResultados.set_xlabel('Fechas [meses]', fontsize=12)
        self.plotFiguraResultados.subplots_adjust(right=0.97)
        self.plotFiguraResultados.subplots_adjust(left=0.15)
        self.plotFiguraResultados.subplots_adjust(bottom=0.27)
        
        listaTicks=[]
        
        for i in self.ener_mes_horizont.index:
            print(i)
            listaTicks.append(i.strftime('%Y-%m'))
        
        self.subPlotFiguraResultados.set_xticklabels(listaTicks, rotation=90)
               
        self.subPlotFiguraResultados.xaxis.set_major_locator(matplotlib.ticker.FixedLocator(auxTicks))
        
        self.canvasPlotResultados.draw()
        
        
                
    
    def graficarCronoNREL(self):
        x=np.linspace(0,30,1000) 
        y=np.sin(x)
        self.subPlotFiguraResultados.clear()
                       
        self.subPlotFiguraResultados.plot(x, y, label='Curva Aerogenerador777')               # grafica los alores de (y) y de (x)
        self.subPlotFiguraResultados.set_title('(Potencia - Velocidad) del Aerogenerador777', fontsize=16)
        self.subPlotFiguraResultados.set_ylabel('Potencia [W] ', fontsize=15)
        self.subPlotFiguraResultados.set_xlabel('Velocidad [m/s] ', fontsize=15)
        self.plotFiguraResultados.subplots_adjust(right=0.97)
        self.plotFiguraResultados.subplots_adjust(left=0.15)
        self.canvasPlotResultados.draw()
        
    def graficarWeibullNREL(self):
        x=np.linspace(0,30,1000) 
        y=np.power(x,5)
        self.subPlotFiguraResultados.clear()
                       
        self.subPlotFiguraResultados.plot(x, y, label='Curva Aerogenerador777')               # grafica los alores de (y) y de (x)
        self.subPlotFiguraResultados.set_title('(Potencia - Velocidad) del Aerogenerador777', fontsize=16)
        self.subPlotFiguraResultados.set_ylabel('Potencia [W] ', fontsize=15)
        self.subPlotFiguraResultados.set_xlabel('Velocidad [m/s] ', fontsize=15)
        self.plotFiguraResultados.subplots_adjust(right=0.97)
        self.plotFiguraResultados.subplots_adjust(left=0.15)
        self.canvasPlotResultados.draw()
        
    def graficarMastersSECAMB(self):
        x=np.linspace(0,30,1000) 
        y=np.power(x,6)
        self.subPlotFiguraResultados.clear()
                       
        self.subPlotFiguraResultados.plot(x, y, label='Curva Aerogenerador777')               # grafica los alores de (y) y de (x)
        self.subPlotFiguraResultados.set_title('(Potencia - Velocidad) del Aerogenerador777', fontsize=16)
        self.subPlotFiguraResultados.set_ylabel('Potencia [W] ', fontsize=15)
        self.subPlotFiguraResultados.set_xlabel('Velocidad [m/s] ', fontsize=15)
        self.plotFiguraResultados.subplots_adjust(right=0.97)
        self.plotFiguraResultados.subplots_adjust(left=0.15)
        self.canvasPlotResultados.draw()

    def graficarTiwariSECAMB(self):
        x=np.linspace(0,30,1000) 
        y=np.power(x,7)
        self.subPlotFiguraResultados.clear()
                       
        self.subPlotFiguraResultados.plot(x, y, label='Curva Aerogenerador777')               # grafica los alores de (y) y de (x)
        self.subPlotFiguraResultados.set_title('(Potencia - Velocidad) del Aerogenerador777', fontsize=16)
        self.subPlotFiguraResultados.set_ylabel('Potencia [W] ', fontsize=15)
        self.subPlotFiguraResultados.set_xlabel('Velocidad [m/s] ', fontsize=15)
        self.plotFiguraResultados.subplots_adjust(right=0.97)
        self.plotFiguraResultados.subplots_adjust(left=0.15)
        self.canvasPlotResultados.draw()
        
    def graficarCronoSECAMB(self):
        x=np.linspace(0,30,1000) 
        y=np.power(x,8)
        self.subPlotFiguraResultados.clear()
                       
        self.subPlotFiguraResultados.plot(x, y, label='Curva Aerogenerador777')               # grafica los alores de (y) y de (x)
        self.subPlotFiguraResultados.set_title('(Potencia - Velocidad) del Aerogenerador777', fontsize=16)
        self.subPlotFiguraResultados.set_ylabel('Potencia [W] ', fontsize=15)
        self.subPlotFiguraResultados.set_xlabel('Velocidad [m/s] ', fontsize=15)
        self.plotFiguraResultados.subplots_adjust(right=0.97)
        self.plotFiguraResultados.subplots_adjust(left=0.15)
        self.canvasPlotResultados.draw()
        
    def graficarWeibullSECAMB(self):
        x=np.linspace(0,30,1000) 
        y=np.power(x,9)
        self.subPlotFiguraResultados.clear()
                       
        self.subPlotFiguraResultados.plot(x, y, label='Curva Aerogenerador777')               # grafica los alores de (y) y de (x)
        self.subPlotFiguraResultados.set_title('(Potencia - Velocidad) del Aerogenerador777', fontsize=16)
        self.subPlotFiguraResultados.set_ylabel('Potencia [W] ', fontsize=15)
        self.subPlotFiguraResultados.set_xlabel('Velocidad [m/s] ', fontsize=15)
        self.plotFiguraResultados.subplots_adjust(right=0.97)
        self.plotFiguraResultados.subplots_adjust(left=0.15)
        self.canvasPlotResultados.draw()
        
    

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
        self.subPlotFiguraDatos.clear()
        x=np.linspace(-100,100,num=200)
        y=np.sin(0.002*x**2)
        self.subPlotFiguraDatos.plot(x,y)
        self.canvasPlotDatos.draw()

    def plotCurvaAerogenerador(self):
        
        
        x=np.linspace(0,30,1000) 
        y=np.power(x,3)
        self.subPlotFiguraResultados.clear()
                       
        self.subPlotFiguraResultados.plot(x, y, label='Curva Aerogenerador777')          
        self.subPlotFiguraResultados.set_title('(Potencia - Velocidad) del Aerogenerador777', fontsize=16)
        self.subPlotFiguraResultados.set_ylabel('Potencia [W] ', fontsize=15)
        self.subPlotFiguraResultados.set_xlabel('Velocidad [m/s] ', fontsize=15)
        self.plotFiguraResultados.subplots_adjust(right=0.97)
        self.plotFiguraResultados.subplots_adjust(left=0.15)
        self.canvasPlotResultados.draw()
        
        
    def plotIrradDatos(self):        
        self.btnTabsDatos1.configure(background="gray70")
        self.btnTabsDatos2.configure(background="gray94")
        self.btnTabsDatos3.configure(background="gray94")
        self.btnTabsDatos4.configure(background="gray94")
        
        self.subPlotFiguraDatos.clear()
        self.subPlotFiguraDatos.plot(self.INTER_irrad, label='Curva Aerogenerador')      
        self.subPlotFiguraDatos.set_title('Distribución Temporal "IRRADIANCIA"', fontsize=12)
        self.subPlotFiguraDatos.set_ylabel('Irradiancia [W/m^2]', fontsize=12)
        self.subPlotFiguraDatos.set_xlabel(self.varAnio.get(), fontsize=12)
        fmt = mdates.DateFormatter('%d-%b')
        self.subPlotFiguraDatos.xaxis.set_major_formatter(fmt)
        self.plotFiguraDatos.subplots_adjust(bottom=0.2)
        
        
        self.canvasPlotDatos.draw()
        
    def plotVelDatos(self):
        self.btnTabsDatos1.configure(background="gray94")
        self.btnTabsDatos2.configure(background="gray70")
        self.btnTabsDatos3.configure(background="gray94")
        self.btnTabsDatos4.configure(background="gray94")
        
        self.subPlotFiguraDatos.clear()
        self.subPlotFiguraDatos.plot(self.INTER_vel, label='Curva Aerogenerador')     
        self.subPlotFiguraDatos.set_title('Distribución Temporal "Velocidad del Viento"', fontsize=12)
        self.subPlotFiguraDatos.set_ylabel('Velocidad del Viento [m/s]', fontsize=12) 
        self.subPlotFiguraDatos.set_xlabel(self.varAnio.get(), fontsize=12)
        fmt = mdates.DateFormatter('%d-%b')
        self.subPlotFiguraDatos.xaxis.set_major_formatter(fmt)
        self.plotFiguraDatos.subplots_adjust(bottom=0.2)
        
        
        self.canvasPlotDatos.draw()
    def plotDirDatos(self):
        self.btnTabsDatos1.configure(background="gray94")
        self.btnTabsDatos2.configure(background="gray94")
        self.btnTabsDatos3.configure(background="gray70")
        self.btnTabsDatos4.configure(background="gray94")
        
        self.subPlotFiguraDatos.clear()
        self.subPlotFiguraDatos.plot(self.INTER_direc, label='Curva Aerogenerador')      
        self.subPlotFiguraDatos.set_title('Distribución Temporal "Dirección del Viento"', fontsize=12)
        self.subPlotFiguraDatos.set_ylabel('Dirección del Viento [°]', fontsize=12)
        self.subPlotFiguraDatos.set_xlabel(self.varAnio.get(), fontsize=12)
        fmt = mdates.DateFormatter('%d-%b')
        self.subPlotFiguraDatos.xaxis.set_major_formatter(fmt)
        self.plotFiguraDatos.subplots_adjust(bottom=0.2)
        
        
        self.canvasPlotDatos.draw()
    def plotTempDatos(self):
        self.btnTabsDatos1.configure(background="gray94")
        self.btnTabsDatos2.configure(background="gray94")
        self.btnTabsDatos3.configure(background="gray94")
        self.btnTabsDatos4.configure(background="gray70")
        
        self.subPlotFiguraDatos.clear()
        self.subPlotFiguraDatos.plot(self.INTER_temp, label='Curva Aerogenerador')      
        self.subPlotFiguraDatos.set_title('Distribución Temporal "Temperatura"', fontsize=12)
        self.subPlotFiguraDatos.set_ylabel('Temperatura [°C]', fontsize=12)
        self.subPlotFiguraDatos.set_xlabel(self.varAnio.get(), fontsize=12)
        fmt = mdates.DateFormatter('%d-%b')
        self.subPlotFiguraDatos.xaxis.set_major_formatter(fmt)
        self.plotFiguraDatos.subplots_adjust(bottom=0.2)
        
        
        self.canvasPlotDatos.draw()
    
    
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
        
            self.btnTabsDatosAux.grid_forget()
            
            self.btnTabsDatos1=tk.Button(self.tabsDatos,text="Irradiancia",command=self.plotIrradDatos)
            self.btnTabsDatos2=tk.Button(self.tabsDatos,text="Velocidad Viento",command=self.plotVelDatos)
            self.btnTabsDatos3=tk.Button(self.tabsDatos,text="Dirección Viento",command=self.plotDirDatos)
            self.btnTabsDatos4=tk.Button(self.tabsDatos,text="Temperatura",command=self.plotTempDatos)
                    
            
            
            self.btnTabsDatos1.grid(column=0,row=0)
            self.btnTabsDatos2.grid(column=1,row=0)
            self.btnTabsDatos3.grid(column=2,row=0)
            self.btnTabsDatos4.grid(column=3,row=0)
            
            self.plotIrradDatos()
            
            
            self.obtenerDatosGlobal()
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
        self.ang_concat=pd.concat([n,delta], axis=1)                                # se concatena todos los valores calculados
        self.ang_concat=self.ang_concat.drop(['N hora','N minutos'],axis=1)              # se elimina las columnas 'N minutos','N minutos'
        self.ang_concat['H antes del medio dia'] = 12+self.ang_concat['Horas dia']*-1    # se determina las horas antes del medio dia 
        self.ang_concat['∡ horario (H°)'] = self.ang_concat['H antes del medio dia']*15  # se determina el angulo horario H
        #------------------------ Se calcula COSENO (H) ------------------------
        co_H=self.ang_concat.filter(items=['∡ horario (H°)'])                    # se filtra la columna deseada
        coseno_H=lambda co_H : math.cos(co_H* math.pi/180)                  # se aplica la formula para calcular coseno de H de la columna filtrada
        cos_H=self.ang_concat['∡ horario (H°)'].apply(coseno_H).to_frame()       # la formula devuelve un tipo series, por lo tanto se transforma a frame
        cos_H.columns=['coseno (H°)']                                       # se cambia el nombre de la columna
        #-------------------------- Se calcula SENO (H) ------------------------
        seno_H=lambda co_H : math.sin(co_H* math.pi/180)                    # se aplica la formula para calcular coseno de H de la columna filtrada
        sin_H=self.ang_concat['∡ horario (H°)'].apply(seno_H).to_frame()         # la formula devuelve un tipo series, por lo tanto se transforma a frame
        sin_H.columns=['seno (H°)']                                         # se cambia el nombre de la columna
        #----------------------- Se calcula coseno (δ°) ------------------------
        coseno_d=lambda delta : math.cos(delta* math.pi/180)                # se aplica la formula para calcular coseno de delta
        cos_d=self.ang_concat['Declinación (δ°)'].apply(coseno_d).to_frame()     # la formula devuelve un tipo series, por lo tanto se transforma a frame
        cos_d.columns=['coseno (δ°)']                                       # se cambia el nombre de la columna
        #------------------------ Se calcula SENO (δ°) -------------------------
        seno_d=lambda delta : math.sin(delta* math.pi/180)                  # se aplica la formula para calcular seno de delta
        sin_d=self.ang_concat['Declinación (δ°)'].apply(seno_d).to_frame()       # la formula devuelve un tipo series, por lo tanto se transforma a frame
        sin_d.columns=['seno (δ°)']                                         # se cambia el nombre de la columna
        #------------------------- Se calcula TAN (δ°) -------------------------
        tangente_d=lambda delta : math.tan(delta* math.pi/180)              # se aplica la formula para calcular tangente de delta
        tan_d=self.ang_concat['Declinación (δ°)'].apply(tangente_d).to_frame()   # la formula devuelve un tipo series, por lo tanto se transforma a frame
        tan_d.columns=['tan (δ°)']                                          # se cambia el nombre de la columna
        #----------H_SR ángulo horario de salida del sol (en radianes)---------- 
        H_amanecer=lambda tan_d : math.acos(-self.tan_L*tan_d* math.pi/180)      # se aplica la formula para calcular angulo H_SR°
        H_SR=self.ang_concat['Declinación (δ°)'].apply(H_amanecer).to_frame()    # la formula devuelve un tipo series, por lo tanto se transforma a frame
        H_SR.columns=['H_SR (Radianes)']                                    # se cambia el nombre de la columna 
        H_SR['(H_SR°)'] = H_SR['H_SR (Radianes)']*180/math.pi               # se transforma de radianes a grados la columna 'Radianes (H_SR)'
        self.ang_concat=pd.concat([self.ang_concat,cos_H,sin_H,cos_d, sin_d, tan_d,H_SR], axis=1)   # se concatena todos los valores calculados
        #-------------seno H_SR ángulo horario de salida del sol ---------------
        sin_Hsr=self.ang_concat.filter(items=['H_SR (Radianes)'])  
        seno_HSR =lambda sin_Hsr : math.sin(sin_Hsr)                        # se aplica la formula para calcular angulo H_SR°
        sin_H_SR=self.ang_concat['H_SR (Radianes)'].apply(seno_HSR).to_frame()   # la formula devuelve un tipo series, por lo tanto se transforma a frame
        sin_H_SR.columns=['seno (H_SR)']                                    # se cambia el nombre de la columna 
        self.ang_concat=pd.concat([self.ang_concat,sin_H_SR], axis=1)                 # se concatena todos los valores calculados
        #----------------------------SENO de (β°)-------------------------------  
        self.ang_concat['seno (β°)'] = self.ang_concat['coseno (δ°)']*self.ang_concat['coseno (H°)']*self.cos_L + self.sin_L*self.ang_concat['seno (δ°)'] # se calcula el seno(β°)
        #------------- Se calcula la altitud β (A cualquier hora)---------------  
        bet=self.ang_concat.filter(items=['seno (β°)'])                          # saca los valores de la columna a ser calculada posteriormente
        beta_H=lambda bet : math.asin(bet)                                  # se aplica la formula para calcular seno de β
        B_H=self.ang_concat['seno (β°)'].apply(beta_H).to_frame()                # la formula devuelve un tipo series, por lo tanto se transforma a frame
        B_H.columns=['Beta (β°)']                                           # se cambia el nombre de la columna
        B_H['Beta (β°)'] = B_H['Beta (β°)']* 180/math.pi                    # se transforma a grados el angulo β
        self.ang_concat=pd.concat([self.ang_concat, B_H], axis=1)                     # se concatena la nueva columna calculada al dataframe anterior
        #-----------------------COSENO β (A cualquier hora)---------------------  
        BETA=self.ang_concat.filter(items=['Beta (β°)'])                         # saca los valores de la columna a ser calculada posteriormente
        beta_B=lambda BETA : math.cos(BETA* math.pi/180)                    # se aplica la formula para calcular seno de β
        BET=self.ang_concat['Beta (β°)'].apply(beta_B).to_frame()                # la formula devuelve un tipo series, por lo tanto se transforma a frame
        BET.columns=['cos (β°)']                                            # se cambia el nombre de la columna
        self.ang_concat=pd.concat([self.ang_concat, BET], axis=1)                     # se concatena la nueva columna calculada al dataframe anterior
        #--------Insolación extraterrestre media diaria Io (kWh/m^2-día)--------  
        num_dia=self.ang_concat.filter(items=['n_dia'])                          # saca los valores de la columna a ser calculada posteriormente
        I_ex=lambda num_dia : math.cos(((num_dia*360)/365)* math.pi/180)    # se aplica la formula para calcular auxiliar de formula
        Io_aux=self.ang_concat['n_dia'].apply(I_ex).to_frame()                   # la formula devuelve un tipo series, por lo tanto se transforma a frame
        Io_aux.columns=['Aux_ndia']                                         # se cambia el nombre de la columna
        #Io_aux['Aux_ndia'] = Io_aux['Aux_ndia']* 180/math.pi               # se transforma a grados el angulo β
        self.ang_concat=pd.concat([self.ang_concat, Io_aux], axis=1)                  # se concatena la nueva columna calculada al dataframe anterior
        SC=1.37                                                            # kW/m^2 constante solar SC=1.377 kW/m^2,   puede ser SC=1.367 kWh/m^2
        self.ang_concat['Io (kWh/m^2)'] = (24/math.pi)*SC*(1+0.034*self.ang_concat['Aux_ndia'] )*(self.cos_L*self.ang_concat['coseno (δ°)']*self.ang_concat['seno (H_SR)']+ self.ang_concat['H_SR (Radianes)']* self.sin_L*self.ang_concat['seno (δ°)'] )   # se calcula el Io(kW/m^2)
        #---------------------Ángulo de acimut solar (Φs)---------------------- 
        self.ang_concat['seno (Φs)'] = self.ang_concat['coseno (δ°)']*self.ang_concat['seno (H°)']/self.ang_concat['cos (β°)'] # se calcula el seno (Φs)
        aci=self.ang_concat.filter(items=['seno (Φs)'])                          # saca los valores de la columna a ser calculada posteriormente
        acimu=lambda aci : math.asin(aci)                                   # se aplica la formula para calcular arcseno (Φs)
        acimut_s = self.ang_concat['seno (Φs)'].apply(acimu).to_frame()          # la formula devuelve un tipo series, por lo tanto se transforma a frame
        acimut_s.columns = ['(Φs1)']                                        # se cambia el nombre de la columna
        acimut_s['(Φs1)'] = acimut_s['(Φs1)']* 180/math.pi                  # se transforma a grados el angulo Φs1
        self.ang_concat = pd.concat([self.ang_concat, acimut_s], axis=1)              # se concatena la nueva columna calculada al dataframe anterior
        self.ang_concat['(Φs2)'] = 180 - (self.ang_concat['(Φs1)'])                   # se aumenta una nueva columna (Φs2), ya que el seno del acimut es ambiguo
        #------------------------Relacion tg(δ) / tg(L) ----------------------- 
        self.ang_concat['tg(δ)/tg(L)'] = self.ang_concat['tan (δ°)']/self.tan_L            # se calcula el relacion tg(δ)/tg(L)
        #------------------------filtrar columnas (Φs)------------------------- 
        self.ang_concat['Φs'] = np.where(self.ang_concat['coseno (H°)']>= self.ang_concat['tg(δ)/tg(L)'], self.ang_concat['(Φs1)'], self.ang_concat['(Φs2)'] )  # creacion de una columna 'Φs' para rellenar con nuevos valores bajo las condiciones de la ambiguedaddel seno
        #--------H_SRC ángulo horario; salida del sol (PARA EL COLECTOR)------- 
        H_amanecer_c=lambda tan_d : math.acos(-self.tan_LE*tan_d* math.pi/180)    # se aplica la formula para calcular angulo H_SRC°
        H_SRC=self.ang_concat['Declinación (δ°)'].apply(H_amanecer_c).to_frame()  # la formula devuelve un tipo series, por lo tanto se transforma a frame
        H_SRC.columns=['H_SRC (Radianes)']                                   # se cambia el nombre de la columna 
        H_SRC['(H_SRC°)'] = H_SRC['H_SRC (Radianes)']*180/math.pi            # se transforma de radianes a grados la columna 'Radianes (H_SRC)'
        self.ang_concat=pd.concat([self.ang_concat, H_SRC], axis=1)                    # se concatena todos los valores calculados
        #-------------------H_SRC mínimo (PARA EL COLECTOR)---------------------
        self.ang_concat['H_SRC min'] = np.where(self.ang_concat['H_SR (Radianes)'] < self.ang_concat['H_SRC (Radianes)'] , self.ang_concat['H_SR (Radianes)'], self.ang_concat['H_SRC (Radianes)'])        # creacion de una columna 'H_SRC min' para rellenar con las condiciones de H_SRC (mínimo)
        #------------seno H_SRC ángulo horario de salida del sol ---------------
        sin_Hsrc=self.ang_concat.filter(items=['H_SRC min'])                      # filtra los valores de la columna a ser calculada posteriormente
        seno_HSRC =lambda sin_Hsrc : math.sin(sin_Hsrc)                      # se aplica la formula para calcular angulo H_SR°
        sin_H_SRC=self.ang_concat['H_SRC min'].apply(seno_HSRC).to_frame()        # la formula devuelve un tipo series, por lo tanto se transforma a frame
        sin_H_SRC.columns=['seno (H_SRC)']                                   # se cambia el nombre de la columna 
        self.ang_concat=pd.concat([self.ang_concat,sin_H_SRC], axis=1)                 # se concatena todos los valores calculados
        #---------FACTORES DE CONVERSION SOBRE UNA SUPERFICIE INCLINADA---------
        self.ang_concat['Rb'] = (self.cos_LE*self.ang_concat['coseno (δ°)']*self.ang_concat['seno (H_SRC)'] + self.ang_concat['H_SRC min']*self.sin_LE*self.ang_concat['seno (δ°)'])/(self.cos_L*self.ang_concat['coseno (δ°)']*self.ang_concat['seno (H_SR)'] + self.ang_concat['H_SR (Radianes)']*self.sin_L*self.ang_concat['seno (δ°)']) # Factor de conversion de radiacion de haz Rb
        
        return ang, self.ang_concat, cos_d, sin_d, cos_H, sin_H, co_H, bet, aci, BETA, sin_Hsr, num_dia, sin_Hsrc      # Valores que retorna la funcion

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


    def spl_de_INTER (self,INTER_irrad, INTER_vel, INTER_temp):
    #--------------------------SPLINE DE BDD -------------------------------
    
        med_irrad_INTER = INTER_irrad.shape[0]                                 # cuenta los valores del dataframe (tipo int)
        hora = np.linspace(0, med_irrad_INTER, med_irrad_INTER)                # med_irrad_INTER guarda el numero de mediciones de la variable irradiancia.
        [t, c, k] = splrep(hora, INTER_irrad, s=0, k=3)                        # s: determina una condicion de suavisado (cercania y control del ajuste), s=0 si no se determinan los pesos (w) en la interpolacion______k: grado de ajuste del spline. Se recomienda splines cúbicos. Deben evitarse los valores pares de k, especialmente con valores pequeños de s. 1 <= k <= 5
        hora1 = np.linspace(0, med_irrad_INTER, med_irrad_INTER*4)             # valores del eje x para el grafico. (med_irrad_INTER*2) Se multiplica por 2 para obtener el doble de valores diarios.
        interp = splev(hora1, [t, c, k])                                       # spl recibe como argumentos(x, [t, c, k]).
        dates = pd.date_range(start=self.fecha_ini , periods=med_irrad_INTER*4, freq='15T') # med_irrad_INTER*2 ; 4: datos por hora (se duplican la cantidad de datos); Al ser 4 datos por hora la frecuencia es cada 15 min ('15T'), ya que (4*15=60).
        self.INTER_spl_irrad = pd.DataFrame(data=interp,index=dates)
        self.INTER_spl_irrad[self.INTER_spl_irrad < 0.1]=0
        self.INTER_spl_irrad.columns = ['GHI']                                      # cambio el nombre de la columna
        self.INTER_spl_irrad.index.names = ['Fecha']
        

        self.INTER_spl_irrad.plot(linewidth=0.8).set_title('spline INTER irrad, aumenta periodos')
        
        med_vel_INTER = INTER_vel.shape[0]                                     # cuenta los valores del dataframe (tipo int)
        hora = np.linspace(0, med_vel_INTER, med_vel_INTER)                    # med_vel_INTER guarda el numero de mediciones de la variable irradiancia.
        [t, c, k] = splrep(hora, INTER_vel, s=0, k=3)                          # s: determina una condicion de suavisado (cercania y control del ajuste), s=0 si no se determinan los pesos (w) en la interpolacion______k: grado de ajuste del spline. Se recomienda splines cúbicos. Deben evitarse los valores pares de k, especialmente con valores pequeños de s. 1 <= k <= 5
        hora1 = np.linspace(0, med_vel_INTER, med_vel_INTER*4)                 # valores del eje x para el grafico. (med_vel_INTER*2) Se multiplica por 2 para obtener el doble de valores diarios.
        interp = splev(hora1, [t, c, k])                                       # spl recibe como argumentos(x, [t, c, k]).
        dates = pd.date_range(start=self.fecha_ini , periods=med_vel_INTER*4, freq='15T') # med_vel_INTER*2 ; 4: datos por hora (se duplican la cantidad de datos); Al ser 4 datos por hora la frecuencia es cada 15 min ('15T'), ya que (4*15=60).
        self.INTER_spl_vel = pd.DataFrame(data=interp,index=dates)
        self.INTER_spl_vel[self.INTER_spl_vel < 0]=0
        self.INTER_spl_vel.columns = ['Wind Speed']                                 # cambio el nombre de la columna
        self.INTER_spl_vel.index.names = ['Fecha']

        self.INTER_spl_vel.plot(linewidth=0.8).set_title('spline BDD vel. viento, aumenta periodos')
        
        
        med_temp_INTER = INTER_temp.shape[0]                                   # cuenta los valores del dataframe (tipo int)
        hora = np.linspace(0, med_temp_INTER, med_temp_INTER)                  # med_temp_INTER guarda el numero de mediciones de la variable irradiancia.
        [t, c, k] = splrep(hora, INTER_temp, s=0, k=3)                         # s: determina una condicion de suavisado (cercania y control del ajuste), s=0 si no se determinan los pesos (w) en la interpolacion______k: grado de ajuste del spline. Se recomienda splines cúbicos. Deben evitarse los valores pares de k, especialmente con valores pequeños de s. 1 <= k <= 5
        hora1 = np.linspace(0, med_temp_INTER, med_temp_INTER*4)               # valores del eje x para el grafico. (med_temp_INTER*2) Se multiplica por 2 para obtener el doble de valores diarios.
        interp = splev(hora1, [t, c, k])                                       # spl recibe como argumentos(x, [t, c, k]).
        dates = pd.date_range(start=self.fecha_ini , periods=med_temp_INTER*4, freq='15T') # med_temp_INTER*2 ; 4: datos por hora (se duplican la cantidad de datos); Al ser 4 datos por hora la frecuencia es cada 15 min ('15T'), ya que (4*15=60).
        self.INTER_spl_temp = pd.DataFrame(data=interp,index=dates)
        self.INTER_spl_temp[self.INTER_spl_temp < 0]=0
        self.INTER_spl_temp.columns = ['Temperatura']
        self.INTER_spl_temp.index.names = ['Fecha']

        self.INTER_spl_temp.plot().set_title('spline INTER temperatura, aumenta periodos')
                
        return self.INTER_spl_irrad, self.INTER_spl_vel, self.INTER_spl_temp                                     # Valores que retorna la funcion
    def Potencia(self,Tamb , Ex): # Tamb:[C] ; Ex:[W/m2]
        TONC = 47.5                                                 # da el fabricante [°C]
        T_cell = Tamb +(TONC-20)*(Ex/800)                           # calculo te la temp. del panel
        g = -0.463 # %/C                                            # da el fabricante  (coeficiente de temperatura de potencia maxima)
        Pmax_STC = 250                                              # da el fabricante [Wp]
        Pmax_T_cell_bdd = Pmax_STC*(1+(g/100)*(T_cell-25))*(Ex/1000)
        
        
        return Pmax_T_cell_bdd      
    
    
    def ener_Ic (self):
        Ic_incli = self.kT_mensual.filter(items=['IC'])                 # filtro IC 
        Ic_incli = self.Temp_prom_mes.Temperatura.astype(object).combine(Ic_incli.IC , func=self.Potencia)
        Ic_incli = Ic_incli.to_frame()
        Ic_incli.columns = ['Energia prom IC[kWh]']                # cambio el nombre de la columna
        Ic_incli = pd.concat([Ic_incli,self.q], axis=1)                 # se concatena todos los valores calculados
        Ic_incli['Energ_IC[kWh]'] = Ic_incli['Energia prom IC[kWh]']*Ic_incli['dias'] # se 
        Ic_incli = Ic_incli.filter(items=['Energ_IC[kWh]'])

        return Ic_incli
    
    def numero_dias (self,num_dia):
        prom_dias = num_dia.resample('M').mean()
        
        fechas=prom_dias.index                                # adquiere todas las dechas del DataFrame bdd_float
        print("prom_dias")
        print(prom_dias)
        
        q=fechas.to_frame()                                   # Se crea una variable que contenga las fechas de la base de datos pero en formato DataFrame  
        q.columns=["Fecha"]
        print("q")
        print(q)
        
        q['dias'] = q.Fecha.dt.strftime('%d')                 # Se cre una columna con nombre n_dia que adquiere el numero de dia del anio de la columna Fecha, a traves de (.dt.strftime('%j'))
        q=q.drop(['Fecha'],axis=1)                            # se elimina la columna Fecha 
        col=['dias']                                          # se enlista el nombre de las nuevas columnas
        q[col]=q[col].apply(pd.to_numeric, errors='coerce', axis=1) # se transforma a formato numerico las columnas que se introducen anteriormente
        
        return q
    
    def kt_bdd_masters (self):
    
        GHI_diario = self.INTER_spl_irrad.resample('D').apply(integrate.trapz, dx=1/4)  # Area bajo la curva de irradiacion, energia diaria de la irradiacion global ;   dx=1/2 porque la integracion por defecto es de 1 unidad (hora), como tenemos una frecuencia de 30T, se debe especificar que la hora la dividimos en 2 partes de 30 minutos
        GHI_diario['GHI'] = GHI_diario['GHI']/1000                         # paso a kWh/m^2-dia   
        GHI_diario.columns=['GHI kWh/m^2-dia']                             # se cambia el nombre de la columna
        
        Io_irad = self.ang_concat.filter(items=['Io (kWh/m^2)'])                # se filtra item Io, para promediar diariamente
        Io_irad = Io_irad.resample('D').mean()                             # se promedia diariamente Io
        #------------------- METODO DE MASTERS, calculo de (kT)---------------
        kT_diario=pd.concat([GHI_diario, Io_irad], axis=1)                       # se concatena la nueva columna calculada al dataframe anterior
        kT_diario['kT'] = kT_diario['GHI kWh/m^2-dia']/kT_diario['Io (kWh/m^2)'] # se calcula el kT(indice de claridad diario)
        kT_diario['I_DH kWh/m^2-dia'] = kT_diario['GHI kWh/m^2-dia']*(1.390-4.027*kT_diario['kT']+5.531*kT_diario['kT']**2-3.108*kT_diario['kT']**3)  # calculo de irradiancia difusa horizontal DIARIA
        kT_diario['IBH'] = kT_diario['GHI kWh/m^2-dia'] - kT_diario['I_DH kWh/m^2-dia']                              # se encuentra la irradiancia de haz directo en una superficie horizontal
        #------------------- METODO DE MASTERS, filtro de (Rb)----------------
        Rb_m = self.ang_concat.filter(items=['Rb'])                             # se filtra item Rb, para promediar diariamente
        Rb_m = Rb_m.resample('D').mean()                                   # se promedia diariamente Rb
        kT_diario=pd.concat([kT_diario, Rb_m], axis=1)                     # se concatena todos los valores calculados
        #-----RADIACION SOLAR TOTAL "DIARIA" EN UNA SUPEFICIE INCLINADA-------
        kT_diario['IC'] = kT_diario['IBH']*kT_diario['Rb']+kT_diario['I_DH kWh/m^2-dia']*self.Rd+ self.Ro*kT_diario['GHI kWh/m^2-dia']*self.Rr

        #----------------Angulos de conversion montura DOS EJES----------------
        kT_diario = pd.concat([kT_diario, self.B_dia], axis=1)
        kT_diario['90-β'] = 90-kT_diario['Prom (β°)'] 
        B_2ejes_d = lambda cos_90_B_d : math.cos(cos_90_B_d* math.pi/180)  # se aplica la formula para calcular angulo H_SRC°
        B_2E_d = kT_diario['90-β'].apply(B_2ejes_d).to_frame()             # la formula devuelve un tipo series, por lo tanto se transforma a frame
        B_2E_d.columns = ['cos(90-β)']                                     # se cambia el nombre de la columna 
        kT_diario=pd.concat([kT_diario, B_2E_d], axis=1)                   # se concatena todos los valores calculados
        #----------------Angulos de conversion montura DOS EJES----------------
        kT_diario['Rd_2Ejes'] = (1+kT_diario['cos(90-β)'])/2
        kT_diario['Rr_2Ejes'] = (1-kT_diario['cos(90-β)'])/2
        #kT_diario['IC_2ejes'] = kT_diario['IBH']*kT_diario['Rb']+kT_diario['I_DH kWh/m^2-dia']*kT_diario['Rd_2Ejes']+ Ro*kT_diario['GHI kWh/m^2-dia']*kT_diario['Rr_2Ejes']
        kT_diario['IC_2ejes2'] = kT_diario['IBH']+kT_diario['I_DH kWh/m^2-dia']*kT_diario['Rd_2Ejes']+ self.Ro*kT_diario['GHI kWh/m^2-dia']*kT_diario['Rr_2Ejes']  
        #------------------- promedio mensual de  GHI e Io----------------------
        self.kT_mensual=pd.concat([GHI_diario, Io_irad], axis=1)
        self.kT_mensual=self.kT_mensual.resample('M').mean()
        self.kT_mensual['kT'] = self.kT_mensual['GHI kWh/m^2-dia']/self.kT_mensual['Io (kWh/m^2)'] # se calcula el kT(indice de claridad mensual)
        self.kT_mensual['I_DH kWh/m^2-dia'] = self.kT_mensual['GHI kWh/m^2-dia']*(1.390-4.027*self.kT_mensual['kT']+5.531*self.kT_mensual['kT']**2-3.108*self.kT_mensual['kT']**3)  # calculo de irradiancia difusa horizontal MENSUAL
        self.kT_mensual['IBH']=self.kT_mensual['GHI kWh/m^2-dia'] - self.kT_mensual['I_DH kWh/m^2-dia'] 
        Rb_m_mensual = Rb_m.resample('M').mean() 
        self.kT_mensual = pd.concat([self.kT_mensual, Rb_m_mensual], axis=1)         # se concatena todos los valores calculados
        #--RADIACION SOLAR TOTAL "DIARIA mensual" EN UNA SUPEFICIE INCLINADA--
        self.kT_mensual['IC'] = self.kT_mensual['IBH']*self.kT_mensual['Rb']+self.kT_mensual['I_DH kWh/m^2-dia']*self.Rd+ self.Ro*self.kT_mensual['GHI kWh/m^2-dia']*self.Rr
        #--------------IC "DIARIO mensual" EN  SEGUIDOR DE DOS EJES------------
        self.kT_mensual = pd.concat([self.kT_mensual, self.B_mes], axis=1)
        self.kT_mensual['90-β'] = 90-self.kT_mensual['Prom (β°)'] 
        B_2ejes = lambda cos_90_B : math.cos(cos_90_B* math.pi/180)     # se aplica la formula para calcular angulo H_SRC°
        B_2E = self.kT_mensual['90-β'].apply(B_2ejes).to_frame()             # la formula devuelve un tipo series, por lo tanto se transforma a frame
        B_2E.columns = ['cos(90-β)']                                    # se cambia el nombre de la columna 
        self.kT_mensual=pd.concat([self.kT_mensual, B_2E], axis=1)                # se concatena todos los valores calculados
        #----------------Angulos de conversion montura DOS EJES----------------
        self.kT_mensual['Rd_2Ejes'] = (1+self.kT_mensual['cos(90-β)'])/2
        self.kT_mensual['Rr_2Ejes'] = (1-self.kT_mensual['cos(90-β)'])/2
        self.kT_mensual['IC_2ejes'] = self.kT_mensual['IBH']+self.kT_mensual['I_DH kWh/m^2-dia']*self.kT_mensual['Rd_2Ejes']+ self.Ro*self.kT_mensual['GHI kWh/m^2-dia']*self.kT_mensual['Rr_2Ejes']

        #--------------IC "DIARIO mensual"  SEGUIDOR DE 1 EJES-----------------
        self.kT_mensual = pd.concat([self.kT_mensual, self.d_mes, self.cos_d_mes], axis=1)
        self.kT_mensual['90-β+d'] = self.kT_mensual['90-β'] + self.kT_mensual['Declinación (δ°)']
        B_1eje = lambda cos_90_B_d : math.cos(cos_90_B_d* math.pi/180)     # se aplica la formula para calcular angulo H_SRC°
        B_1E = self.kT_mensual['90-β+d'].apply(B_1eje).to_frame()             # la formula devuelve un tipo series, por lo tanto se transforma a frame
        B_1E.columns = ['cos(90-β+d)']                                    # se cambia el nombre de la columna 
        self.kT_mensual=pd.concat([self.kT_mensual, B_1E], axis=1)                # se concatena todos los valores calculados
        #----------------Angulos de conversion montura DOS EJES----------------
        self.kT_mensual['Rd_1Eje'] = (1+self.kT_mensual['cos(90-β+d)'])/2
        self.kT_mensual['Rr_1Eje'] = (1-self.kT_mensual['cos(90-β+d)'])/2
        self.kT_mensual['IC_1eje'] = self.kT_mensual['IBH']*self.kT_mensual['coseno (δ°)']+self.kT_mensual['I_DH kWh/m^2-dia']*self.kT_mensual['Rd_1Eje']+ self.Ro*self.kT_mensual['GHI kWh/m^2-dia']*self.kT_mensual['Rr_1Eje']

        return GHI_diario, kT_diario, self.kT_mensual, Rb_m
    
    def ener_Ic_1E (self):
        Ic_1E = self.kT_mensual.filter(items=['IC_1eje'])                  # filtro IC_1eje 
        Ic_1E = self.Temp_prom_mes.Temperatura.astype(object).combine(Ic_1E.IC_1eje , func=self.Potencia)
        Ic_1E = Ic_1E.to_frame()
        Ic_1E.columns = ['Energia prom IC_1eje[kWh]']                 # cambio el nombre de la columna
        Ic_1E = pd.concat([Ic_1E,self.q], axis=1)                          # se concatena todos los valores calculados
        Ic_1E['Energ_IC_1E[kWh]'] = Ic_1E['Energia prom IC_1eje[kWh]']*Ic_1E['dias'] # se 
        Ic_1E = Ic_1E.filter(items=['Energ_IC_1E[kWh]'])

        return Ic_1E
    
    
    def ener_Ic_2E (self):
        Ic_2E = self.kT_mensual.filter(items=['IC_2ejes'])                  # filtro IC_2ejes 
        Ic_2E = self.Temp_prom_mes.Temperatura.astype(object).combine(Ic_2E.IC_2ejes , func=self.Potencia)
        Ic_2E = Ic_2E.to_frame()
        Ic_2E.columns = ['Energia prom IC_2ejes[kWh]']                 # cambio el nombre de la columna
        Ic_2E = pd.concat([Ic_2E,self.q], axis=1)                           # se concatena todos los valores calculados
        Ic_2E['Energ_IC_2E[kWh]'] = Ic_2E['Energia prom IC_2ejes[kWh]']*Ic_2E['dias'] # se 
        Ic_2E = Ic_2E.filter(items=['Energ_IC_2E[kWh]'])

        return Ic_2E
    
    
    def beta_promedio (self):
        
        beta_m = self.ang_concat.filter(items=['coseno (δ°)','seno (H_SR)','H_SR (Radianes)','seno (δ°)'])
        beta_m['prom(sin β°)'] = (self.cos_L*beta_m['coseno (δ°)']*beta_m['seno (H_SR)'] + beta_m['H_SR (Radianes)']*self.sin_L*beta_m['seno (δ°)']) # promedio de (seno  β°)
        #---------------- Se calcula la altitud β (PROMEDIO)--------------------  
        bet_prom = beta_m.filter(items=['prom(sin β°)'])                   # saca los valores de la columna a ser calculada posteriormente
        bet_prom[bet_prom > 1] = 1  
        
        beta_H_prom = lambda bet_prom : math.asin(bet_prom)                # se aplica la formula para calcular seno de β
        B_H_prom = bet_prom['prom(sin β°)'].apply(beta_H_prom).to_frame()    # la formula devuelve un tipo series, por lo tanto se transforma a frame
        B_H_prom.columns = ['Prom (β°)']                                   # se cambia el nombre de la columna
        B_H_prom['Prom (β°)'] = B_H_prom['Prom (β°)']* 180/math.pi         # se transforma a grados el angulo β
        beta_m = pd.concat([beta_m, B_H_prom], axis=1)                     # se concatena la nueva columna calculada al dataframe anterior
        
        return beta_m, bet_prom
    
    
    def temp_promedio (self):
        prom_temp = pd.concat([self.INTER_spl_irrad, self.INTER_spl_temp], axis=1)
        temp_sin_ceros = prom_temp['GHI'] != 0                                # filtro los valores diferentes de cero para escojer los valores de arranque (min) y de parada (max) 
        temp_filt = prom_temp [temp_sin_ceros] 
        temp_filt = temp_filt.filter(items=['Temperatura'])                   # defino los valores diferentes de cero en las fechas correspondientes
        Temp_prom_dia = temp_filt.resample('D').mean()
        Temp_prom_mes = temp_filt.resample('M').mean()
        return Temp_prom_dia, Temp_prom_mes
    
    
    def ener_Ic_tiw (self):
        
        print("................................................................................................")
        print("self.kT_mensual_t")
        print(self.kT_mensual_t)
        
        Ic_tiw = self.kT_mensual_t.filter(items=['IT_Tiw'])                  # filtro IT_Tiw 
        
        print("***************************************************  Ic_tiw")
        print("Ic_tiw")
        print(Ic_tiw)
        
        Ic_tiw = self.Temp_prom_mes.Temperatura.astype(object).combine(Ic_tiw.IT_Tiw , func=self.Potencia)
        
        print("***************************************************  Ic_tiw")
        print("Ic_tiw")
        print(Ic_tiw)
        Ic_tiw = Ic_tiw.to_frame()
        print("***************************************************  Ic_tiw")
        print("Ic_tiw")
        print(Ic_tiw)
        Ic_tiw.columns = ['Energia prom Ic_tiw[kWh]']                 # cambio el nombre de la columna
        print("***************************************************  Ic_tiw")
        print("Ic_tiw")
        print(Ic_tiw)
        Ic_tiw = pd.concat([Ic_tiw, self.q], axis=1)                           # se concatena todos los valores calculados
        print("***************************************************  Ic_tiw")
        print("Ic_tiw")
        print(Ic_tiw)
        Ic_tiw['Energ_IC[kWh]'] = Ic_tiw['Energia prom Ic_tiw[kWh]']*Ic_tiw['dias'] # se 
        print("***************************************************  Ic_tiw")
        print("Ic_tiw")
        print(Ic_tiw)
        Ic_tiw = Ic_tiw.filter(items=['Energ_IC[kWh]'])
        
        print("***************************************************  Ic_tiw Final")
        print("Ic_tiw")
        print(Ic_tiw)

        return Ic_tiw
    
    
    def kt_bdd_tiwari (self,GHI_diario, num_dia, kT_mensual):
    
        print("---------------------------------------------------------------------")
        
        print("GHI_diario")
        print(GHI_diario)
        
        print("---------------------------------------------------------------------")
    
        Io_tiwari = self.ang_tiwari.filter(items=['Io (kWh/m^2)'])                          # filtro Io de ang_tiwari
        Io_tiwari = Io_tiwari.resample('D').mean()                                     # promedio diario de Io
        #------------------- METODO DE TIWARI, calculo de (kT)------------------
        kT_diario_t = pd.concat([GHI_diario, Io_tiwari], axis=1)                       # se concatena la nueva columna calculada al dataframe GHI_diario (calculado inicialmente)
        kT_diario_t['kT'] = kT_diario_t['GHI kWh/m^2-dia']/kT_diario_t['Io (kWh/m^2)'] # se calcula el kT(indice de claridad diario)
        #-------------FORMULAS PARA EL CALCULAR IRRADIACION DIFUSA --------------
        kT_diario_t['I_D1'] = kT_diario_t['GHI kWh/m^2-dia']*0.99
        kT_diario_t['I_D2'] = kT_diario_t['GHI kWh/m^2-dia']*(1.188- 2.272*kT_diario_t['kT']+ 9.473*kT_diario_t['kT']**2- 21.856*kT_diario_t['kT']**3+ 14.648*kT_diario_t['kT']**4)
        kT_diario_t['I_D3'] = kT_diario_t['GHI kWh/m^2-dia']*(-0.5*kT_diario_t['kT']+ 0.632)
        kT_diario_t['I_D4'] = 0.2*kT_diario_t['GHI kWh/m^2-dia']
        #-------------IRRADIACION DIFUSA PARA DIFERENTES CONDICIONES-------------
        kT_diario_t['I1'] = np.where(kT_diario_t['kT']<= 0.17 , kT_diario_t['I_D1'], 0)                           # creacion de una columna 'I1' para rellenar con las condiciones de kT
        kT_diario_t['I2'] = np.where((kT_diario_t['kT']>0.17) & (kT_diario_t['kT']<0.75), kT_diario_t['I_D2'], 0) # creacion de una columna 'I2' para rellenar con las condiciones de kT
        kT_diario_t['I3'] = np.where((kT_diario_t['kT']>0.75) & (kT_diario_t['kT']<0.8), kT_diario_t['I_D3'], 0)  # creacion de una columna 'I3' para rellenar con las condiciones de kT
        kT_diario_t['I4'] = np.where(kT_diario_t['kT']>=0.8, kT_diario_t['I_D4'], 0 )                             # creacion de una columna 'I4' para rellenar con las condiciones de kT
        kT_diario_t['ID_Tiw']=kT_diario_t['I1']+kT_diario_t['I2']+kT_diario_t['I3']+kT_diario_t['I4']             # SE CREA LA COLUMNA (ID_Tiw) que representa la irradiacion difusa despues de pasar las condiciones kT
        
        print("---------------------------------------------------------------------")
        
        print("kT_diario_t")
        print(kT_diario_t)
        
        print("---------------------------------------------------------------------")
        
        #-------------IRRADIACION de HAZ PARA DIFERENTES CONDICIONES-------------
        kT_diario_t['IB_Tiw']=kT_diario_t['GHI kWh/m^2-dia'] - kT_diario_t['ID_Tiw']                              # se encuentra la irradiancia de haz directo en una superficie horizontal
        #-------------ELIMINACION DE COLUMNAS DESPUES DE CONDICIONES-------------
        kT_diario_t=kT_diario_t.drop(['I_D1','I_D2','I_D3','I_D4','I1', 'I2', 'I3', 'I4'],axis=1)                 # elimina las columnas no deseadas de la nueva base de datos, (SE PUEDE COMENTAR ESTA LINEA no afecta)
        #------------------- METODO DE TIWARI, filtro de (Rb)----------------
        Rb_t = self.ang_tiwari.filter(items=['Rb'])                                   # se filtra item Rb, para promediar diariamente
        Rb_t = Rb_t.resample('D').mean()                                         # se promedia diariamente Rb
        kT_diario_t = pd.concat([kT_diario_t, Rb_t], axis=1)                     # se concatena todos los valores calculados
        #-----RADIACION SOLAR TOTAL "DIARIA" EN UNA SUPEFICIE INCLINADA-------
        kT_diario_t['IC'] = kT_diario_t['IB_Tiw']*kT_diario_t['Rb']+kT_diario_t['ID_Tiw']*self.Rd+ self.Ro*kT_diario_t['GHI kWh/m^2-dia']*self.Rr

        #---------------------------- promedio diario----------------------------
        num_dia_mensual = num_dia.resample('D').mean()                        # se extrae solamente el numero de dias del anio
        kT_diario_t = pd.concat([kT_diario_t, num_dia_mensual], axis=1)       # se concatena la columna del numero de dias con el dataframe kT_diario_t
        #--------------------- promedio mensual de  GHI e Io---------------------
        H_promedio = kT_mensual.filter(items=['GHI kWh/m^2-dia'])             # filtro el H promedio calculado en el metodo anterior del dataFrame (kT_mensual)
        H_promedio.index = H_promedio.index.strftime('%Y-%m')                 # se define promedio del idice mensualmente
        dias_promedio = [17,47,75,105,135,162,198,228,258,288,318,344]        # escoge el dia promedio del mes segun tabla 1.4 de Tiwari 
        kT_mensual_t = kT_diario_t[kT_diario_t.n_dia.isin(dias_promedio)]     # la funcion .isin(), permite escoger el numero de dia que propone la tabla 1.4 de tiwari (para los promedios mensuales de Io)
        kT_mensual_t = kT_mensual_t.filter(items=['Io (kWh/m^2)','n_dia','Rb'])    # se extrae las columnas deseadas
        kT_mensual_t.index = kT_mensual_t.index.strftime('%Y-%m')             # se define promedio del idice mensualmente 
        kT_mensual_t = pd.concat([H_promedio, kT_mensual_t], axis=1)          # se concatena (H_promedio, kT_mensual_t)
        kT_mensual_t['kT'] = kT_mensual_t['GHI kWh/m^2-dia']/kT_mensual_t['Io (kWh/m^2)'] # se calcula el kT(indice de claridad mensual)
        kT_mensual_t['I_DH kWh/m^2-dia'] = kT_mensual_t['GHI kWh/m^2-dia']*(1.403 - 1.672*kT_mensual_t['kT'])  # calculo de irradiancia difusa horizontal MENSUAL
        kT_mensual_t['IB_Tiw']=kT_mensual_t['GHI kWh/m^2-dia'] - kT_mensual_t['I_DH kWh/m^2-dia']
        kT_mensual_t['IT_Tiw']=kT_mensual_t['IB_Tiw']*kT_mensual_t['Rb'] + kT_mensual_t['I_DH kWh/m^2-dia']*self.Rd + self.Ro*self.Rr*kT_mensual_t['GHI kWh/m^2-dia']
        #--------------------- ARREGLO DE FECHAS EN kT_mensual_t---------------------
        
        
        
        
        #kT_mensual_t = kT_mensual_t.reset_index()                             # resetea el indice del DataFrame
        
        #kT_mensual_t=kT_mensual_t.reset_index(inplace=True)
        
        
        print("kT_mensual_t")
        print(kT_mensual_t)
        
        print("columns kT_mensual_t")
        print(kT_mensual_t.columns)
        
        
        kT_mensual_t['Fecha']=kT_mensual_t.index
               
        print("***************************************************************")
        
        print("kT_mensual_t")
        print(kT_mensual_t)
        
        print("columns kT_mensual_t")
        print(kT_mensual_t.columns)
        
        kT_mensual_t = kT_mensual_t.reset_index()
        kT_mensual_t = kT_mensual_t.drop(['Fecha'],axis=1)                    # elimina las columnas no deseadas de la nueva base de datos
        
        fecha_mes_tiw = kT_diario_t.filter(items=['n_dia'])
        fecha_prom_MES = fecha_mes_tiw.resample('M').mean()
        fecha_prom_MES = fecha_prom_MES.reset_index()                         # resetea el indice del DataFrame
        fecha_prom_MES = fecha_prom_MES.drop(['n_dia'],axis=1)                # resetea el indice del DataFrame
        print(";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;")
        print("fecha_prom_MES")
        print(fecha_prom_MES)
        fecha_prom_MES=fecha_prom_MES.rename(columns={"index":"Fecha"})
        
        kT_mensual_t = pd.concat([kT_mensual_t, fecha_prom_MES], axis=1)      # se concatena (fecha_prom_MES, kT_mensual_t)
        kT_mensual_t = kT_mensual_t.set_index('Fecha')                        # Se fija la fecha como indice (index)
        
        print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
        print("self.kT_mensual_t")
        print(kT_mensual_t)
        
        return kT_diario_t, kT_mensual_t
    
    def angulos_tiwari (self,n):
    
        #---------------------- Se calcula la declinacion-----------------------
        ang=lambda x : 23.45*math.sin(((360/365)*(284+x)* math.pi)/180)     # se aplica la formula para calcular la declinacion
        delta=n['n_dia'].apply(ang).to_frame()                              # la formula devuelve un tipo series, por lo tanto se transforma a frame
        delta.columns=['Declinación (δ°)']                                  # se cambia el nombre de la columna
        #----------------horas del dia (H) antes del medio dia------------------
        ang_tiwari=pd.concat([n,delta], axis=1)                             # se concatena todos los valores calculados
        ang_tiwari=ang_tiwari.drop(['N hora','N minutos'],axis=1)           # se elimina las columnas 'N minutos','N minutos'
        ang_tiwari['∡ horario (ω°)'] = (ang_tiwari['Horas dia']-12)*15      # se determina el angulo horario ω, 'Horas dia' SON LAS HORAS SOLARES LOCALES
        #------------------------ Se calcula COSENO (ω) ------------------------
        co_w=ang_tiwari.filter(items=['∡ horario (ω°)'])                    # se filtra la columna deseada
        coseno_W=lambda co_w : math.cos(co_w* math.pi/180)                  # se aplica la formula para calcular coseno de ω de la columna filtrada
        cos_W=ang_tiwari['∡ horario (ω°)'].apply(coseno_W).to_frame()       # la formula devuelve un tipo series, por lo tanto se transforma a frame
        cos_W.columns=['coseno (ω°)']                                       # se cambia el nombre de la columna
        #-------------------------- Se calcula SENO (ω) ------------------------
        seno_W=lambda co_w : math.sin(co_w* math.pi/180)                    # se aplica la formula para calcular seno de ω de la columna filtrada
        sin_W=ang_tiwari['∡ horario (ω°)'].apply(seno_W).to_frame()         # la formula devuelve un tipo series, por lo tanto se transforma a frame
        sin_W.columns=['seno (ω°)']                                         # se cambia el nombre de la columna
        #----------------------- Se calcula coseno (δ°) ------------------------
        coseno_d=lambda delta : math.cos(delta* math.pi/180)                # se aplica la formula para calcular coseno de delta
        cos_d=ang_tiwari['Declinación (δ°)'].apply(coseno_d).to_frame()     # la formula devuelve un tipo series, por lo tanto se transforma a frame
        cos_d.columns=['coseno (δ°)']                                       # se cambia el nombre de la columna
        #------------------------ Se calcula SENO (δ°) -------------------------
        seno_d=lambda delta : math.sin(delta* math.pi/180)                  # se aplica la formula para calcular seno de delta
        sin_d=ang_tiwari['Declinación (δ°)'].apply(seno_d).to_frame()       # la formula devuelve un tipo series, por lo tanto se transforma a frame
        sin_d.columns=['seno (δ°)']                                         # se cambia el nombre de la columna
        #------------------------- Se calcula TAN (δ°) -------------------------
        tangente_d=lambda delta : math.tan(delta* math.pi/180)              # se aplica la formula para calcular tangente de delta
        tan_d=ang_tiwari['Declinación (δ°)'].apply(tangente_d).to_frame()   # la formula devuelve un tipo series, por lo tanto se transforma a frame
        tan_d.columns=['tan (δ°)']                                          # se cambia el nombre de la columna
        #-----------Ws ángulo horario de salida del sol (en radianes)----------- 
        H_amanecer = lambda tan_d : math.acos(-self.tan_L*tan_d* math.pi/180)    # se aplica la formula para calcular angulo Ws°
        Ws=ang_tiwari['Declinación (δ°)'].apply(H_amanecer).to_frame()      # la formula devuelve un tipo series, por lo tanto se transforma a frame
        Ws.columns=['Ws (Radianes)']                                        # se cambia el nombre de la columna 
        Ws['(Ws°)'] = Ws['Ws (Radianes)']*180/math.pi                       # se transforma de radianes a grados la columna 'Radianes (Ws)'
        ang_tiwari=pd.concat([ang_tiwari,cos_W,sin_W,cos_d, sin_d, tan_d, Ws], axis=1)   # se concatena todos los valores calculados
        #-------------seno Ws ángulo horario de salida del sol ---------------
        sin_Ws=ang_tiwari.filter(items=['Ws (Radianes)'])  
        seno_WS =lambda sin_Ws : math.sin(sin_Ws)                           # se aplica la formula para calcular angulo Ws°
        sin_W_S=ang_tiwari['Ws (Radianes)'].apply(seno_WS).to_frame()       # la formula devuelve un tipo series, por lo tanto se transforma a frame
        sin_W_S.columns=['seno (Ws)']                                       # se cambia el nombre de la columna 
        ang_tiwari=pd.concat([ang_tiwari,sin_W_S], axis=1)                  # se concatena todos los valores calculados
        #--------------------------COSENO de (θZ °)-----------------------------  
        ang_tiwari['coseno (θZ°)'] = ang_tiwari['coseno (δ°)']*ang_tiwari['coseno (ω°)']*self.cos_L + self.sin_L*ang_tiwari['seno (δ°)'] # se calcula el coseno(θZ°)
        #-------------- Se calcula el cenit θZ (A cualquier hora)---------------  
        tet=ang_tiwari.filter(items=['coseno (θZ°)'])                       # saca los valores de la columna a ser calculada posteriormente
        teta_H=lambda tet : math.acos(tet)                                  # se aplica la formula para calcular arcocoseno de θZ
        T_H=ang_tiwari['coseno (θZ°)'].apply(teta_H).to_frame()             # la formula devuelve un tipo series, por lo tanto se transforma a frame
        T_H.columns=['Cenit (θZ°)']                                         # se cambia el nombre de la columna
        T_H['Cenit (θZ°)'] = T_H['Cenit (θZ°)']* 180/math.pi                # se transforma a grados el angulo θZ
        ang_tiwari=pd.concat([ang_tiwari, T_H], axis=1)                     # se concatena la nueva columna calculada al dataframe anterior
        #--------Insolación extraterrestre media diaria Io (kWh/m^2-día)--------  
        num_dia=ang_tiwari.filter(items=['n_dia'])                          # saca los valores de la columna a ser calculada posteriormente
        I_ex=lambda num_dia : math.cos(((num_dia*360)/365)* math.pi/180)    # se aplica la formula para calcular auxiliar de formula
        Io_aux=ang_tiwari['n_dia'].apply(I_ex).to_frame()                   # la formula devuelve un tipo series, por lo tanto se transforma a frame
        Io_aux.columns=['Aux_ndia']                                         # se cambia el nombre de la columna
        ang_tiwari=pd.concat([ang_tiwari, Io_aux], axis=1)                  # se concatena la nueva columna calculada al dataframe anterior
        SC=1.367                                                            # kW/m^2 constante solar SC=1.377 kW/m^2,   puede ser SC=1.367 kWh/m^2
        ang_tiwari['Io (kWh/m^2)'] = (24/math.pi)*SC*(1+0.033*ang_tiwari['Aux_ndia'] )*(self.cos_L*ang_tiwari['coseno (δ°)']*ang_tiwari['seno (Ws)']+ ang_tiwari['Ws (Radianes)']* self.sin_L*ang_tiwari['seno (δ°)'] )   # se calcula el Io(kW/m^2)
        #------------------Ángulo de incidencia (Cos θi °)----------------------
        ang_tiwari['Coseno (θi)']=(self.cos_L*self.cos_E + self.sin_L*self.sin_E*self.cos_GAMA)*ang_tiwari['coseno (δ°)']*ang_tiwari['coseno (ω°)'] + ang_tiwari['coseno (δ°)']*ang_tiwari['seno (ω°)']*self.sin_E*self.sin_GAMA + ang_tiwari['seno (δ°)']*(self.sin_L*self.cos_E-self.cos_L*self.sin_E*self.cos_GAMA) # se calcula cos θi (angulo de incidencia)
        #---------FACTORES DE CONVERSION SOBRE UNA SUPERFICIE INCLINADA---------
        #ang_tiwari['Rb'] = ang_tiwari['Coseno (θi)']/ang_tiwari['coseno (θZ°)'] # Factor de conversion de radiacion de haz Rb
        #--------W_SRC ángulo horario; salida del sol (PARA EL COLECTOR)------- 
        W_amanecer_c=lambda tan_d : math.acos(-self.tan_LE*tan_d* math.pi/180)    # se aplica la formula para calcular angulo W_SRC°
        W_SRC=ang_tiwari['Declinación (δ°)'].apply(W_amanecer_c).to_frame()  # la formula devuelve un tipo series, por lo tanto se transforma a frame
        W_SRC.columns=['W_SRC (Radianes)']                                   # se cambia el nombre de la columna 
        W_SRC['(W_SRC°)'] = W_SRC['W_SRC (Radianes)']*180/math.pi            # se transforma de radianes a grados la columna 'Radianes (W_SRC)'
        ang_tiwari=pd.concat([ang_tiwari, W_SRC], axis=1)                    # se concatena todos los valores calculados
        #-------------------W_SRC mínimo (PARA EL COLECTOR)---------------------
        ang_tiwari['W_SRC min'] = np.where(ang_tiwari['Ws (Radianes)'] < ang_tiwari['W_SRC (Radianes)'] , ang_tiwari['Ws (Radianes)'], ang_tiwari['W_SRC (Radianes)'])        # creacion de una columna 'W_SRC min' para rellenar con las condiciones de W_SRC (mínimo)
        #------------seno W_SRC ángulo horario de salida del sol ---------------
        sin_Wsrc=ang_tiwari.filter(items=['W_SRC min'])                      # filtra los valores de la columna a ser calculada posteriormente
        seno_WSRC =lambda sin_Wsrc : math.sin(sin_Wsrc)                      # se aplica la formula para calcular seno de W_SRC°
        sin_W_SRC=ang_tiwari['W_SRC min'].apply(seno_WSRC).to_frame()        # la formula devuelve un tipo series, por lo tanto se transforma a frame
        sin_W_SRC.columns=['seno (W_SRC)']                                   # se cambia el nombre de la columna 
        ang_tiwari=pd.concat([ang_tiwari,sin_W_SRC], axis=1)                 # se concatena todos los valores calculados
        
        #---------FACTORES DE CONVERSION SOBRE UNA SUPERFICIE INCLINADA---------
        ang_tiwari['Rb'] = (self.cos_LE*ang_tiwari['coseno (δ°)']*ang_tiwari['seno (W_SRC)'] + ang_tiwari['W_SRC min']*self.sin_LE*ang_tiwari['seno (δ°)'])/(self.cos_L*ang_tiwari['coseno (δ°)']*ang_tiwari['seno (Ws)'] + ang_tiwari['Ws (Radianes)']*self.sin_L*ang_tiwari['seno (δ°)']) # Factor de conversion de radiacion de haz Rb
        
        
        
        
        
        return ang, ang_tiwari, cos_d, sin_d, cos_W, sin_W, co_w, tet, sin_Ws, num_dia, sin_Wsrc #, aci      # Valores que retorna la funcion
        

 #####################################################################################################################
 #####################################################################################################################
 #####################################################################################################################
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
