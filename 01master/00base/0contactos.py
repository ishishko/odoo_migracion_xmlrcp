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
conditionOrigen = [['name', '!=' ,'']]
field_listOrigen = ['name', 'street', 'phone',
               'mobile', 'email', 'website', 'lang', 'weigth',
               'property_product_pricelist']
# Creacion de conexion origen
clientes_origen = CreateXMLRCP( urlOrigen, dbnameOrigen, userOrigen,
                                pwdOrigen, modelOrigen )

# BBDD Destino // Configuracion de conexion y modelo afectado.
urlDestino = 'https://geminis.ntsystemwork.com.ar/'
dbnameDestino = 'geminis'
userDestino = 'admin'
pwdDestino = 'gemi19nis'
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
datosClientes = clientes_origen.mass_read_data(conditionOrigen, field_listOrigen)

datosClientes = clientes_origen.update_reg_keys(datosClientes,'id','old_id')

