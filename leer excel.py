# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 14:53:33 2021

@author: jan-c
"""
#  https://nsrdb.nrel.gov/   (PAGINA DE DESCARGAS DE NREL) BORRAR EL COMENTARIO
#  http://www.quitoambiente.gob.ec/index.php/inicio   (Pagina secretaria del ambiente), entrar en RED DE MONITOREO ATMOSFÉRICO
#  https://tuluzsolar.com/products/panel-solar-risen-450w-monocristalino-144-celulas , (FICHAS DE PANELES SOLARES)

import pandas as pd
import tkinter as tk
from tkinter import messagebox, Canvas, Button#, Frame
#from tkinter import *            #libreria para fondo de pantalla importa todas las librerias de tkinter como Button, Entry, Frame, Label, Tk etc....
from tkinter import Label        #libreria para importar espeficamente la etiqueta
from PIL import ImageTk, Image   #libreria para fondo de pantalla
from scipy.interpolate import splrep, BSpline, splev    #Libreria que permite interpolar valores
import matplotlib.pyplot as plt  #libreri que permite graficar
import numpy as np
import math
from scipy import integrate
from scipy import stats
from windrose import WindroseAxes
import matplotlib.cm as cm

#import scipy.stats as s


#import scipy.integrate as sci


#import sympy as sp


#from scipy.integrate import quad
#from sympy.abc import z
#from sympy import symbols

#from datetime import datetime
import seaborn as sbn
sbn.set(rc={'figure.figsize':(10, 5)})

#import sympy
#from matplotlib.figure import Figure 
#from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  NavigationToolbar2Tk) 


#---------------FUNCIONES A SER LLAMADAS PARA LOS SUB-MENUS------------------
def mensaje():                                                                   #funcion para mensaje de cerrar ventana
    respuesta_salida=messagebox.askyesno("SALIR","¿Desea salir?")
    if (respuesta_salida):
        ventana.destroy()
#------------------ventanas secundarias métodos USADOS-----------------------
def f_masters():
    #ventana.withdraw()                                   #cierra la ventana principal
    V_masters=tk.Toplevel()                              #Abre la ventana secundaria
    V_masters.title('MÉTODO DE MASTERS')                 #titulo de la ventana
    V_masters.geometry('600x300')                        #tamaño de la ventana 600x300
    V_masters.iconbitmap('BUHO_EPN_big.ico')             #ingreso del icono en la ventana
    
    mi_menu_master=tk.Menu(V_masters)                    #creacion de menu en la subventana con una nueva variable 'mi_menu_master'
    
    menu_solar_master=tk.Menu(mi_menu_master, tearoff=0) #creacion de sub-menu en la ventana con la nueva variable 'mi_menu_master'.....tearoff=0 sirve para corregir error del submenu
    menu_solar_master.add_command(label='Opcion 1')      #Opciones del menú
    menu_solar_master.add_command(label='Opcion 2')      #Opciones del menú
    mi_menu_master.add_cascade(label='metodo', menu=menu_solar_master)   #nombre de la opcion principal para sub-menu
    
    fondo_solar1=ImageTk.PhotoImage(Image.open ('energía-solare-1.jpg').resize((600, 300)))
    fondo_s1=Label(V_masters, image=fondo_solar1)
    fondo_s1.image = fondo_solar1                        # ojo realizar la igualacion para la visualizacion del fondo en ventana secundaria
    fondo_s1.pack()
    
    V_masters.config(menu=mi_menu_master)
    
    
    

def f_tiwari():
    #ventana.withdraw()                           #cierra la ventana principal
    V_tiwari=tk.Toplevel()                       #Abre la ventana secundaria
    V_tiwari.title('MÉTODO DE TIWARI')           #titulo de la ventana
    V_tiwari.geometry('600x300')                 #tamaño de la ventana 600x300
    V_tiwari.iconbitmap('BUHO_EPN_big.ico')      #ingreso del icono en la ventana
    
def f_cronologico():
    #ventana.withdraw()                           #cierra la ventana principal
    V_cronologico=tk.Toplevel()                  #Abre la ventana secundaria
    V_cronologico.title('MÉTODO CRONOLÓGICO')    #titulo de la ventana
    V_cronologico.geometry('600x300')            #tamaño de la ventana 600x300
    V_cronologico.iconbitmap('BUHO_EPN_big.ico') #ingreso del icono en la ventana
    #-----------------------Imagen de fonde pantalla------------------------
    
    #V_cronologico.config(menu=mi_menu_master)
    #-----------------------------crear botones-----------------------------
    fondo_eolico_cron = ImageTk.PhotoImage(Image.open ('energía-Eolica-1.jpg'))  # Abre la imagen de fondo de pantalla, es igual al metodo anterior  fondo_eolico_cron = ImageTk.PhotoImage(Image.open ('energía-Eolica-1.jpg').resize((600, 300)))  cuando necesito definir el tamaño de la imagen
    fondo_cron1 = Label(V_cronologico, image=fondo_eolico_cron)
    fondo_cron1.image = fondo_eolico_cron                        # ojo realizar la igualacion para la visualizacion del fondo en ventana secundaria
    
    canvas1 =Canvas(V_cronologico, width = 400, height = 400)
    canvas1.pack(fill= 'both', expand = True)
    canvas1.create_image(0,0, image=fondo_eolico_cron, anchor= 'nw')    # posicion de la imagen de fondo
    canvas1.create_text(200, 50, text= 'prueba de titulo')              # posicion del texto interno
    
    #---------------------------------botones-------------------------------
    b_1 = Button(master = V_cronologico, text= 'Curva Potencia Aerogenerador')   # crea el texto sobre el boton, el command si llama la grafica         # b_1 = Button(master = V_cronologico, text= 'Curva Potencia Aerogenerador',  command = lambda: Curva_Aerogenerador())   # crea el texto sobre el boton, el command si llama la grafica
    
    #b_1.pack()
    b_2 = Button(V_cronologico, text= 'Promedio mensual')               # crea el texto sobre el boton
    b_3 = Button(V_cronologico, text= 'Promedio diario')                # crea el texto sobre el boton
    
    b1_canvas = canvas1.create_window(100, 60, anchor= 'nw', window= b_1)
    b2_canvas = canvas1.create_window(100, 120, anchor= 'nw', window= b_2)
    b3_canvas = canvas1.create_window(100, 180, anchor= 'nw', window= b_3)
    
    #return b1_canvas, b2_canvas, b3_canvas   #uso para evitar los warning
    
    
    #-----------Aplico en metodo de frame en ventana actual-----------------
    #Frame1_cronologico = Frame(V_cronologico, bg='blue')  # creo en frame interno para llevar la grafic a Tk
    #Frame1_cronologico.pack(expand=True, fill='both')     # defino que el frame se expanda a ambos lados si se estira la ventana
    #Frame1_cronologico.config(width='700', height='400')  # defino el tamaño del frame
    
    

def f_estadistico():
    #ventana.withdraw()                           #cierra la ventana principal
    V_estadistico=tk.Toplevel()                  #Abre la ventana secundaria
    V_estadistico.title('MÉTODO ESTADÍSTICO')    #titulo de la ventana
    V_estadistico.geometry('600x300')            #tamaño de la ventana 600x300
    V_estadistico.iconbitmap('BUHO_EPN_big.ico') #ingreso del icono en la ventana

#-------------------funciones para CURVAS DE AEROGENERADORES-----------------
def curva_Goldwind (filename):
    Goldwind = pd.read_excel('GoldWind GW70-1500.xlsx', sheet_name='Hoja1')
    vel_goldwind = Goldwind['Velocidad(m/s)'].values            # adquiere los valores de la velocidad de la hoja excel, en tipo Array
    pot_goldwind = Goldwind['Potencia(kW)'].values              # adquiere los valores de la potencia de la hoja excel, en tipo Array
    t, c, k = splrep(vel_goldwind, pot_goldwind, s=0, k=3)      # k=3 usa spline de ecuacion cubica
    spline = BSpline(t, c, k)
    
    gold_sin_ceros = Goldwind['Potencia(kW)'] != 0              # filtro los valores diferentes de cero para escojer los valores de arranque (min) y de parada (max) 
    gold_filt = Goldwind [gold_sin_ceros]                       # defino los valores diferentes de cero en las fechas correspondientes
    
    veleloc_filt = gold_filt['Velocidad(m/s)'].values           # adquiere los valores de la velocidad filtrada, en tipo Array
    vel_arranque = veleloc_filt.min()                           # adquiere el valor de arranque de la turbina (min)
    vel_parada = veleloc_filt.max()                             # adquiere el valor de parada de la turbina (max)
    
    
    return spline, gold_filt, vel_arranque, vel_parada

filename= 'GoldWind GW70-1500.xlsx'               # Nombre del archivo a ser leido
spline, gold_filt, vel_arranque, vel_parada = curva_Goldwind(filename)                 # Valores que retorna la funcion



def Curva_Aerogenerador ():
    x=np.linspace(0,30,1000)                                          # se define los limitesde velocidad para la grafica de, 1000 valores desde (0 m/s) hasta (30 m/s) 
    plt.figure()                                  
    plt.plot(x, spline(x), label='Curva Aerogenerador')               # grafica los alores de (y) y de (x)
    plt.title('(Potencia - Velocidad) del Aerogenerador', fontsize=16)
    plt.ylabel('Potencia [W] ', fontsize=15)
    plt.xlabel('Velocidad [m/s] ', fontsize=15)
    plt.show()
    #-------------para llamar la grafica a la ventana ------------------
    '''
    canvas = FigureCanvasTkAgg(Fig, master = V_cronologico)   
    canvas.draw() 
    canvas.get_tk_widget().pack() 
  
    toolbar = NavigationToolbar2Tk(canvas, V_cronologico) 
    toolbar.update() 
  
    canvas.get_tk_widget().pack() 
    '''
    
Curva_Aerogenerador()


#-----------------lectura de base de datos en hoja excel .csv----------------
def lectura_datos (archivo_csv):
    Hexc=pd.read_csv(archivo_csv , delimiter=',')       # usa el separador del archivo csv, para ordenar el DataFrame
    Hexc=Hexc.filter(items=['Source','Location ID','City','State','Country','Latitude',
                            'Longitude','Time Zone','Local Time Zone',
                            'Clearsky DHI Units'])      # filtra solo las columnas que se desea usar
    #Hexc=Hexc.drop(['DNI Units','GHI Units'],axis=1)   # elimina las columnas que no se quiere usar
    Longitudes=Hexc.iloc[0:1,5:8]                       # iloc filtras las filas y columnas deseadas de la base de datos
    col_L=['Latitude']                                  # se enlista el nombre de la nueva columna
    Longitudes[col_L]=Longitudes[col_L].apply(pd.to_numeric, errors='coerce', axis=1) #se transforma a formato numerico las columnas que se introducen anteriormente
    L=Longitudes['Latitude'].values[0]                  # Adquiere el valor float de la latitud
    #-------------Definición de nuevo encabezado-------------------
    base_datos=Hexc.iloc[1: , : ]                       # iloc filtras las filas y columnas deseadas de la base de datos
    nuevo_header = base_datos.iloc[0]                   # toma la primera fila para el encabezado
    base_datos = base_datos[1:]                         # toma los datos menos la fila del encabezado
    base_datos.columns = nuevo_header                   # establece la fila del encabezado como el encabezado del dataFrame
    base_datos=base_datos.reset_index()                 # resetea el indice del DataFrame
    base_datos.drop(['index'],axis=1,inplace=True)      # elimina el anterior indice y lo guarda en el mismo DataFrame
    #--------------Creacion de fecha con datetime------------------
    base_datos['Fecha']=pd.to_datetime(dict(year=base_datos['Year'],month=base_datos['Month'],day=base_datos['Day'], hour=base_datos['Hour'], minute=base_datos['Minute']))
                                                        # Se ha creado una nueva columna tipo datetime de nombre 'Fecha',extrayendo la informacion de las columnas de la base de datos tanto de los meses, dias, año, horas y minutos
    base_datos=base_datos.set_index('Fecha')            # Se fija la fecha como indice (index)
    bdd=base_datos.drop(['Year','Month','Day','Hour','Minute'],axis=1)  # elimina las columnas no deseadas de la nueva base de datos
    bdd_float=bdd.replace('[^\d.]', '', regex= True).astype(float)      # se convierte los valores del DataFrame de tipo object a type float, para realizar los promedios
    
    return Hexc, Longitudes, bdd_float, L                   # Valores que retorna la funcion

archivo_csv='NREL Villonaco 2019.csv'                         # nombre del archivo a ser leido
Hexc, Longitudes, bdd_float, L = lectura_datos(archivo_csv) # Valores que retorna la funcion

#-----------------seno, coseno y tangente de L (latitud)---------------------
cos_L=math.cos(L* math.pi/180)                           # se aplica la formula para calcular coseno de latitud
sin_L=math.sin(L* math.pi/180)                           # se aplica la formula para calcular seno de latitud
tan_L=math.tan(L* math.pi/180)                           # se aplica la formula para calcular tangente de latitud
#----------------declaro el angulo de inclinacion del panel------------------
E=25                                                     # Tanto para Masters como para Tiwari
cos_E=math.cos(E* math.pi/180)                           # se aplica la formula para calcular coseno de inclinacion de panel
sin_E=math.sin(E* math.pi/180) 
L_E=L-E  
tan_LE= math.tan(L_E*math.pi/180)                        # se aplica la formula para calcular tangente de resta de angulos de panel  
cos_LE= math.cos(L_E*math.pi/180)                        # se aplica la formula para calcular coseno de resta de angulos de panel 
sin_LE= math.sin(L_E*math.pi/180)                        # se aplica la formula para calcular seno de resta de angulos de panel 
#----------------factores de conversion de plano inclinado-------------------
Rd = (1+cos_E)/2                                         # Factor de conversion de radiacion difusa Rd
Rr = (1-cos_E)/2                                         # Factor de conversion de radiacion reflejada Rr
Ro = 0.2                                                 # Coeficiente de reflexion para suelo ordinario  
#--------------------DEFINICION DE ORIENTACION DEL PANEL---------------------
if L > 0:                                                # Condicion para escoger el ángulo acimut de orientacion del panel (PARA TIWARI)
    GAMA =  0                                            # si el panel esta en el hemisferio norte
else:
    GAMA = 180                                           # si el panel esta en el hemisferio sur
GAMA_rad= math.radians(GAMA)                             # transformacion de grados a radianes
cos_GAMA=math.cos(GAMA_rad)                              # coseno de angulo acimutal GAMA
sin_GAMA=math.sin(GAMA_rad)                              # seno de angulo acimutal GAMA

#_____________________________MÉTODO DE MASTERS______________________________
#---------------------funciones para estructuras de fechas-------------------   
def fechas_horas (bdd_float):
    #-------------------Adquiere las fechas del DataTime---------------------
    fechas=bdd_float.index                               # adquiere todas las dechas del DataFrame bdd_float
    f_inicio=fechas[0]                                   # adquiere la fecha en la que inicio la toma de datos variable type TimeStamp
    fecha_ini=str(f_inicio)                              # fecha inicial se pasa a tipo str
    #f_fin=fechas[-1]                                    # adquiere la fecha en la que finalizo la toma de datos variable type TimeStamp
    #----se extrae el numero de dia "n" para las formulas de declinacion----
    f=fechas.to_frame()                                  # Se crea una variable que contenga las fechas de la base de datos pero en formato DataFrame  
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

n, fechas, fecha_ini, f = fechas_horas(bdd_float)        # Valores que retorna la funcion

#---------------------DECLINACION Y ANGULO DE ALTITUD----------------------

def angulos (n):
    
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
    H_amanecer=lambda tan_d : math.acos(-tan_L*tan_d* math.pi/180)      # se aplica la formula para calcular angulo H_SR°
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
    ang_concat['seno (β°)'] = ang_concat['coseno (δ°)']*ang_concat['coseno (H°)']*cos_L + sin_L*ang_concat['seno (δ°)'] # se calcula el seno(β°)
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
    ang_concat['Io (kWh/m^2)'] = (24/math.pi)*SC*(1+0.034*ang_concat['Aux_ndia'] )*(cos_L*ang_concat['coseno (δ°)']*ang_concat['seno (H_SR)']+ ang_concat['H_SR (Radianes)']* sin_L*ang_concat['seno (δ°)'] )   # se calcula el Io(kW/m^2)
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
    ang_concat['tg(δ)/tg(L)'] = ang_concat['tan (δ°)']/tan_L            # se calcula el relacion tg(δ)/tg(L)
    #------------------------filtrar columnas (Φs)------------------------- 
    ang_concat['Φs'] = np.where(ang_concat['coseno (H°)']>= ang_concat['tg(δ)/tg(L)'], ang_concat['(Φs1)'], ang_concat['(Φs2)'] )  # creacion de una columna 'Φs' para rellenar con nuevos valores bajo las condiciones de la ambiguedaddel seno
    #--------H_SRC ángulo horario; salida del sol (PARA EL COLECTOR)------- 
    H_amanecer_c=lambda tan_d : math.acos(-tan_LE*tan_d* math.pi/180)    # se aplica la formula para calcular angulo H_SRC°
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
    ang_concat['Rb'] = (cos_LE*ang_concat['coseno (δ°)']*ang_concat['seno (H_SRC)'] + ang_concat['H_SRC min']*sin_LE*ang_concat['seno (δ°)'])/(cos_L*ang_concat['coseno (δ°)']*ang_concat['seno (H_SR)'] + ang_concat['H_SR (Radianes)']*sin_L*ang_concat['seno (δ°)']) # Factor de conversion de radiacion de haz Rb
    
    return ang, ang_concat, cos_d, sin_d, cos_H, sin_H, co_H, bet, aci, BETA, sin_Hsr, num_dia, sin_Hsrc      # Valores que retorna la funcion
ang, ang_concat, cos_d, sin_d, cos_H, sin_H, co_H, bet, aci, BETA, sin_Hsr, num_dia, sin_Hsrc = angulos(n)    # Valores que retorna la funcion


#---------------INTERPOLACION Y FILTRADO de BASE DE DATOS------------------
                                                            # SE rellena los datos faltante Nan con el methodo de interpolacion (akima)
def interpolacion_bdd ():
    bdd_float[bdd_float < 0] = 0                            # se elimina los valores negativos de la primera base de datos 
    sin_nan=bdd_float.interpolate(method='akima', order=3)  # otros metodos spline, polynomial, linear, ojo revisar: CubicSpline
    bdd_inter=sin_nan.fillna(method='ffill')                # completa los valores en la ultima posicion de las columnas debido a que el metodo solo realiza interpolacion, no resuelve extrapolación
    bdd_inter=bdd_inter.fillna(method='bfill')              # completa los valores en la posicion inicial de las columnas debido a que el metodo solo realiza interpolacion, no resuelve extrapolación
    bdd_inter[bdd_inter < 0] = 0                            # se elimina valores negativos nuevamente debido a que los metodos de interpolacion pueden entregar valores negativos en el proceso
    
    return bdd_inter                                        # Valores que retorna la funcion

bdd_inter = interpolacion_bdd()                             # Valores que retorna la funcion
#--------------------FUNCIONES INDEPENDIENTES BDD --------------------------

def BDD_independientes ():
    BDD_irad = bdd_float.filter(items=['GHI'])               # se filtran las columnas individuales de la bdd_float
    BDD_vel_v = bdd_float.filter(items=['Wind Speed'])       # se filtran las columnas individuales de la bdd_float
    BDD_direc_v = bdd_float.filter(items=['Wind Direction']) # se filtran las columnas individuales de la bdd_float
    BDD_temp = bdd_float.filter(items=['Temperature'])       # se filtran las columnas individuales de la bdd_float
   
    return BDD_irad, BDD_vel_v, BDD_direc_v, BDD_temp               # Valores que retorna la funcion

BDD_irad, BDD_vel_v, BDD_direc_v, BDD_temp = BDD_independientes ()  # Valores que retorna la funcion

#----------------FUNCIONES INDEPENDIENTES BDD INTERPOLADA-------------------

def INTER_independientes ():
    INTER_irrad = bdd_inter.filter(items=['GHI'])                   # se filtran las columnas individuales de la bdd_inter
    INTER_vel = bdd_inter.filter(items=['Wind Speed'])              # se filtran las columnas individuales de la bdd_inter
    INTER_direc = bdd_inter.filter(items=['Wind Direction'])        # se filtran las columnas individuales de la bdd_inter
    INTER_temp = bdd_inter.filter(items=['Temperature'])            # se filtran las columnas individuales de la bdd_inter
    
    return INTER_irrad, INTER_vel, INTER_direc, INTER_temp                # Valores que retorna la funcion

INTER_irrad, INTER_vel, INTER_direc, INTER_temp = INTER_independientes ()  # Valores que retorna la funcion



#---------------EJEMPLO DE GRAFICA DE DATOS DIARIOS-------------------------
# no_spline=BDD_irad.plot().set_title('BDD irrad, no aumenta periodos')


def distribucion_temporal_solar():
    
    plt.figure()
    BDD_irad.plot(linewidth=0.7)
    plt.title('Distribución Temporal "IRRADIANCIA"', fontsize=15)
    plt.ylabel('Irradiancia [W/m^2]', fontsize=16)
    plt.show()
      
distribucion_temporal_solar()


def distribucion_temporal_temp():
    
    plt.figure()
    BDD_temp.plot(linewidth=0.7)
    plt.title('Distribución Temporal "Temperatura"', fontsize=15)
    plt.ylabel('Temperatura [°C]', fontsize=16)
    plt.show()
      
distribucion_temporal_temp()

def distribucion_temporal_V_viento():
    
    plt.figure()
    BDD_vel_v.plot(linewidth=0.7)
    plt.title('Distribución Temporal "Velocidad del Viento"', fontsize=15)
    plt.ylabel('Velocidad del Viento [m/s]', fontsize=16)
    plt.show()
      
distribucion_temporal_V_viento()

def distribucion_temporal_D_viento():
    
    plt.figure()
    BDD_direc_v.plot(linewidth=0.7)
    plt.title('Distribución Temporal "Dirección del Viento"', fontsize=15)
    plt.ylabel('Dirección del Viento [°]', fontsize=16)
    plt.show()
      
distribucion_temporal_D_viento()


#-------------------SPLINE DE BDD Y BDD INTERPOLADA-------------------------
def spl_de_INTER (INTER_irrad, INTER_vel, INTER_temp):
    #--------------------------SPLINE DE BDD -------------------------------
    
    med_irrad_INTER = INTER_irrad.shape[0]                                 # cuenta los valores del dataframe (tipo int)
    hora = np.linspace(0, med_irrad_INTER, med_irrad_INTER)                # med_irrad_INTER guarda el numero de mediciones de la variable irradiancia.
    [t, c, k] = splrep(hora, INTER_irrad, s=0, k=3)                        # s: determina una condicion de suavisado (cercania y control del ajuste), s=0 si no se determinan los pesos (w) en la interpolacion______k: grado de ajuste del spline. Se recomienda splines cúbicos. Deben evitarse los valores pares de k, especialmente con valores pequeños de s. 1 <= k <= 5
    hora1 = np.linspace(0, med_irrad_INTER, med_irrad_INTER*2)             # valores del eje x para el grafico. (med_irrad_INTER*2) Se multiplica por 2 para obtener el doble de valores diarios.
    interp = splev(hora1, [t, c, k])                                       # spl recibe como argumentos(x, [t, c, k]).
    dates = pd.date_range(start=fecha_ini , periods=med_irrad_INTER*2, freq='15T') # med_irrad_INTER*2 ; 4: datos por hora (se duplican la cantidad de datos); Al ser 4 datos por hora la frecuencia es cada 15 min ('15T'), ya que (4*15=60).
    INTER_spl_irrad = pd.DataFrame(data=interp,index=dates)
    INTER_spl_irrad[INTER_spl_irrad < 0.1]=0
    INTER_spl_irrad.columns = ['GHI']                                      # cambio el nombre de la columna
    INTER_spl_irrad.index.names = ['Fecha']
    

    INTER_spl_irrad.plot(linewidth=0.8).set_title('spline INTER irrad, aumenta periodos')
    
    med_vel_INTER = INTER_vel.shape[0]                                     # cuenta los valores del dataframe (tipo int)
    hora = np.linspace(0, med_vel_INTER, med_vel_INTER)                    # med_vel_INTER guarda el numero de mediciones de la variable irradiancia.
    [t, c, k] = splrep(hora, INTER_vel, s=0, k=3)                          # s: determina una condicion de suavisado (cercania y control del ajuste), s=0 si no se determinan los pesos (w) en la interpolacion______k: grado de ajuste del spline. Se recomienda splines cúbicos. Deben evitarse los valores pares de k, especialmente con valores pequeños de s. 1 <= k <= 5
    hora1 = np.linspace(0, med_vel_INTER, med_vel_INTER*2)                 # valores del eje x para el grafico. (med_vel_INTER*2) Se multiplica por 2 para obtener el doble de valores diarios.
    interp = splev(hora1, [t, c, k])                                       # spl recibe como argumentos(x, [t, c, k]).
    dates = pd.date_range(start=fecha_ini , periods=med_vel_INTER*2, freq='15T') # med_vel_INTER*2 ; 4: datos por hora (se duplican la cantidad de datos); Al ser 4 datos por hora la frecuencia es cada 15 min ('15T'), ya que (4*15=60).
    INTER_spl_vel = pd.DataFrame(data=interp,index=dates)
    INTER_spl_vel[INTER_spl_vel < 0]=0
    INTER_spl_vel.columns = ['Wind Speed']                                 # cambio el nombre de la columna
    INTER_spl_vel.index.names = ['Fecha']

    INTER_spl_vel.plot(linewidth=0.8).set_title('spline BDD vel. viento, aumenta periodos')
    
    
    med_temp_INTER = INTER_temp.shape[0]                                   # cuenta los valores del dataframe (tipo int)
    hora = np.linspace(0, med_temp_INTER, med_temp_INTER)                  # med_temp_INTER guarda el numero de mediciones de la variable irradiancia.
    [t, c, k] = splrep(hora, INTER_temp, s=0, k=3)                         # s: determina una condicion de suavisado (cercania y control del ajuste), s=0 si no se determinan los pesos (w) en la interpolacion______k: grado de ajuste del spline. Se recomienda splines cúbicos. Deben evitarse los valores pares de k, especialmente con valores pequeños de s. 1 <= k <= 5
    hora1 = np.linspace(0, med_temp_INTER, med_temp_INTER*2)               # valores del eje x para el grafico. (med_temp_INTER*2) Se multiplica por 2 para obtener el doble de valores diarios.
    interp = splev(hora1, [t, c, k])                                       # spl recibe como argumentos(x, [t, c, k]).
    dates = pd.date_range(start=fecha_ini , periods=med_temp_INTER*2, freq='15T') # med_temp_INTER*2 ; 4: datos por hora (se duplican la cantidad de datos); Al ser 4 datos por hora la frecuencia es cada 15 min ('15T'), ya que (4*15=60).
    INTER_spl_temp = pd.DataFrame(data=interp,index=dates)
    INTER_spl_temp[INTER_spl_temp < 0]=0
    INTER_spl_temp.columns = ['Temperatura']
    INTER_spl_temp.index.names = ['Fecha']

    INTER_spl_temp.plot().set_title('spline INTER temperatura, aumenta periodos')
    

    
    
    return INTER_spl_irrad, INTER_spl_vel, INTER_spl_temp                                     # Valores que retorna la funcion

INTER_spl_irrad, INTER_spl_vel, INTER_spl_temp  = spl_de_INTER (INTER_irrad, INTER_vel, INTER_temp)  # Valores que retorna la funcion

#----------------POTENCIA generada por el panel solar--------------------

def Potencia(Tamb , Ex): # Tamb:[C] ; Ex:[W/m2]

    
    TONC = 47.5 # C        ## da el fabricante
    T_cell = Tamb +(TONC-20)*(Ex/800)
    g = -0.463 # %/C       ## da el fabricante
    Pmax_STC = 250 # Wp    ## da el fabricante
    Pmax_T_cell_bdd = Pmax_STC*(1+(g/100)*(T_cell-25))*(Ex/1000)
    
    
    return Pmax_T_cell_bdd                          # Valores que retorna la funcion


#---------------------POTENCIA PARA BDD------------------------------
potenc_bdd = BDD_temp.Temperature.astype(object).combine(BDD_irad.GHI , func = Potencia)
potenc_bdd = potenc_bdd.to_frame()
potenc_bdd.columns = ['Energia [Wh]']                                 # cambio el nombre de la columna
ener_panel_bdd = potenc_bdd.resample('D').apply(integrate.trapz, dx=1/2)  #realiza la integracion diaria de la energia  ;  dx=1/2 porque la integracion por defecto es de 1 unidad (hora), como tenemos una frecuencia de 30T, se debe especificar que la hora la dividimos en 2 partes de 30 minutos
suma_BDD = ener_panel_bdd.sum()


#---------------------POTENCIA PARA SPLINE------------------------------

potenc_INTER_SPLINE = INTER_spl_temp .Temperatura.astype(object).combine(INTER_spl_irrad.GHI , func=Potencia)
potenc_INTER_SPLINE = potenc_INTER_SPLINE.to_frame()
potenc_INTER_SPLINE.columns = ['Energia [Wh]']                                 # cambio el nombre de la columna
ener_panel_spl = potenc_INTER_SPLINE.resample('D').apply(integrate.trapz, dx=1/4) #realiza la integracion diaria de la energia;   dx=1/4 porque la integracion por defecto es de 1 unidad (hora), como tenemos una frecuencia de 15T, se debe especificar que la hora la dividimos en 4 partes de 15 minutos
suma_spline = ener_panel_spl.sum() 

prom_mes_pot = ener_panel_spl.resample('M').mean()

fig, ax = plt.subplots()
prom_mes_pot.plot(kind='bar', figsize=(12,8), color='r',edgecolor='black',  width=0.7, alpha=0.8, stacked= True, ax=ax)    #  width=0.7 es el ancho, alpha=0.8 es la opacidad, color='g' es el color de la grafica, edgecolor='black' es el color del contorno de las barras, puedo retirar los 4 argumentos
ax.set_xticklabels([x.strftime('%Y-%m') for x in prom_mes_pot.index], rotation=90)
plt.ylabel('Energía generada [Wh/m^2-dia]', fontsize=16)
plt.xlabel('Fechas [meses]', fontsize=16)
plt.title('METODO MASTERS: Energía SOLAR Generada promedio mensual')
plt.show()


#----------------------- Grafica hecha funcion-------------------------
def graficas_energia_solar():
    
    fig, ax = plt.subplots()
    prom_mes_pot.plot(kind='bar', figsize=(12,8), color='r',edgecolor='black',  width=0.7, alpha=0.8, stacked= True, ax=ax)    #  width=0.7 es el ancho, alpha=0.8 es la opacidad, color='g' es el color de la grafica, edgecolor='black' es el color del contorno de las barras, puedo retirar los 4 argumentos
    ax.set_xticklabels([x.strftime('%Y-%m') for x in prom_mes_pot.index], rotation=90)
    plt.ylabel('Energía generada [Wh/m^2-dia]', fontsize=16)
    plt.xlabel('Fechas [meses]', fontsize=16)
    plt.title('MASTERS: Energía SOLAR Generada promedio mensual')
    plt.show()
    
    
graficas_energia_solar()


#----------------------------ERROR RELATIVO---------------------------

error_solar = abs(((suma_BDD-suma_spline)/suma_BDD)*100)

#-------------------Muestra la radiacion diaria-----------------------
# -----esta funcion funciona pero no es equivalente a su reemplazo-----
'''
def periodo_valido (BDD_irad):
    
    #periodo_radiacion_filt=FILT_irrad.between_time('06:30','18:30') #Establezco el horario en que existen medidas de radiacion solar para sacar promedios diarios
    periodo_radiacion_BDD = BDD_irad['GHI'] != 0           # selecciono los valores diferentes de cero para realizar el promedio diario de irradiacion solar sin importar la zona horaria devuelve valores bool (true, false)
    periodo_rad_BDD = BDD_irad [periodo_radiacion_BDD]           # defino los valores diferentes de cero en las fechas correspondientes
    
    return periodo_rad_BDD

periodo_rad_BDD = periodo_valido (BDD_irad)
'''
#-------------------kT, IDH, por metodo de MASTERS-----------------------
#-------------promedio de GHI para sacar kT (indice de claridad)---------
def kt_bdd_masters ():
    
    GHI_diario =BDD_irad.resample('D').apply(integrate.trapz, dx=1/2)  # Area bajo la curva de irradiacion, energia diaria de la irradiacion global ;   dx=1/2 porque la integracion por defecto es de 1 unidad (hora), como tenemos una frecuencia de 30T, se debe especificar que la hora la dividimos en 2 partes de 30 minutos
    GHI_diario['GHI'] = GHI_diario['GHI']/1000                         # paso a kWh/m^2-dia   
    GHI_diario.columns=['GHI kWh/m^2-dia']                             # se cambia el nombre de la columna
    
    Io_irad = ang_concat.filter(items=['Io (kWh/m^2)'])                # se filtra item Io, para promediar diariamente
    Io_irad=Io_irad.resample('D').mean()                               # se promedia diariamente Io
    #------------------- METODO DE MASTERS, calculo de (kT)---------------
    kT_diario=pd.concat([GHI_diario, Io_irad], axis=1)                       # se concatena la nueva columna calculada al dataframe anterior
    kT_diario['kT'] = kT_diario['GHI kWh/m^2-dia']/kT_diario['Io (kWh/m^2)'] # se calcula el kT(indice de claridad diario)
    kT_diario['I_DH kWh/m^2-dia'] = kT_diario['GHI kWh/m^2-dia']*(1.390-4.027*kT_diario['kT']+5.531*kT_diario['kT']**2-3.108*kT_diario['kT']**3)  # calculo de irradiancia difusa horizontal DIARIA
    kT_diario['IBH'] = kT_diario['GHI kWh/m^2-dia'] - kT_diario['I_DH kWh/m^2-dia']                              # se encuentra la irradiancia de haz directo en una superficie horizontal
    #------------------- METODO DE MASTERS, filtro de (Rb)----------------
    Rb_m = ang_concat.filter(items=['Rb'])                             # se filtra item Rb, para promediar diariamente
    Rb_m = Rb_m.resample('D').mean()                                   # se promedia diariamente Rb
    kT_diario=pd.concat([kT_diario, Rb_m], axis=1)                     # se concatena todos los valores calculados
    #-----RADIACION SOLAR TOTAL "DIARIA" EN UNA SUPEFICIE INCLINADA-------
    kT_diario['IC'] = kT_diario['IBH']*kT_diario['Rb']+kT_diario['I_DH kWh/m^2-dia']*Rd+ Ro*kT_diario['GHI kWh/m^2-dia']*Rr

    #------------------- promedio mensual de  GHI e Io--------------------
    kT_mensual=pd.concat([GHI_diario, Io_irad], axis=1)
    kT_mensual=kT_mensual.resample('M').mean()
    kT_mensual['kT'] = kT_mensual['GHI kWh/m^2-dia']/kT_mensual['Io (kWh/m^2)'] # se calcula el kT(indice de claridad mensual)
    kT_mensual['I_DH kWh/m^2-dia'] = kT_mensual['GHI kWh/m^2-dia']*(1.390-4.027*kT_mensual['kT']+5.531*kT_mensual['kT']**2-3.108*kT_mensual['kT']**3)  # calculo de irradiancia difusa horizontal MENSUAL
    kT_mensual['IBH']=kT_mensual['GHI kWh/m^2-dia'] - kT_mensual['I_DH kWh/m^2-dia'] 
    Rb_m_mensual = Rb_m.resample('M').mean() 
    kT_mensual = pd.concat([kT_mensual, Rb_m_mensual], axis=1)                     # se concatena todos los valores calculados
    #--RADIACION SOLAR TOTAL "DIARIA mensual" EN UNA SUPEFICIE INCLINADA--
    kT_mensual['IC'] = kT_mensual['IBH']*kT_mensual['Rb']+kT_mensual['I_DH kWh/m^2-dia']*Rd+ Ro*kT_mensual['GHI kWh/m^2-dia']*Rr
    
    
    return GHI_diario, kT_diario, kT_mensual, Rb_m

GHI_diario, kT_diario, kT_mensual, Rb_m  = kt_bdd_masters ()





   

#-----------------------PARA LA BDD SPLINE-------------------------------


'''
colum_encabezados=['GHI', 'Temperature']
periodo_radiacion_filt=bdd_inter [colum_encabezados] != 0            #selecciono los valores diferentes de cero para realizar el promedio diario de irradiacion solar sin importar la zona horaria
p_rad_filt=bdd_inter  [periodo_radiacion_filt]           #defino los valores diferentes de cero en las fechas correspondientes
#prom_diario_filt=p_rad_filt.resample('d').mean()         #promedio diario de radiacion solar filtrada
'''   
#-----------------------PARA LA BDD EOLICA-------------------------------

def poten_eolica_bdd (BDD_vel_v):
    
    pot_eo = spline(BDD_vel_v)                                          # saca los valores de potencia de las velocidaddes de viento
    forma = pot_eo.shape[0]                                             # saca el numero de datos 
    datos = pd.date_range(start=fecha_ini , periods=forma, freq='30T')  # saca las fechas y horas a una frecuencia de 30 minutos
    p_eolica = pd.DataFrame(data=pot_eo, index=datos)                   # es el mismo df de (pot_eo), pero con los datos de intervalos(fechas)
    
    
    return  p_eolica

p_eolica = poten_eolica_bdd(BDD_vel_v)
p_eolica.columns=['P eólica (W)']  
p_eolica[p_eolica < 0.01] = 0
area_eol_bdd=p_eolica.resample('D').apply(integrate.trapz, dx=1/2)   # Area bajo la curva de velocidad del viento, (energia diaria) ;   dx=1/2 porque la integracion por defecto es de 1 unidad (hora), como tenemos una frecuencia de 30T, se debe especificar que la hora la dividimos en 2 partes de 30 minutos
area_eol_bdd.columns=['E_eólica_Wh'] 

area_eol_bdd_mes = area_eol_bdd.resample('M').mean()

area_eol_bdd_año = area_eol_bdd.resample('Y').mean()


''' 
fechas_solar=area_eol_bdd.index                             # saca las fechas del indice
f_eolic=fechas_solar.to_frame()                             # pasa a formato Frame las fechas del indice
f_eolic.columns=['Fecha']                                   # se cambia el nombre de la columna

pot_eolic=pd.concat([f_eolic, area_eol_bdd], axis=1)        # concatena las fecjas del indice con la potencia generada por el aerogenerador
'''
#index_fecha = pd.date_range(start=fecha_ini , periods=12)   # define los meses del año del indice 
fig, ax = plt.subplots()
area_eol_bdd_mes.plot(kind='bar', figsize=(12,8), color='r',edgecolor='black',  width=0.7, alpha=0.8, stacked= True, ax=ax)    #  width=0.7 es el ancho, alpha=0.8 es la opacidad, color='g' es el color de la grafica, edgecolor='black' es el color del contorno de las barras, puedo retirar los 4 argumentos
ax.set_xticklabels([x.strftime('%Y-%m') for x in area_eol_bdd_mes.index], rotation=90)
plt.ylabel('Energía generada [Wh]', fontsize=16)
plt.xlabel('Fechas [meses]', fontsize=16)
plt.title('METODO: CRONOLÓGICO: Energía Eólica promedio mensual')
plt.show()



#area_eol_bdd_mes['E_eólica_Wh'].plot.bar().set_title('Grafica mensual  de E_eólica_Wh')

#area_eol_bdd.plot.bar().set_title('Grafica diaria  de E_eólica_Wh')    # Tambien grafica barras

     

#---------------------Promedio de "DataFrame COMPLETO"-----------------------
BDD_prom_diario=bdd_float.resample('d').mean()             #se saca promedio por dia de todo el DataFrame
BDD_prom_mensual=bdd_float.resample('M').mean()            #se saca promedio por mes de todo el DataFrame
BDD_prom_anual=bdd_float.resample('Y').mean()              #se saca promedio por año de todo el DataFrame


#------------------Promedio de "DataFrame por variables"---------------------

prom_dia_DNI=BDD_prom_diario.filter(items=['GHI'])         #Escoje solamente la columna deseada, si quiero mas elementos uso (items=['DNI', 'Temperature', 'Presure', 'etc'])
prom_mes_DNI=BDD_prom_mensual.filter(items=['GHI'])

#------------------------------DataFrame SOLAR-------------------------------

df_solar=bdd_float.filter(items=['GHI','Temperature'])

#-------------------------------GRAFICA SOLAR--------------------------------

# DNI (direct Normal Irradiance), DHI (diffuse horizontal irradiance)
# GHI (Global Horizantal Irradiance)   TRABAJAR CON ESTA VARIABLE 'GHI' = es la SUMA DE LAS 3 RADIACIONES DIRECTA+ DIFUSA+ REFLEJADA 

RADIACIONES = kT_diario.filter(items=['GHI kWh/m^2-dia', 'I_DH kWh/m^2-dia']) 


RADIACIONES=RADIACIONES.T                                  #Se transpone el DataFrame para poder ingresar a la agrupacion de datos por mes
solar_grupo_mes=RADIACIONES.groupby(pd.PeriodIndex(RADIACIONES.columns, freq='M'), axis=1).mean()   #se agrupa por mes mediante groupby la parte de..!  .sum() suma los valores de todo el mes
df_grupo_mes=solar_grupo_mes.T                    # se vuelve a transponer para dar una mejor presentacion de los datos


df_grupo_mes.plot.bar().set_title('RADIACION promedio mensual diario')
plt.ylabel('Energía [kWh/m^2-dia]', fontsize=15)
df_grupo_mes.plot().set_title('RADIACION promedio mensual diario')



df_solar.plot().set_title('Grafica de todos los valores de df_solar GHI')
prom_dia_DNI.plot().set_title('Grafica de promedio diario GHI')

prom_mes_DNI.index = prom_mes_DNI.index.strftime('%Y-%m')
prom_mes_DNI.plot.bar(color='g',edgecolor='black',  width=0.7, alpha=0.8).set_title('MÉTODO MASTERS: Gráfica promedio mensual GHI')
plt.ylabel('[kWh]', fontsize=16)
#plt.title('Ganancias en el 2020')
#plt.xlabel('Mes del 2020')
#plt.ylabel('Ganancias (en miles de pesos)')


BDD_prom_mensual.plot().set_title('Promedio mensual de todas las variables')

# ejemplo de plot:    opsd_dia['Consumption'].plot(linewidth=0.1)

#--------------------------GRAFICA SOLAR con Spline--------------------------

area_eol_bdd_mes.index = area_eol_bdd_mes.index.strftime('%Y-%m')
area_eol_bdd_mes.plot.bar().set_title('METODO CRONOLÓGICO: Grafica Prom.mensual Energía eólica [Wh]')
plt.ylabel('Energía [kWh/m^2-dia]', fontsize=15)

#------------------------------DataFrame EÓLICO------------------------------
#df_eolico=bdd_float.filter(items=['Wind Speed','Wind Direction','Pressure']) #se eliminan las columnas que no se utilizan para la evaluación eólica, y se adquiere un nuevo DataFrame


#______________________________MÉTODO TIWARI_________________________________


#---------------------DECLINACION Y ANGULO DE ALTITUD----------------------

def angulos_tiwari (n):
    
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
    H_amanecer = lambda tan_d : math.acos(-tan_L*tan_d* math.pi/180)    # se aplica la formula para calcular angulo Ws°
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
    ang_tiwari['coseno (θZ°)'] = ang_tiwari['coseno (δ°)']*ang_tiwari['coseno (ω°)']*cos_L + sin_L*ang_tiwari['seno (δ°)'] # se calcula el coseno(θZ°)
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
    ang_tiwari['Io (kWh/m^2)'] = (24/math.pi)*SC*(1+0.033*ang_tiwari['Aux_ndia'] )*(cos_L*ang_tiwari['coseno (δ°)']*ang_tiwari['seno (Ws)']+ ang_tiwari['Ws (Radianes)']* sin_L*ang_tiwari['seno (δ°)'] )   # se calcula el Io(kW/m^2)
    #------------------Ángulo de incidencia (Cos θi °)----------------------
    ang_tiwari['Coseno (θi)']=(cos_L*cos_E + sin_L*sin_E*cos_GAMA)*ang_tiwari['coseno (δ°)']*ang_tiwari['coseno (ω°)'] + ang_tiwari['coseno (δ°)']*ang_tiwari['seno (ω°)']*sin_E*sin_GAMA + ang_tiwari['seno (δ°)']*(sin_L*cos_E-cos_L*sin_E*cos_GAMA) # se calcula cos θi (angulo de incidencia)
    #---------FACTORES DE CONVERSION SOBRE UNA SUPERFICIE INCLINADA---------
    #ang_tiwari['Rb'] = ang_tiwari['Coseno (θi)']/ang_tiwari['coseno (θZ°)'] # Factor de conversion de radiacion de haz Rb
    #--------W_SRC ángulo horario; salida del sol (PARA EL COLECTOR)------- 
    W_amanecer_c=lambda tan_d : math.acos(-tan_LE*tan_d* math.pi/180)    # se aplica la formula para calcular angulo W_SRC°
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
    ang_tiwari['Rb'] = (cos_LE*ang_tiwari['coseno (δ°)']*ang_tiwari['seno (W_SRC)'] + ang_tiwari['W_SRC min']*sin_LE*ang_tiwari['seno (δ°)'])/(cos_L*ang_tiwari['coseno (δ°)']*ang_tiwari['seno (Ws)'] + ang_tiwari['Ws (Radianes)']*sin_L*ang_tiwari['seno (δ°)']) # Factor de conversion de radiacion de haz Rb
    
    
    
    
    
    return ang, ang_tiwari, cos_d, sin_d, cos_W, sin_W, co_w, tet, sin_Ws, num_dia, sin_Wsrc #, aci      # Valores que retorna la funcion
ang, ang_tiwari, cos_d, sin_d, cos_W, sin_W, co_w, tet, sin_Ws, num_dia, sin_Wsrc = angulos_tiwari(n) #, aci   # Valores que retorna la funcion

#-----------------------kT, IDH, por metodo de TIWARI-----------------------
#---------------promedio de GHI para sacar kT (indice de claridad)----------


def kt_bdd_tiwari (GHI_diario, num_dia, kT_mensual):
    
    Io_tiwari = ang_tiwari.filter(items=['Io (kWh/m^2)'])                          # filtro Io de ang_tiwari
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
    #-------------IRRADIACION de HAZ PARA DIFERENTES CONDICIONES-------------
    kT_diario_t['IB_Tiw']=kT_diario_t['GHI kWh/m^2-dia'] - kT_diario_t['ID_Tiw']                              # se encuentra la irradiancia de haz directo en una superficie horizontal
    #-------------ELIMINACION DE COLUMNAS DESPUES DE CONDICIONES-------------
    kT_diario_t=kT_diario_t.drop(['I_D1','I_D2','I_D3','I_D4','I1', 'I2', 'I3', 'I4'],axis=1)                 # elimina las columnas no deseadas de la nueva base de datos, (SE PUEDE COMENTAR ESTA LINEA no afecta)
    #------------------- METODO DE TIWARI, filtro de (Rb)----------------
    Rb_t = ang_tiwari.filter(items=['Rb'])                                   # se filtra item Rb, para promediar diariamente
    Rb_t = Rb_t.resample('D').mean()                                         # se promedia diariamente Rb
    kT_diario_t = pd.concat([kT_diario_t, Rb_t], axis=1)                     # se concatena todos los valores calculados
    '''
    #-----RADIACION SOLAR TOTAL "DIARIA" EN UNA SUPEFICIE INCLINADA-------
    kT_diario['IC'] = kT_diario['IBH']*kT_diario['Rb']+kT_diario['I_DH kWh/m^2-dia']*Rd+ Ro*kT_diario['GHI kWh/m^2-dia']*Rr

    '''
    
    
    
    #---------------------------- promedio diario----------------------------
    num_dia_mensual = num_dia.resample('D').mean()                        # se extrae solamente el numero de dias del año
    kT_diario_t = pd.concat([kT_diario_t, num_dia_mensual], axis=1)       # se concatena la columna del numero de dias con el dataframe kT_diario_t
    #--------------------- promedio mensual de  GHI e Io---------------------
    H_promedio = kT_mensual.filter(items=['GHI kWh/m^2-dia'])             # filtro el H promedio calculado en el metodo anterior del dataFrame (kT_mensual)
    H_promedio.index = H_promedio.index.strftime('%Y-%m')                 # se define promedio del idice mensualmente
    dias_promedio = [17,47,75,105,135,162,198,228,258,288,318,344]        # escoge el dia promedio del mes segun tabla 1.4 de Tiwari 
    kT_mensual_t = kT_diario_t[kT_diario_t.n_dia.isin(dias_promedio)]     # la funcion .isin(), permite escoger el numero de dia que propone la tabla 1.4 de tiwari (para los promedios mensuales de Io)
    kT_mensual_t = kT_mensual_t.filter(items=['Io (kWh/m^2)','n_dia'])    # se extrae las columnas deseadas
    kT_mensual_t.index = kT_mensual_t.index.strftime('%Y-%m')             # se define promedio del idice mensualmente 
    kT_mensual_t = pd.concat([H_promedio, kT_mensual_t], axis=1)          # se concatena (H_promedio, kT_mensual_t)
    kT_mensual_t['kT'] = kT_mensual_t['GHI kWh/m^2-dia']/kT_mensual_t['Io (kWh/m^2)'] # se calcula el kT(indice de claridad mensual)
    kT_mensual_t['I_DH kWh/m^2-dia'] = kT_mensual_t['GHI kWh/m^2-dia']*(1.403 - 1.672*kT_mensual_t['kT'])  # calculo de irradiancia difusa horizontal MENSUAL
    kT_mensual_t['IB_Tiw']=kT_mensual_t['GHI kWh/m^2-dia'] - kT_mensual_t['I_DH kWh/m^2-dia']
    
    

    return kT_diario_t, kT_mensual_t

kT_diario_t, kT_mensual_t  = kt_bdd_tiwari (GHI_diario, num_dia, kT_mensual)   


'''
# https://pypi.org/project/windrose/    # enlace de ejemplo

$ pip install windrose
$ pip install git+https://github.com/python-windrose/windrose
or

$ git clone https://github.com/python-windrose/windrose
$ python setup.py install


from windrose import WindroseAxes
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import numpy as np

# Create wind speed and direction variables

ws = np.random.random(500) * 6
wd = np.random.random(500) * 360


ax = WindroseAxes.from_ax()
ax.bar(wd, ws, normed=True, opening=0.8, edgecolor='white')
ax.set_legend()

'''
#_______________________GRAFICAS DE ROSA DE LOS VIENTOS______________________

veloc = INTER_vel['Wind Speed']
direc = INTER_direc['Wind Direction']
veloci = np.array(veloc)
direcc = np.array(direc)
    # Histograma apilado con resultados normados (mostrados en porcentaje)
ax = WindroseAxes.from_ax()
ax.bar(direcc, veloci, normed=True, opening=0.8, edgecolor='black')
ax.set_legend(title="Rangos de velocidad del viento [m/s]", bbox_to_anchor=(1,0,1,1)) # bbox_to_anchor: 1er valor.- 1: der y 0: izq ; 2do valor.- 1: arriba y 0:abajo ; 3er valor.- no se ven cambios ; 4to valor.- no se ven cambios
plt.title('Diagrama de la Rosa de los Vientos Normalizado')
plt.show()

# Histograma apilada, no normalizada, con límites de bins. con resultados normados (mostrados en porcentaje)
ax = WindroseAxes.from_ax()
ax.box(direcc, veloci, bins=np.arange(0, 8, 1), edgecolor='black')
ax.set_legend(title="Niveles o capas", bbox_to_anchor=(1,0,1,1)) # bbox_to_anchor: 1er valor.- 1: der y 0: izq ; 2do valor.- 1: arriba y 0:abajo ; 3er valor.- no se ven cambios ; 4to valor.- no se ven cambios
plt.title('Diagrama de la Rosa de los Vientos Tipo Histograma')
plt.show()

 # Rosa de los vientos en representación llena con mapa de colores controlado.
ax = WindroseAxes.from_ax()
ax.contourf(direcc, veloci, bins=np.arange(0, 8, 1),cmap=cm.hot)
ax.contour(direcc, veloci, bins=np.arange(0, 8, 1),colors='black')
    #ax.contour(wd, ws, bins=np.arange(0, 8, 1),cmap=cm.hot,lw=3)
ax.set_legend(title="Capas o niveles", bbox_to_anchor=(1,0,1,1))
plt.title('Diagrama de la Rosa de los Vientos Tipo Mapa')
plt.show()

# Histograma de frecuencia de direcciones (diagrama de barras)
tabla = ax._info['table']
frec = np.sum(tabla, axis=0)
direccion = ax._info['dir']
direc = np.array(direccion)
forma = direc.shape[0]
plt.figure(30)
plt.bar(np.arange(forma), frec, align='center',edgecolor='black', linewidth='1.5', color='blue', alpha=1)
plt.title('Frecuencia de Direcciones')  # Colocamos el título
xlabels = ('N','','N-E','','E','','S-E','','S','','S-O','','O','','N-O','')
plt.xticks(np.arange(forma), xlabels, rotation = 0)  # Colocamos las etiquetas del eje x, en este caso, los días.
plt.xlabel('Rumbos')
plt.ylabel('Frecuencia relativa[m/s]')
plt.show()



#___________________________MÉTODO PROBABILISTICO____________________________


#--------------------------PARAMETROS DE WEIBULL---------------------------

'''
desviacion_std_DIA = INTER_vel.resample('D').std()                         # desviacion estandar de la velocidad interpolada
desviacion_std_DIA.columns=['σ std']                                       # cambio el nombre de la columna
v_prom_DIA = INTER_vel.resample('D').mean()                                # promedio diario de la velocidad interpolada
v_prom_DIA.columns=['v_prom (m/s)']                                        # cambio el nombre de la columna
parametros = pd.concat([desviacion_std_DIA, v_prom_DIA], axis=1)           # se concatena todos los valores calculados
parametros['k'] = (parametros['σ std']/parametros['v_prom (m/s)'])**-1.086 # se calcula el parametro k

parametros['c'] = parametros['v_prom (m/s)']*(0.568+(0.433/parametros['k']))**(-1/parametros['k']) # se calcula el parametro k

'''

desviacion_std_ANUAL = INTER_vel.resample('Y').std()                         # desviacion estandar de la velocidad interpolada
desviacion_std_ANUAL.columns=['σ std']                                       # cambio el nombre de la columna
v_prom_ANUAL = INTER_vel.resample('Y').mean()                                # promedio diario de la velocidad interpolada
v_prom_ANUAL.columns=['v_prom (m/s)']                                        # cambio el nombre de la columna
parametros = pd.concat([desviacion_std_ANUAL, v_prom_ANUAL], axis=1)         # se concatena todos los valores calculados
parametros['k'] = (parametros['σ std']/parametros['v_prom (m/s)'])**-1.086   # se calcula el parametro k

parametros['c'] = parametros['v_prom (m/s)']*(0.568+(0.433/parametros['k']))**(-1/parametros['k']) # se calcula el parametro k


k = parametros['k'].values[0]                  # Adquiere el valor float de la FACTOR DE FORMA (k)
c = parametros['c'].values[0]                  # Adquiere el valor float de la FACTOR DE ESCALA (c)
#----- velocidad minima y maxima del DataFrame (anual)---------------
v_min_anual = INTER_vel.resample('Y').min()                                  # valor minimo anual de la velocidad interpolada
v_min_anual = v_min_anual['Wind Speed'].values[0]                            # Adquiere el valor float de la velocidad minima (v_min_anual)
v_max_anual = INTER_vel.resample('Y').max()                                  # valor maximo anual de la velocidad interpolada
v_max_anual = v_max_anual['Wind Speed'].values[0]                            # Adquiere el valor float de la velocidad maxima (v_max_anual)


#-------pasar el dataFrame de la velocidad interpolada a tipo array---------
vel_array = INTER_vel.to_numpy()


#----------------------------PRUEBA DE WEIBULL--------------------------

def weib(vel_array,c,k):
    return (k/c) * (vel_array/c)**(k - 1) * np.exp(-(vel_array/c)**k)



#fdp=(k/c)*(v/c)**(k-1)*np.exp(-(v/c)**k)
    
'''
#----------OTRO METODO PARA CALCULAR LOS PARAMETROS c, k------------
param1 = s.exponweib.fit(vel_array, floc=0, f0=1)
x1 = np.linspace(v_min_anual, v_max_anual, 1000)

shape1 = param1[1] # k: parámetro de forma
scale1 = param1[3] # c: parámetro de escala
    


s11 = scale1*np.random.weibull(shape1, 10000)
plt.figure(23)
plt.plot(x1, weib(x1, scale1, shape1), label='Weibull')
plt.hist(s11, density=True, alpha=1, edgecolor='black', label='Histograma (random)')
plt.title('Densidad de probabilidad experimental y teórica usando la Función de densidad de Weibull') # se usa la función de weibull para graficar.
plt.xlabel('Velocidad del Viento [m/s]')
plt.ylabel('Densidad de probabilidad')
plt.legend()
plt.show()
'''

#rv= stats.exponweib(c,k).rvs(size=1000)

#--------------este metodo resulta mas conveniente-----------------
x1 = np.linspace(v_min_anual, v_max_anual, 1000)            # determina el numero de valores en el eje x para la grafica
s11 = c*np.random.weibull(k, 10000)
plt.figure()
plt.plot(x1, weib(x1, c, k), label='Weibull')          # SE USA NUESTRA PROPIA FUNCION DE WEIBULL
plt.hist(s11, density=True, alpha=1, edgecolor='black', bins= 20, label='Histograma (random)')
plt.title('Densidad de probabilidad experimental y teórica usando la Función de densidad de Weibull') # se usa la función de weibull para graficar.
plt.xlabel('Velocidad del Viento [m/s]')
plt.ylabel('Densidad de probabilidad')
plt.legend()
plt.show()


#-------segunda manera de graficar weibull, pertenece al sitema python-------- 
weibull=stats.exponweib(c,k).pdf(x1)   # FDP
plt.figure()
plt.plot(x1,weibull)
plt.show

#--------------- histograma mas fdp------------

rv= stats.exponweib(c,k).rvs(size=1000)
plt.figure()
plt.hist(rv, density=True, edgecolor='black',bins=20, label='GRAFICAS JUNTAS')
plt.plot(x1,weibull)
plt.title('Función de densidad de Weibull') # se usa la función de weibull para graficar.
plt.xlabel('Velocidad del Viento [m/s]')
plt.ylabel('Densidad de probabilidad')
plt.legend()
plt.show()



#--------GRAFICA DE LA CURVA DE POTENCIA VS VELOCIDAD Y LA GRAFICA DE DENSIDAD DE PROBABILIDAD-----


x3 = np.linspace(0, 25, 1000)                             # determina el numero de valores en el eje x para la grafica
y3 = weib(x3, c, k)                                       # determina los valores del eje y de la segunda curva
y4 = spline(x3)                                           # determina los valores del eje y de la primera curva

fig, ax3 = plt.subplots()                                 # determina el figure y el ax el subplot()


color = 'tab:red'                                         # determona el color del delineado de la funcion
ax3.set_xlabel('Velocidad de viento (m/s)')               # nombra el eje x
ax3.set_ylabel('Densidad de probabilidad', color=color)   # nombra el eje y
label1 = ax3.plot(x3, y3, color=color, label='Densidad de probabilidad') # grafica los parametros x e y, con el color determinado
ax3.tick_params(axis='y', labelcolor=color)               # colorea los valores del eje y

ax4 = ax3.twinx()                                         # instancia un segundo eje que comparta el mismo eje x

color = 'tab:blue'                                        # determona el color del delineado de la funcion
ax4.set_ylabel('Potencia (W)', color=color)               # nombra el eje y
label2 = ax4.plot(x3, y4, color=color, label= 'Curva potencia')          # grafica los parametros x e y, con el color determinado
ax4.tick_params(axis='y', labelcolor=color)               # colorea los numerales del eje y
plt.title('CURVA DE POTENCIA  y PROBABILIDAD DE DENSIDAD DE VIENTO') # titulo de la grafica

# agrega las dos etiquetas en una sola
lns = label1 + label2
labs = [l.get_label() for l in lns]
ax3.legend(lns, labs, loc= 'center right', shadow=True, fancybox=True)

fig.tight_layout()                                        # para que la etiqueta del eje y derecho no se recorte
plt.show()
  

#plt.title('Densidad de probabilidad experimental y teórica usando la Función de densidad de Weibull') # se usa la función de weibull para graficar.

#------ajuste de la ecuacion de la curva de weibull, para la ecuacion de la curva-----
x_weib = np.array(x3)
y_weib = np.array(weib(x3, c, k))
ajuste = np.polyfit(x_weib, y_weib, 10)
a = np.poly1d(ajuste)
print(a)

#------ajuste de la ecuacion de la curva de potencia velocidad, para la ecuacion de la curva-----
x_pv = np.array(x3)
y_pv = np.array(spline(x3))
ajuste_pv = np.polyfit(x_pv, y_pv, 10)
a_pv = np.poly1d(ajuste_pv)
print(a_pv)

#produc_polinom = np.poly1d(a)*np.poly1d(a_pv)
produc_polinom = a*a_pv
integral = np.polyint(produc_polinom)


pot_prob2 = np.polyval(integral, vel_parada) - np.polyval(integral, vel_arranque)

energia_prob_anual = pot_prob2*8760

#produc_polinom = np.poly1d(produc_polinom, variable='z')
#dz = integrate(produc_polinom, (z, 2, 25))








desviacion_std_MES = INTER_vel.resample('M').std() 


    



#---------------------CONVOLUCION METODO WEIBULL----------------------

Pv = np.poly1d(y4)   # polinomio de la potencia en funcion de la velocidad
fv = np.poly1d(y3)   # polinomio de la distribucion de weibul en funcion de la velocidad

Pprom_prob = Pv*fv   # multiplicacion de los dos polinomios
#sp.init_printing()   # cambia las letras de salida en pantalla
#z = symbols('z')
#poli_z = np.poly1d(Pprom_prob, variable='z')
#print(poli_z)



integ = np.polyint(Pprom_prob)
print(integ)



#---- ESTE AJUSTE DE POLIOMIO NO FUNCIONA, PORQUE (integ) ES UN POLINOMIO MUY ''GRANDE''
'''
y_inte = np.array(integ(x3))
ajuste_inte = np.polyfit(x_pv, y_inte, 10)
a_inte = np.poly1d(ajuste_inte)
print(a_inte)
'''




'''
pot_pb = np.polyval(integ, vel_parada) - np.polyval(integ, vel_arranque)  # SI SE INTEGRA PERO NO SE PUEDE CALCULAR
'''
#________________________________GRAFICAS FINALES____________________________

#------------------------GRAFICAS PARA EL RECURSO EOLICO---------------------

v_viento_bdd = BDD_vel_v.plot().set_title('Registro de la velocidad del viento (BDD)')            # Grafica del registro de velocidad del viento (sin tratamiento de datos BDD)
v_viento_filtrada = INTER_spl_vel.plot(linewidth=0.7).set_title('Registro de la velocidad del viento (INTERPOLADA Y FILTRADA)')  # Grafica del registro de velocidad del viento (filtrada e interpolada)

p_eolica_bdd = p_eolica.plot().set_title('Potencia eólica generada (MÉTODO CRONOLÓGICO)')  # Grafica de la potencia eolica generada (metodo cronologico para BDD)
plt.ylabel('Potencia [W]', fontsize=16)





#-----------------------------MENÚ PRINCIPAL---------------------------------
##--------- creacion de menu y submenu con tkinter --------------------------
ventana=tk.Tk()                                       #creacion de la ventana
ventana.title('Evaluación de Recurso Solar y Eólico') #titulo de la ventana
ventana.geometry('600x300')                           #tamaño de la ventana 600x300
ventana.iconbitmap('BUHO_EPN_big.ico')                #ingreso del icono en la ventana
fondo=ImageTk.PhotoImage(Image.open ('energías-renovables-5.jpg').resize((600, 400)))   # para fondo de ventana
fondo1=Label(image=fondo)                             
fondo1.pack()

mi_menu=tk.Menu(ventana)                              #creacion de menu en la ventana con una nueva variable 'mi_menu'

##------------------------menu solar-----------------------------------------
menu_solar=tk.Menu(mi_menu, tearoff=0)                                  #creacion de sub-menu en la ventana con la nueva variable 'mi_menu'.....tearoff=0 sirve para corregir error del submenu
menu_solar.add_command(label='Método de Masters',command=f_masters)     #Opciones del menú
menu_solar.add_command(label='Método de Tiwari', command=f_tiwari)      #Opciones del menú
mi_menu.add_cascade(label='Evaluación solar', menu=menu_solar)          #nombre de la opcion principal para sub-menu

#-------------------------menu eólico----------------------------------------
menu_eolico=tk.Menu(mi_menu, tearoff=0)                                      #creacion de sub-menu en la ventana con la nueva variable 'mi_menu'.....tearoff=0 sirve para corregir error del submenu
menu_eolico.add_command(label='Método cronológico', command=f_cronologico)   #Opciones del menú
menu_eolico.add_command(label='Método estadístico', command=f_estadistico)   #Opciones del menú
mi_menu.add_cascade(label='Evaluación Eólica',menu=menu_eolico)              #nombre de la opcion principal para sub-menu

#------------------------submenu salir---------------------------------------
mi_menu.add_command(label='Salir', command=mensaje)   #llamado de la funcion mensaje, para cerrar ventana


ventana.config(menu=mi_menu)
ventana.mainloop()                               #evita que se cierre la ventana











