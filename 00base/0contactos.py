#!/usr/bin/python3
from createXMLRCP import CreateXMLRCP
from _11_field_list_res_partner import field_list_check

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
# clientes_origen = CreateXMLRCP( urlOrigen, dbnameOrigen, userOrigen,
#                                 pwdOrigen, modelOrigen )

# BBDD Destino // Configuracion de conexion y modelo afectado.
urlDestino = 'https://ortopediageminis-test-13057985.dev.odoo.com/'
dbnameDestino = 'ortopediageminis-test-13057985'
userDestino = 'admin'
pwdDestino = 'a9183666539c7a8f67a75fc7e7bacad169a8bbd2'
# dbnameDestino = 'ortopediageminis-pruebas-pagos-12791939'
# userDestino = 'admin'
# pwdDestino = '258c94152632f1bd8980e7b6d6f9ec9d3345e4cc'
# Model de BBDD afectado
modelDestino = 'res.partner'
# Condicion requeriada para search
conditionDestino = [['name', '!=' ,'']]
field_listDestino = ['name', 'street', 'phone',
               'mobile', 'email', 'website', 'lang', 'weigth',
               'property_product_pricelist']
# Creacion de conexion Destino
clientes_destino = CreateXMLRCP( urlDestino, dbnameDestino, userDestino,
                                pwdDestino, modelDestino )



clientes_destino.models_compare_fields(field_list_check)