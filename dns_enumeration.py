import dns.resolver

#Definimos el nombre del dominio a investigar.
dominio_objetivo = 'udemy.com'
tipo_registros = ['A','AAAA','CNAME','MX','NS','SOA','TXT']

#Definimos un cliente DNS para realizar la consulta. Creamos un Dns resolver.
resolver = dns.resolver.Resolver()

#Iteramos la lista de tipos de registro, y hacemos la consulta al servidor de nombres.
for tipo in tipo_registros:
    try:
        respuesta = resolver.resolve(dominio_objetivo,tipo)
    except dns.resolver.NoAnswer:
        print('Sin respuesta para el tipo de registro: ',tipo)
        continue
    
    #Mostramos los resultados de la consulta.
    
    print(f'{tipo} registros para {dominio_objetivo}')
    for dato in respuesta:
        print(f' {dato}')
        print('')
        
    print(f'El tipo de dato que es respuesta, donde se guarda la informacion de la consulta de resolver es {type(respuesta)}')
    print(f'Número de registros obtenidos: {len(respuesta)}')
    
