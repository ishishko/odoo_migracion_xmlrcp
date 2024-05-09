#!/usr/bin/python3
from createXMLRCP import CreateXMLRCP
from _11_field_list_product_template import field_list_check, field_no_used, fi
# BBDD Origen // Configuracion de conexion y modelo afectado.
urlOrigen = 'https://geminis.ntsystemwork.com.ar/'
dbnameOrigen = 'geminis'
userOrigen = 'admin'
pwdOrigen = 'gemi19nis'
modelOrigen = 'product.template'
conditionOrigen = [['name', '!=' ,'']]
field_listOrigen = ['name', 'street', 'phone', 'mobile', 'email', 'website', 'lang', 'weigth', 'main_id_numbre'
               'property_product_pricelist']

clientes_origen = CreateXMLRCP( urlOrigen, dbnameOrigen, userOrigen,
                                pwdOrigen, modelOrigen )

clientes_origen.models_use()