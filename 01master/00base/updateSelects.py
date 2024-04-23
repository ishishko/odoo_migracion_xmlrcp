#!/usr/bin/python3

from createXMLRCP import CreateXMLRCP


# BBDD Origen // Configuracion de conexion y modelo afectado.
urlOrigen = 'https://geminis.ntsystemwork.com.ar/'
dbnameOrigen = 'geminis'
userOrigen = 'admin'
pwdOrigen = 'gemi19nis'
# Model de BBDD afectado
modelOrigen = 'res.partner'
# Condicion requeriada para search
conditionOrigen = [['name', '!=' ,''],['supplier', '=' , True]]
field_listOrigen = ['name']
# Creacion de conexion origen
clientes_origen = CreateXMLRCP( urlOrigen, dbnameOrigen, userOrigen,
                                pwdOrigen, modelOrigen )


# # BBDD Destino // Configuracion de conexion y modelo afectado.
# urlD = 'https://ortopediageminis-pruebas-pagos-12791939.dev.odoo.com/'
# dbnameD = 'ortopediageminis-pruebas-pagos-12791939'
# userD = 'admin'
# pwdD = '5c805110a6ca0ea87722640d1734a915ce3a26fb'
# # Model de BBDD afectado
# modelD = 'res.country'
# # Condicion requeriada para search
# conditionD = []
# # Creacion de conexion destino
# clientes_destino = CreateXMLRCP( urlD, dbnameD, userD, pwdD, modelD )

lista = clientes_origen.search_ids(conditionOrigen)

def dividirlist(lista, tamano):
    return [lista[n:n+tamano] for n in range(0,len(lista),tamano)]



# lista= [1,2,3,4,5,6,7,8,9,10,11,12,13]
div= dividirlist(lista,100)

condicion = [['id' , 'in' , div[0]]]
datosClientes = clientes_origen.mass_read_data(conditionOrigen)


