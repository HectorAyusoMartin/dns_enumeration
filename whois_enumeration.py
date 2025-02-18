import whois


dominio_objetivo = 'google.com'

respuesta = whois.whois(dominio_objetivo)

print(respuesta.city) # respuesta es iterable, ademas podemos acceder a los atribuutos de forma individual, en este ejemplo, la ciudad del propietario del dominio.

print(respuesta)    # respuesta es un objeto whois, que contiene toda la informacion del dominio consultado.

# En este caso, la libreria whois nos permite obtener informacion de un dominio, como el propietario, la ciudad, el pais, la fecha de creacion, la fecha de expiracion, entre otros datos.
# La libreria whois es una herramienta muy util para obtener informacion de un dominio, y realizar investigaciones de seguridad en la red.




#TODO pasar una lista con todos los dominios y subdominios encontrados con dns_enumeration.py y obtener informacion de cada uno de ellos con whois.






