Script Ciberseguridad OSINT enumeración DNS, a través de la biblioteca dnspython.
Creamos un resolver que es capaz de enumerar varios registros de un dominio, haciendo 
previamente una [lista] de ellos. Luego la iteramos y vamos resolviendo la consulta con cada
tipo de registro (A, AAAA, MX...).
