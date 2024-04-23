#!/usr/bin/python3
import xmlrpc.client
from createXMLRCP import CreateXMLRCP

# BBDD Origen // Configuracion de conexion y modelo afectado.
urlOrigen = 'https://geminis.ntsystemwork.com.ar/'
dbnameOrigen = 'geminis'
userOrigen = 'admin'
pwdOrigen = 'gemi19nis'
# Model de BBDD afectado
modelOrigen = 'res.partner'
# Condicion requeriada para search
conditionOrigen = [['name', '!=' ,'']]
field_listOrigen = ['name', 'street', 'phone', 'afip_responsability_type_id',
               'mobile', 'email', 'website', 'lang', 'weigth', 'main_id_numbre'
               'property_product_pricelist',]
# Creacion de conexion origen
clientes_origen = CreateXMLRCP( urlOrigen, dbnameOrigen, userOrigen,
                                pwdOrigen, modelOrigen )

# BBDD Destino // Configuracion de conexion y modelo afectado.
urlDestino = 'https://ortopediageminis-xmlrpc-12821112.dev.odoo.com/'
dbnameDestino = 'ortopediageminis-xmlrpc-12821112'
userDestino = 'admin'
pwdDestino = '6da60e1559204080571e99d04b550de159126985'
# Model de BBDD afectado
modelDestino = 'res.partner'
# Condicion requeriada para search
conditionDestino = [['name', '!=' ,'']]
field_listDestino = ['name', 'street', 'phone',
               'mobile', 'email', 'website', 'lang', 'weigth',
               'property_product_pricelist']
# Creacion de conexion Destino
clientes_Destino = CreateXMLRCP( urlDestino, dbnameDestino, userDestino,
                                pwdDestino, modelDestino )

# Obtengo todos registros en una lista
# datosClientes = clientes_origen.mass_read_data(conditionOrigen, field_listOrigen)
# Actualizo los campos que deseo
# datosClientes = clientes_origen.update_reg_keys(datosClientes,'id','old_id')

# crearregistros = clientes_Destino.mass_create_reg(datosClientes)
proxy = xmlrpc.client.ServerProxy("http://google.com/")
try:
    proxy.some_method()
except xmlrpc.client.ProtocolError as err:
    print("A protocol error occurred")
    print("URL: %s" % err.url)
    print("HTTP/HTTPS headers: %s" % err.headers)
    print("Error code: %d" % err.errcode)
    print("Error message: %s" % err.errmsg)