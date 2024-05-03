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
field_listOrigen = ['name', 'street', 'phone', 'mobile', 'email', 'website', 'lang', 'weigth', 'main_id_numbre'
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
# clientes_Destino = CreateXMLRCP( urlDestino, dbnameDestino, userDestino,
#                                 pwdDestino, modelDestino )

# Obtengo todos registros en una lista
# datosClientes = clientes_origen.read_data([16376])
datosClientes = clientes_origen.mass_read_data( field_listOrigen, conditionOrigen)
# Actualizo los campos que deseo
# datosClientes = clientes_origen.update_reg_keys(datosClientes,'id','old_id')

# crearregistros = clientes_Destino.create_reg(datosClientes)
# crearregistros = clientes_Destino.mass_create_reg2(datosClientes)
# lista_campos = clientes_origen.models_use()
