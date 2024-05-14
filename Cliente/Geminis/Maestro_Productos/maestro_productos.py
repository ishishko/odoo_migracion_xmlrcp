#!/usr/bin/python3
from createXMLRCP import CreateXMLRCP
from _11_field_list_product_template import field_list_check, field_no_used, field_ignore

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


urlDestino = 'https://ortopediageminis-test-13057985.dev.odoo.com/'
dbnameDestino = 'ortopediageminis-test-13057985'
userDestino = 'admin'
pwdDestino = 'a9183666539c7a8f67a75fc7e7bacad169a8bbd2'
modelDestino = 'product.product'
conditionDestino = [['name', '!=' ,'']]
field_listDestino = ['name', 'street', 'phone',
               'mobile', 'email', 'website', 'lang', 'weigth',
               'property_product_pricelist']

# clientes_destino = CreateXMLRCP( urlDestino, dbnameDestino, userDestino,
#                                 pwdDestino, modelDestino )

# clientes_destino.models_compare_fields(field_list_check)