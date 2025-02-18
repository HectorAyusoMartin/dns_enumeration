import folium.map
import ipinfo
from dotenv import load_dotenv
import os
import sys
import folium

#carga nuestras variables de entorno
load_dotenv()
#Configuracion
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
IP_ADDR = '79.116.189.204'

if ACCESS_TOKEN == False:
    print('No se encontro el token de acceso. Introduza uno valido en el archivo .env , o ingrese el token manualmente a continuación: ')
    token = print(input('Token de acceso: '))
    if token:
        ACCESS_TOKEN = token
    else:
        print('No se proporciono un token de acceso. Saliendo...')
    sys.exit(1)
else:
    print(f'Token de acceso: {ACCESS_TOKEN}')
    

def obtener_detalles_ip(ip, acces_token):
    """ Obtiene los detalles de geolocalizacion de una direccion IP utilizando la API de ipinfo.io """
    try:
        #definimos el cliente de la API
        handler = ipinfo.getHandler(acces_token)
        detalles = handler.getDetails(ip)
        return detalles.all
         
        
    except Exception as e:
        print(f'Ocurrio un error al obtener los detalles de la IP: {e}')
        #Cierra el programa de forma inmediata con el codigo de salida 1 (el programa fallo o ejecución anomala)
        sys.exit(1)
        
def dibujar_mapa(lat, lon, localizacion, filename='map.html'):
    """ Dibuja un mapa basandose en los detalles de geolocalizacion de una IP """
    my_map = folium.Map(location=[lat, lon], zoom_start=9)
    folium.Marker([lat,lon], popup=localizacion).add_to(my_map)
    my_map.save(filename)
    return os.path.abspath(filename)

    
    
    
        
if __name__ == '__main__':
    detalles = obtener_detalles_ip(IP_ADDR, ACCESS_TOKEN)
    print(detalles)
    print('')
    print(detalles.get('city')) #Podemos acceder a cada atributo de la respuesta utilizando el metodo get() de un diccionario{}.
    print(f'La IP {IP_ADDR} se encuentra en la ciudad de {detalles.get('city')}')
    print(f'Coordenadas: {detalles.get('loc')}')
    
    #Mostramos todos los atributos de la respuesta iterando sobre el diccionario:
    for clave, valor in detalles.items():
        print(f'{clave}: {valor}')
        print('\n')
        
        
    #Usando Folium, vamos a pintar donde esta la IP en un mapa
    
    #obtenemos los valores de latitud, longitud y localizacion
    latitude = detalles.get('latitude')
    longitude = detalles.get('longitude')
    location = detalles.get('region','Ubicacion Desconocida')
    #dibujando y guardando el mapa...
    map_file_path = dibujar_mapa(latitude, longitude, location)
    print(f'Mapa guardado en: {map_file_path}')
    
    
    
    
    
    
        
    
    
    




