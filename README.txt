Script Ciberseguridad OSINT enumeración DNS, a través de la biblioteca dnspython.

Creamos un resolver que es capaz de enumerar varios registros de un dominio, haciendo 
previamente una [lista] de ellos. Luego la iteramos y vamos resolviendo la consulta con 
cada tipo de registro (A, AAAA, MX...).

También podemos usar la función Whois para obtener información relevante de cada dominio,
una vez estén enumerados estos con dns_enumeration.py
Cabe recordar que en Europa, existe normativa y regulación propia para Whois, y este NO
funcionará. En españa disponemos de https://www.dominios.es/es para este propósito.

Commit3: Añadida la funcion Geolocalización de IP, que usa la API de IPINFO. También crea
un mapa con FOLIUM , poniendo un pin en la localización de la ip, usando la latitud y longitud
del diccionario de respuesta que nos devuelve la API.

Commit4: Añadida la funcionalidad de Geolocalización de un número telefónico usando phonenumbers,
mas concretamente los módulos geocoder, carrier y timezone.
Función de pintado en mapa con Folium, y codificación de la geolocalozación con Photon.






