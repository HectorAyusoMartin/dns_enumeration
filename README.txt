Script Ciberseguridad OSINT enumeración DNS, a través de la biblioteca dnspython.
Creamos un resolver que es capaz de enumerar varios registros de un dominio, haciendo 
previamente una [lista] de ellos. Luego la iteramos y vamos resolviendo la consulta con 
cada tipo de registro (A, AAAA, MX...).
También podemos usar la función Whois para obtener información relevante de cada dominio,
una vez estén enumerados estos con dns_enumeration.py
Cabe recordar que en Europa, existe normativa y regulación propia para Whois, y este NO
funcionará. En españa disponemos de https://www.dominios.es/es para este propósito.

