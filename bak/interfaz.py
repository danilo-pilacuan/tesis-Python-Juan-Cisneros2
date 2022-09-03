#import sirve para cargar las librerias y usar sus funciones
import tkinter as tk   #cargar libreria de interfaz grafica

from tkinter import filedialog as fd  #cargar libreria para buscar archivos
import matplotlib #cargar libreria para crear graficos
matplotlib.use('TkAgg') #configurar graficos para mostrar en ventanas
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  #configuracion adicional para mostrar los graficos en ventanas
from matplotlib.figure import Figure #configuracion adicional para mostrar los graficos en ventanas


from cmath import nan #librería para manejar datos exportados no numericos (nan (Not is a number) se produce al importar desde excel y si el dato contiene errores se importan como no numerico) 
import pandas as pd      #pandas es una libreria para el manejo de grandes volumenes de datos
import numpy as np #es una libreria para la realizacion de operaciones matematicas entre variables y que tambien permite usar matrices y vectores

from os import listdir #OS listdir es la libreria que nos permite acceder a los archivos del sistema operativo
from os.path import isfile, join  #libreria para acceder a las carpetas donde se guardan los archivos de excel

from scipy.interpolate import Rbf, InterpolatedUnivariateSpline #se carga las funciones para realizar interpolacion de curvas (se usa para interpolar la curva del fabricante)
import csv  #libreria para cargar datos de excel o separados por comas

class App: #ventana principal
    def __init__(self, window, window_title): #inicializara la ventana
        self.filename="null" #variable para hacer referencia a el nombre del archivo excel que se analizará del mes escogido

        self.window = window #se definen las propiedades de la ventana
        self.window.geometry("900x630") #se define el taño inicial en pixeles
        self.window.title(window_title) #se define el titulo de la ventana

        self.gradoPoli=3 #variable para almacenar el grado del polinomio para la regresion, por defecto se inicializa en 3

        self.content = tk.Frame(self.window, padx=10,pady=10) #cuadro que permite almacenar controles (botones,texto,graficos)
        #self.frame = tk.Frame(self.content, borderwidth=5, relief="ridge", width=200, height=100)

        #cuando se crea un frame recibe (elementoPadre,borde,tipo borde)
        self.frameComandos = tk.Frame(self.content, borderwidth=5, relief="ridge") #cuadro que almacena los comandos de la ventana
        self.frameExaminar = tk.Frame(self.frameComandos, borderwidth=5, relief="ridge") #cuadro para almacenar botones de control

        self.frameGraficos = tk.Frame(self.content, borderwidth=5, relief="ridge") #cuadro para almacenar los graficos de la ventana
        self.frameGrafico1 = tk.Frame(self.frameGraficos, borderwidth=5, relief="ridge") #cuadro para almacenar el grafico 1
        self.frameGrafico2 = tk.Frame(self.frameGraficos, borderwidth=5, relief="ridge") #cuadro para almacenar el grafico 1
        self.frameGrafico3 = tk.Frame(self.frameGraficos, borderwidth=5, relief="ridge") #cuadro para almacenar el grafico 1
        self.frameGrafico4 = tk.Frame(self.frameGraficos, borderwidth=5, relief="ridge") #cuadro para almacenar el grafico 1
        
        #cuando se crea un objeto recibe (elementoPadre,...)
        self.labelTitulo=tk.Label(self.content,text='ESCUELA POLITÉCNICA NACIONAL FACULTAD DE INGENIERÍA ELÉCTRICA Y ELECTRÓNICA\nDETERMINACIÓN DE CURVA DE RENDIMIENTO AEROGENERADOR\nCENTRAL VILLONACO',font=('times', 10, 'bold'))

        self.labelSeleccionar=tk.Label(self.frameExaminar,text="Seleccione archivo:") #etiqueta labelSeleccionar
        self.botonExaminar = tk.Button(self.frameExaminar, text="Examinar...", command=self.abrirExcel) #boton examinar excel, command sirve para llamar a una funcion

        self.labelAnalisis=tk.Label(self.frameExaminar,text="Mostrar Análisis:") #etiqueta para mostrar analisis
        self.botonAbrirAnalisis = tk.Button(self.frameExaminar, text="Mostrar", command=self.abrirAnalisis) #boton abrir analisis

        self.labelGrado=tk.Label(self.frameExaminar,text="Grado Polinomio") #etiqueta para mostrar el texto grado polinomio

        #self.labelPol=tk.Label(self.frameExaminar,text="Polinomio Resultante")

        #self.textVarPoly=tk.StringVar()
        #self.textVarPoly.set("")
        #self.labelPolRes=tk.Label(self.frameExaminar,textvariable=self.textVarPoly, anchor='w',font=("Courier New", 12))

        self.sliderGrado = tk.Scale(self.frameExaminar,from_=3,to=8, orient=tk.HORIZONTAL,command=self.updateSlider) #barra deslizante para escoger un valor

        self.content.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))       #configurar grid de la ventana y escoger como se manipulan los elementos
        
        self.labelTitulo.grid(column=0, row=0, columnspan=5, sticky=(tk.N,tk.E,tk.W), padx=5) #configurar comportamiento de la ventana
        #self.frame.grid(column=0, row=1, columnspan=8, rowspan=2, sticky=(tk.N, tk.S, tk.E, tk.W))
        
        self.frameGraficos.grid(column=1, row=1, columnspan=7, rowspan=2, sticky=(tk.N, tk.S, tk.E, tk.W))

        self.frameComandos.grid(column=0, row=1, sticky=(tk.N, tk.S, tk.E, tk.W))

        self.frameExaminar.grid(column=0, row=0, sticky="NSEW")
        self.labelSeleccionar.grid(column=0, row=0, sticky="NSEW")
        self.botonExaminar.grid(column=0, row=1, sticky="NSEW")
        self.labelAnalisis.grid(column=0, row=2, sticky="NSEW")
        self.botonAbrirAnalisis.grid(column=0, row=3, sticky="NSEW")

        self.labelGrado.grid(column=0,row=4,sticky="NSEW")
        self.sliderGrado.grid(column=0,row=5,sticky="NSEW")

        # self.labelPol.grid(column=0,row=6,sticky="W")
        # self.labelPolRes.grid(column=0,row=7,sticky="W")

        self.frameComandos.columnconfigure(0,weight=1)
        self.frameExaminar.columnconfigure(0,weight=1)

        self.frameExaminar.rowconfigure(0,weight=1)
        self.frameExaminar.rowconfigure(1,weight=1)
        self.frameExaminar.rowconfigure(2,weight=1)
        self.frameExaminar.rowconfigure(3,weight=1)
        self.frameExaminar.rowconfigure(4,weight=1)
        self.frameExaminar.rowconfigure(5,weight=1)
        self.frameExaminar.rowconfigure(6,weight=1)
        self.frameExaminar.rowconfigure(7,weight=1)

        self.window.columnconfigure(0, weight=1)
        self.window.rowconfigure(0, weight=1)

        # self.one.grid(column=0, row=3)
        # self.two.grid(column=1, row=3)
        # self.three.grid(column=2, row=3)
        # self.ok.grid(column=3, row=3)
        # self.cancel.grid(column=4, row=3)

        self.figura1 = Figure(figsize=(2,2)) #se crea una figura para que se pueda hacer un plot en el frameGrafico1
        self.subpltFigura1 = self.figura1.add_subplot() #se crea un subplot
        #self.subpltFigura1.invert_yaxis()

        self.figura2 = Figure(figsize=(2,2))
        self.subpltFigura2 = self.figura2.add_subplot()
        #self.subpltFigura2.invert_yaxis()

        self.figura3 = Figure(figsize=(2,2))
        self.subpltFigura3 = self.figura3.add_subplot()
        #self.subpltFigura3.invert_yaxis()

        self.figura4 = Figure(figsize=(2,2))
        self.subpltFigura4 = self.figura4.add_subplot()
        #self.subpltFigura4.invert_yaxis()

        ##Agregar titulos a los plots
        self.subpltFigura1.set_title ("Potencia vs Viento", fontsize=8) #configurar titulos de los plots
        self.subpltFigura1.set_ylabel("Potencia", fontsize=8)
        self.subpltFigura1.set_xlabel("Viento", fontsize=8)
        
        self.canvas1 = FigureCanvasTkAgg(self.figura1, master=self.frameGrafico1) #configurar graficos en la ventana
        self.canvas1.get_tk_widget().grid(column=0,row=0, sticky="NSEW")

        self.canvas2 = FigureCanvasTkAgg(self.figura2, master=self.frameGrafico2)
        self.canvas2.get_tk_widget().grid(column=0,row=0, sticky="NSEW")

        self.canvas3 = FigureCanvasTkAgg(self.figura3, master=self.frameGrafico3)
        self.canvas3.get_tk_widget().grid(column=0,row=0, sticky="NSEW")

        self.canvas4 = FigureCanvasTkAgg(self.figura4, master=self.frameGrafico4)
        self.canvas4.get_tk_widget().grid(column=0,row=0, sticky="NSEW")

        self.frameGrafico1.grid(column=0,row=0, sticky="NSEW")
        self.frameGrafico2.grid(column=1,row=0, sticky="NSEW")
        self.frameGrafico3.grid(column=0,row=1, sticky="NSEW")
        self.frameGrafico4.grid(column=1,row=1, sticky="NSEW")
        
        self.frameGrafico1.columnconfigure(0,weight=1)
        self.frameGrafico2.columnconfigure(0,weight=1)
        self.frameGrafico3.columnconfigure(0,weight=1)
        self.frameGrafico4.columnconfigure(0,weight=1)
        
        self.frameGrafico1.rowconfigure(0,weight=1)
        self.frameGrafico2.rowconfigure(0,weight=1)
        self.frameGrafico3.rowconfigure(0,weight=1)
        self.frameGrafico4.rowconfigure(0,weight=1)

        self.frameGraficos.columnconfigure(0,weight=1)
        self.frameGraficos.columnconfigure(1,weight=1)
        self.frameGraficos.rowconfigure(0,weight=1)
        self.frameGraficos.rowconfigure(1,weight=1)

        self.content.columnconfigure(0, weight=1)
        self.content.columnconfigure(1, weight=2)
        self.content.columnconfigure(2, weight=2)
        self.content.columnconfigure(3, weight=2)
        self.content.columnconfigure(4, weight=2)
        self.content.columnconfigure(5, weight=2)
        self.content.columnconfigure(6, weight=2)
        self.content.columnconfigure(7, weight=2)
        self.content.rowconfigure(1, weight=1)

        self.window.mainloop()  #una vez establecida la estructura de la ventana, mostrarla en pantalla

    def updateSlider(self,val):
        self.plot1() #cada vez que se actualiza el valor del slider, cambia el grado de polinomio, volver a graficas

    def abrirExcel(self):
        filetypes = (
            ('Excel Files', '*.xlsx'),
            ('All files', '*.*')
        ) #configurar cuadro de dialogo, para escoger un archivo, solo se permitira archivos de excel
        self.filename = fd.askopenfilename( #en filename se almacena el valor del nombre del archivo abierto
        title='Abrir Archivo',
        filetypes=filetypes)  #cuando se llama a askopenfilename 

        self.plot1()  #se llama a la funcion plot1, que se encarga de graficar el procesamiento realizado al archivo seleccionado

    def abrirAnalisis(self): #se ejecuta cuando se presiona el boton abrir analisis
        exec(open("./regresionPolyfit.py").read()) #ejecutar el archivo regresionPolyfit

    def plot1 (self): #funcion que se encargara del procesamiento del archivo excel y de graficar el resultado
    
        #print(self.filename)
        dataGenerador=pd.DataFrame()  #dataGenerador será un dataframe para almacenar las lecturas de todas las unidades del archivo excel

        dataGenerador=pd.read_excel (self.filename,usecols="B,C,D,F") #leemos el excel
        dataGenerador=dataGenerador.rename(columns={"Avg Theory active power(kW)":"Avg Active Power (kW)"}) #normalizamos los nombres de las columnas

        dataGenerador=dataGenerador.sort_values(by=["Avg Wind Speed(m/s)"])        #ordenamos en funcion de la velocidad del viento, de menor a mayor

        #print(dataGenerador)
        
        self.subpltFigura1.clear()  #en subpltFigura1, se grafica los datos originales en el plot1
        self.subpltFigura1.set_title ("Potencia vs Viento", fontsize=8)
        self.subpltFigura1.set_ylabel("Potencia", fontsize=8)
        self.subpltFigura1.set_xlabel("Viento", fontsize=8) #configuramos los titulos del plot

        self.subpltFigura1.scatter(dataGenerador["Avg Wind Speed(m/s)"],dataGenerador["Avg Active Power (kW)"]) # ploteamos la lectura inicial de datos
        self.canvas1.draw() #el plot no se grafica hasta ejecutar canvas1.draw

        dataGenerador=dataGenerador[dataGenerador["Avg Wind Speed(m/s)"]>=0] #Eliminacion de los valores de lecturas de viento menores al valor minimo de viento
        dataGenerador=dataGenerador[dataGenerador["Avg Wind Speed(m/s)"]<=16] #Eliminacion de los valores de lecturas de viento mayores al valor maximo de viento

        dataGenerador=dataGenerador[dataGenerador["Avg Active Power (kW)"]>=0] #Eliminamos potencias negativas
        dataGenerador=dataGenerador[dataGenerador["Avg Active Power (kW)"]<=1500]  #Eliminamos potencias mayores a la capacidad del generador

        maxWind=dataGenerador["Avg Wind Speed(m/s)"].max() #para la creacion de los intervalos calculamos el maximo de viento
        minWind=dataGenerador["Avg Wind Speed(m/s)"].min() #calculamos el minimo

        NPaquetes=50 #variable para almacenar el numero de paquetes que se desea
        intervalos=np.linspace(minWind,maxWind,NPaquetes+1) #creamos un rango de intervalos para empaquetar los datos de viento

        listaDF=[]  #creamos una lista para almacenar los paquetes

        for i in range(0,intervalos.size-1): #se va de 0 a NPaquetes-1
            if i==intervalos.size-2: 
                listaDF.append(dataGenerador[(dataGenerador["Avg Wind Speed(m/s)"]>=intervalos[i]) & (dataGenerador["Avg Wind Speed(m/s)"]<=intervalos[i+1])])  
            else:
                listaDF.append(dataGenerador[(dataGenerador["Avg Wind Speed(m/s)"]>=intervalos[i]) & (dataGenerador["Avg Wind Speed(m/s)"]<intervalos[i+1])]) #creacion de los paquetes

        for i in range(0,intervalos.size-1): #se iterara cada uno de los paquetes para eliminar los valores atipicos de cada paquete
            if not listaDF[i].empty: #se ejecuta solo si el paquete no esta vacio
                Q1 = np.percentile(listaDF[i]["Avg Active Power (kW)"], 25,method= 'midpoint') #obtencion de primer quartil
                Q3 = np.percentile(listaDF[i]["Avg Active Power (kW)"], 75,method= 'midpoint') #obtencion de tercer quartil

                IQR=Q3-Q1 #Calculo del rango intercuartil
                listaDF[i]=listaDF[i][listaDF[i]["Avg Active Power (kW)"]>=(Q1-1.5*IQR)]  #Eliminacion de atipos inferiores
                listaDF[i]=listaDF[i][listaDF[i]["Avg Active Power (kW)"]<=(Q3+1.5*IQR)] #Eliminacion de atipos superiores   

        dataNoOutliers=pd.DataFrame() #creacion de tabla sin valores atipos
        for i in range(0,intervalos.size-1):  #iteramos todos los paquetes
            dataNoOutliers=pd.concat([dataNoOutliers,listaDF[i]]) #los vamos concatenado en una sola tabla (datos sin atipicos por cuartiles)

        wind=dataNoOutliers["Avg Wind Speed(m/s)"].to_numpy() #obtenemos en la variable auxiliar wind lo valores de viento con los atipicos eliminados con criterio intercuartil
        power=dataNoOutliers["Avg Active Power (kW)"].to_numpy() #obtenemos en la variable auxiliar power lo valores de potencia con los atipicos eliminados con criterio intercuartil
        
        dataWP=np.column_stack((wind,power)) #se hace una tabla con ambas variables auxiliares wind y power

        dataMeans=np.mean(dataWP,axis=0) #obtenemos la media  de los datos

        listaMH=[] #auxiliar para almacenar los valores de distancia de mahalanobis de cada dato

        dfLen=len(dataNoOutliers.index) #variable para almacenar la longitud de la tabla (cuantas filas hay)

        umbralAtipico=0 #declaracion de umbral de evaluacion
        porcentajeMH=0.85 #porcentaje de distancia de mahalanobis al centro de masa de los datos

        auxDataWP=np.transpose(dataWP) #auxiliar para almacenar los valores de viento y potencia con distancias MH temporales
        matrizCov=np.cov(auxDataWP,bias=False) #matriz de covarianza de los datos
        matrizCovInv=np.linalg.inv(matrizCov) #Calculo de la matriz de covarianza inversa
        for j in range(0,dfLen-1): #iteracion uno a uno de los datos para el calculo de distancia de Mahalanobis
            muestraWP=dataWP[j] #muestra WP es una variable temporal que almacena una muestra de viento y su correspondiente potencia generada
            muestraWPmMeans=muestraWP-dataMeans #resta entre el dato menos la media (vector unidimensional)
            aux1=np.dot(muestraWPmMeans,matrizCovInv) #obtencion del producto matricial entre la matriz de covarianza y la resta del dato menos la media
            aux2=np.dot(aux1,np.transpose(muestraWPmMeans)) #obtencion del producto punto entre aux1 y resta entre el dato menos la media (vector unidimensional)
            distMH=np.sqrt(aux2)  #obtencion de raiz cuadrada para calcular la distancia MH
            distMH=np.reshape(distMH,-1) #se aplica reshape porque np.dot y np.sqrt se devuelve un vector unidimensional y se realiza un casting para que distMH sea un valor numerico escalar
            listaMH.append(distMH[0])  #se almacena el valor de distancia de MH en listaMH

        maxMH=max(listaMH) #se obtiene la distancia MH maxima
        umbralAtipico=maxMH*porcentajeMH #umbral atipico significa que los valores con una distancia MH > la distancia maxima * porcentajeMH
        for j in range(0,dfLen-1): #iteracion uno a uno de los datos filtrados con metodo intercuartil
            if listaMH[j]>umbralAtipico: #comparamos la distancia de Mahalanobis de cada dato contra el umbral de Atipicos
                dataNoOutliers["Avg Wind Speed(m/s)"]=dataNoOutliers["Avg Wind Speed(m/s)"].replace(dataNoOutliers["Avg Wind Speed(m/s)"].iloc[j],np.nan) #si el valor es mayor al umbral atipico es un dato no valido por lo cual se lo marca como nan
        dataNoOutliers=dataNoOutliers.dropna() #eliminar Nans de la tabla, dataNoOutliers es la tabla final
        
        
        
        
        ##################################################  Regresion ####################
        dfBuffer = pd.read_csv('bufferData.csv')  #lectura de archivo buffer que contiene los datos procesados para extraer los atipicos
        dataWindBuffer=dfBuffer["dataWind"].to_numpy() #extraccion de datos de viento no atipicos desde la variable que dfBuffer
        dataPowerBuffer=dfBuffer["dataPower"].to_numpy() #extraccion de datos de potencia no atipicos desde la variable que dfBuffer       
        self.gradoPoli=self.sliderGrado.get()
        z=np.polyfit(dataWindBuffer,dataPowerBuffer,self.gradoPoli) #ajuste polinomico para generacion de la curva de datos procesados

        p=np.poly1d(z) #creacion de predictor con polinomio de regresion de ajuste polinomico

        

        print("Polinomio Regresión curva datos no atipicos") #impresion de polinomio con regresion
        print(np.poly1d(z)) #impresion de polinomio

        # p_lines = str(np.poly1d(z)).splitlines()
        # lineaExponentes=p_lines[0]
        # lineaPoly=p_lines[1]
        # #print(.split(" "))
        # exps=[]
        # contElement=0
        # for element in range(0,len(lineaExponentes)):
        #     if(lineaExponentes[element].isdigit()):
        #         exps.append(lineaExponentes[element])
        #         contElement=contElement+1
        # #print("Exps---------------")
        # #print(exps)
        # stringExps=" "
        # contElement=0
        # for element in range(0,len(lineaPoly)):
        #     print(lineaPoly[element])
        #     if(lineaPoly[element]=="x"):
        #         stringExps=stringExps+exps[contElement]
        #         contElement=contElement+1
        #         if contElement==len(exps):
        #             break
        #     else:
        #         stringExps=stringExps+" "
        
        # resPol = "\n\n\nA{}\n{}".format(stringExps, lineaPoly)

        # print("ResPol")
        # print(resPol)

        # resPol2=str(np.poly1d(z))

        # self.textVarPoly.set(resPol)



        dataWindRegresion=dataNoOutliers["Avg Wind Speed(m/s)"]

        #print(dataNoOutliers["Avg Wind Speed(m/s)"])

        dataPowerRegresion=p(dataWindRegresion) #calculo de valores para la curva de potencia para los datos de procesamiento de acuerdo al polinomio de ajuste
        

        dfCurvaReal = pd.read_csv('datosCurvaReal.csv') #lectura de archivo que contiene los datos de la curva del fabricante

        dataWindCR=dfCurvaReal["dataWind"].to_numpy() #extraccion de datos de viento desde la variable que almacena los datos de la curva del fabricante
        dataPowerCR=dfCurvaReal["dataPower"].to_numpy() #extraccion de datos de potencia desde la variable que almacena los datos de la curva del fabricante        

        dataWindCR=dfCurvaReal["dataWind"].to_numpy() #extraccion de datos de viento desde la variable que almacena los datos de la curva del fabricante
        dataPowerCR=dfCurvaReal["dataPower"].to_numpy() #extraccion de datos de potencia desde la variable que almacena los datos de la curva del fabricante        

        fCurvaReal = Rbf(dataWindCR, dataPowerCR,function="cubic",fill_value="extrapolate") #interpolacion de la curva del fricante

        dataWindCR=dataWindRegresion #calculo de la curva real (fabricante)
        dataPowerCR=fCurvaReal(dataWindCR)

        # indicesEliminar1=np.where(dataWindCR<np.amin(dataNoOutliers["Avg Wind Speed(m/s)"]))
        # #print("indicesEliminar1")
        # #print(indicesEliminar1)
        # maxPosIE1=np.amax(indicesEliminar1)
        # dataWindCR=dataWindCR[maxPosIE1+1:len(dataWindCR)]
        # dataPowerCR=dataPowerCR[maxPosIE1+1:len(dataPowerCR)]
        
        # indicesEliminar2=np.where(dataWindRegresion<np.amin(dataNoOutliers["Avg Wind Speed(m/s)"]))
        # #print("indicesEliminar2")
        # #print(indicesEliminar2)
        # maxPosIE2=np.amax(indicesEliminar2)
        # dataWindRegresion=dataWindRegresion[maxPosIE2+1:len(dataWindRegresion)]
        # dataPowerRegresion=dataPowerRegresion[maxPosIE2+1:len(dataPowerRegresion)]

        

        self.subpltFigura2.clear() #plotear el grafico 2
        self.subpltFigura2.scatter(dataNoOutliers["Avg Wind Speed(m/s)"],dataNoOutliers["Avg Active Power (kW)"]) # ploteamos la lectura inicial de datos
        self.subpltFigura2.plot(dataWindRegresion, dataPowerRegresion, 'r') #graficacion de la curva de regresion de los datos no atipicos
        self.subpltFigura2.plot(dataWindCR, dataPowerCR, 'g') #graficacion de la curva de potencia del fabricante

        self.subpltFigura2.set_title ("Eliminación Atípicos", fontsize=8) #configuramos los titulos y etiquetas del plot
        self.subpltFigura2.set_ylabel("Potencia", fontsize=8)
        self.subpltFigura2.set_xlabel("Viento", fontsize=8)
        self.subpltFigura2.legend(['Datos no atípicos', 'Regresion curva datos no atípicos','Curva fabricante','Regresión curva fabricante'],loc='upper left') #impresion de identificadores (legend) de cada curva en el plot
        self.canvas2.draw()

        #############################################

        auxPowerNoOutliers=dataNoOutliers["Avg Active Power (kW)"].to_numpy() #se crea dos arrays, el array con la potencia leida del excel, potencia medida
        #print("auxPowerNoOutliers")
        #print(auxPowerNoOutliers)
        arrayErrorRelCR=dataPowerRegresion*0 #se crea otro array para almacenar los valores de error

        #print("arrayErrorRelCR")
        #print(arrayErrorRelCR)

        for iterWind in range(0,len(auxPowerNoOutliers)): #iteramos cada uno de los valores de potencia medidos
            arrayErrorRelCR[iterWind]=((dataPowerCR[iterWind]-auxPowerNoOutliers[iterWind])/dataPowerCR[iterWind])*100  #se calcula el error relativo para la potencia medida vs curva fabricante

        auxPowerNoOutliers=dataNoOutliers["Avg Active Power (kW)"].to_numpy()  #se crea dos arrays, el array con la potencia calculada con la regresion
        #print("auxPowerNoOutliers")
        #print(auxPowerNoOutliers)
        arrayErrorRelRegresion=dataPowerRegresion*0  #se crea otro array para almacenar los valores de error

        #print("arrayErrorRelCR")
        #print(arrayErrorRelCR)

        for iterWind in range(0,len(auxPowerNoOutliers)): #iteramos cada uno de los valores de potencia calculados con la regresion
            arrayErrorRelRegresion[iterWind]=((dataPowerRegresion[iterWind]-auxPowerNoOutliers[iterWind])/dataPowerRegresion[iterWind])*100  #se calcula el error relativo para la potencia medida vs curva fabricante
        
        self.subpltFigura3.clear() #borrar plot anterior plotear el grafico 3
        self.subpltFigura3.set_title ("Error Respecto a Curva del Fabricante", fontsize=8)
        self.subpltFigura3.set_ylabel("Error", fontsize=8)
        self.subpltFigura3.set_xlabel("Viento", fontsize=8)
        self.subpltFigura3.plot(dataNoOutliers["Avg Wind Speed(m/s)"], arrayErrorRelCR, 'r') #graficacion de la curva de error con respecto a la curva real del fabricante
        self.subpltFigura3.plot(dataNoOutliers["Avg Wind Speed(m/s)"], arrayErrorRelRegresion, 'g') #graficacion de la curva de error con respecto a la curva regresion
        self.subpltFigura3.legend(['Error Relativo Respecto a Curva del Fabricante', 'Error Relativo Respecto a Regresion'],loc='upper right')
        self.canvas3.draw()
        
        #############################################

        auxPowerNoOutliers=dataNoOutliers["Avg Active Power (kW)"].to_numpy()  #se crea dos arrays, el array con la potencia de la curva real y la segunda la potencia de la curva regresion

        arrayErrorRelRegresion=dataPowerRegresion*0 #creamos array para almacenar los valores de error relativo de curva real vs curva regresion

        #print("arrayErrorRelCR")
        #print(arrayErrorRelCR)

        for iterWind in range(0,len(auxPowerNoOutliers)): #iteramos cada uno de los valores de potencia real vs potencia regresion
            arrayErrorRelRegresion[iterWind]=((dataPowerRegresion[iterWind]-dataPowerCR[iterWind])/dataPowerRegresion[iterWind])*100 #se calcula el error relativo entre la curva real vs curva regresion
        
        self.subpltFigura4.clear() #borrar plot anterior plotear el grafico 3
        self.subpltFigura4.set_title ("Error relativo Curva Real vs Curva Regresion", fontsize=8)
        self.subpltFigura4.set_ylabel("Error", fontsize=8)
        self.subpltFigura4.set_xlabel("Viento", fontsize=8)

        self.subpltFigura4.plot(dataNoOutliers["Avg Wind Speed(m/s)"], arrayErrorRelRegresion, 'purple') #graficacion de la curva de error entre curva real y cura regresion
        self.canvas4.draw()

        # mse = (np.square(auxPowerNoOutliers - dataPowerRegresion)).mean()   #calculo del error cuadratico medio

        # print("MSE: "+str(mse)) #impresion del MSE

        
#definimos el metodo main, el cual se encarga de crear la ventana que esta contenida en la clase app       
       
def main():    #metodo main
    App(tk.Tk(),'Determinación Curva Rendimiento Generador Eólico') #cargar ventana

main() #llamado a ejecucion del metodo main