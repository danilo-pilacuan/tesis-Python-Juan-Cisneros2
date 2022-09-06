import pandas as pd
import ssl
ssl._create_default_https_context = ssl._create_unverified_context     # IMPORTANTE: permite la certificacion del enlace

# requisitos para solicitud de base de datos 
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


# Declarar la cadena url
url = 'https://developer.nrel.gov/api/nsrdb/v2/solar/psm3-download.csv?api_key=WT0MS4JUkh59reR6YxisV0WpybhCyfjhzTrGexNO&full_name=Juan+Cisneros&email=juan.cisneros@epn.edu.ec&affiliation=National+Polytechnic+School&reason=Thesis+research&mailing_list=true&wkt=POINT({lng}+{lat})&names={year}&attributes=dhi,dni,ghi,clearsky_dhi,clearsky_dni,clearsky_ghi,cloud_type,dew_point,air_temperature,surface_pressure,relative_humidity,solar_zenith_angle,total_precipitable_water,wind_direction,wind_speed,fill_flag&leap_day=false&utc=false&interval=60'.format(year=year, lat=lat, lng=lng)


info = pd.read_csv(url, nrows=1)                                   # Devuelve informacion del de la base de datos

timezone, elevation = info['Local Time Zone'], info['Elevation']   # Ver las propiedades especificadas
print(info)
print("-------------------------------------------------------------------------")
print(timezone)
print("-------------------------------------------------------------------------")
print(elevation)
print("-------------------------------------------------------------------------")
print("-------------------------------------------------------------------------")

# lectura del archivo csv de la url
df = pd.read_csv(url, skiprows=2)
#(Establece el índice de tiempo en el marco de datos de pandas:)
df = df.set_index(pd.date_range('1/1/{yr}'.format(yr=year), freq=interval+'Min', periods=525600/int(interval)))

print(df)

