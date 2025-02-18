import phonenumbers
from phonenumbers import  geocoder , carrier , timezone
import folium
from geopy.geocoders import Photon



#funciona sin API KEY, sin servicios de terceros, pero no será tan concisa como IPINFO con su API.
#para mejorar la funcionalidad, se recomienda usar twilio. Mas concretamente su API: twilio API Phone Number V2.



def obtener_info_telefono(numero_telefono):
    """Obtener datos de Geolocalizacion de un numero de telefono"""
    numero = phonenumbers.parse(numero_telefono,'ES')
    
    #Obtener la zona horaria:
    zona_horaria = timezone.time_zones_for_number(numero)
    
    #Obtener pais / region
    pais = geocoder.description_for_number(numero , 'es')
    
    #Obtener el operador asociado con el numero
    operador = carrier.name_for_number(numero,'es')
    
    info = {
        'Numero': phonenumbers.format_number(numero, phonenumbers.PhoneNumberFormat.INTERNATIONAL),
        'Pais': pais,
        'Operador': operador,
        'Zona Horaria': zona_horaria
    }
    
    return info

def pintar_numero_mapa(localizacion, filename='phone_map.html'):
    """Construye un mapa con la localizacion del numero de telefono"""
    
    geolocalizador = Photon(user_agent='geoapiExercise')
    location = geolocalizador.geocode(localizacion)
    
    
    mapa = folium.Map(location=[location.latitude, location.longitude], zoom_start=9) 
    folium.Marker([location.latitude, location.longitude], popup=localizacion).add_to(mapa)
    #Guardar el mapa como un archivo html
    mapa.save(filename)
    print(f'Mapa guardado en {filename}')
    


if __name__ == '__main__':
    #ejemplo de uso:
    numero = '666666666'
    info = obtener_info_telefono(numero)
    print(info)
    pintar_numero_mapa(info['Pais'])
    