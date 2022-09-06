# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 12:27:29 2022

@author: jan-c
"""

#  https://nsrdb.nrel.gov/data-sets/api-instructions.html   (AQUI SE ENCUENTRA EL API)

#--------- USO DE APIs PARA DESCARGA DE NREL--------------------

import pandas as pd
import ssl
ssl._create_default_https_context = ssl._create_unverified_context     # IMPORTANTE: permite la certificacion del enlace


'''
import ssl
ssl.SSLContext.verify_mode = ssl.VerifyMode.CERT_OPTIONAL   # ESTA CERTIFICACION NO funciono
'''

'''
Para obtener más ayuda, póngase en contacto con nosotros. Cuando se ponga en contacto con nosotros, indíquenos a qué API está accediendo y facilite los siguientes datos de la cuenta para que podamos encontrarle rápidamente:

Correo electrónico de la cuenta: juan.cisneros@epn.edu.ec
ID de la cuenta: 90f85f18-34bd-41db-aaa3-dd2c5208e144

c07f644e-5ed2-40c4-a44c-2d958c4a9ff5
WT0MS4JUkh59reR6YxisV0WpybhCyfjhzTrGexNO
'''
'''
import locale;  
os.environ["PYTHONIOENCODING"] = "utf-8" 
myLocale=locale.setlocale(category=locale.LC_ALL, locale="en_GB.UTF-8")
print(myText.encode('utf-8', errors='ignore'))
'''


# Declare todas las variables como cadenas. Los espacios deben ser sustituidos por '+', es decir, cambiar 'Juan Cisneros' por 'Juan+Cisneros'.
 # Defina la latitud y la longitud del lugar y el año
lat, lon, year = -3.99, -79.26, 2019
  # Debe solicitar una clave api de la NSRDB desde el enlace anterior
api_key = '{{WT0MS4JUkh59reR6YxisV0WpybhCyfjhzTrGexNO}}'
#primera clave#  api_key = 'AsX2SF8ySNggZ4Vs0aiFMMNow3udAT0DV40xOt71'

#api_key = 'AsX2SF8ySNggZ4Vs0aiFMMNow3udAT0DV40xOt71'



  # Establezca los atributos a extraer (por ejemplo, dhi, ghi, etc.), separados por comas.
attributes = 'ghi,dhi,wind_speed,air_temperature,wind_direction,relative_humidity'
  # Elige el año de los datos
#year = '2019'
  # Establece el año bisiesto como verdadero o falso. True devolverá los datos de los días bisiestos si están presentes, false no.
leap_year = 'false'
  # Establezca el intervalo de tiempo en minutos, es decir, "30" es un intervalo de media hora. Los intervalos válidos son 30 y 60.
interval = '30'
  # Especifique el Tiempo Universal Coordinado (UTC), 'true' utilizará el UTC, 'false' utilizará la zona horaria local de los datos.
  # NOTA: Para utilizar los datos de la NSRDB en SAM, debe especificar UTC como "falso". SAM requiere que los datos estén en la zona horaria local.
utc = 'false'
  # Su nombre COMPLETO, utilice "+" en lugar de espacios.
your_name = 'Juan+Cisneros'
  # Su razón para utilizar la NSRDB.
reason_for_use = 'Thesis+research'
  # Su afiliación (iNSTITUCION)
your_affiliation = 'National+Polytechnic+School'
  # Su dirección de correo electrónico
your_email = 'juan.cisneros@epn.edu.ec'
  # Únase a nuestra lista de correo para que podamos mantenerle al día de las novedades.
mailing_list = 'true'


url ='https://developer.nrel.gov/api/nsrdb/v2/solar/psm3-download.csv?api_key={key}&full_name={full_name}&email={email}&affiliation={affiliation}&reason={reason}&mailing_list=true&wkt=POINT({lng}+{lat})&names={names}&attributes=dhi,dni,ghi,clearsky_dhi,clearsky_dni,clearsky_ghi,cloud_type,dew_point,air_temperature,surface_pressure,relative_humidity,solar_zenith_angle,total_precipitable_water,wind_direction,wind_speed,fill_flag&leap_day=false&utc=false&interval=60'.format(key="WT0MS4JUkh59reR6YxisV0WpybhCyfjhzTrGexNO",full_name="Juan+Cisneros",email="juan.cisneros@epn.edu.ec",affiliation="National+Polytechnic+School",reason="Thesis+research",lat="-108.5449",lng="10.5137",names="2019")

print(url)

# Devuelve sólo las 2 primeras líneas para obtener los metadatos:
info = pd.read_csv(url, skiprows=2)
  # Ver los metadatos de las propiedades especificadas, por ejemplo, la zona horaria y la elevación
#timezone, elevation = info['Local Time Zone'], info['Elevation']
# Ver metadatos.... PARA VER LA DATA SOLAMENTE SE PUEDE OMITIR.... OJO
#info


# enlace de prueva
df = pd.read_csv('https://developer.nrel.gov/api/nsrdb/v2/solar/psm3-download.csv?api_key=WT0MS4JUkh59reR6YxisV0WpybhCyfjhzTrGexNO&full_name=Sample+User&email=user@company.com&affiliation=Test+Organization&reason=Example&mailing_list=true&wkt=POINT({lon}+{lat})&names={year}&attributes=dhi,dni,ghi,clearsky_dhi,clearsky_dni,clearsky_ghi,cloud_type,dew_point,air_temperature,surface_pressure,relative_humidity,solar_zenith_angle,total_precipitable_water,wind_direction,wind_speed,fill_flag&leap_day=false&utc=false&interval=30'.format(year=year, lat=lat, lon=lon), skiprows=2)


  # Set the time index in the pandas dataframe: (Establece el índice de tiempo en el marco de datos de pandas:)
df = df.set_index(pd.date_range('1/1/{yr}'.format(yr=year), freq=interval+'Min', periods=525600/int(interval)))

  # ver la forma del DataFrame
print ('shape:'),df.shape
df.head()
#Imprimir los nombres de las columnas
print (df.columns.values)
