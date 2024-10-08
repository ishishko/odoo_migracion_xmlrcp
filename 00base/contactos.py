#!/usr/bin/python3

from createXMLRCP import CreateXMLRCP


# BBDD Origen
urlO = 'https://geminis.ntsystemwork.com.ar/'
dbnameO = 'geminis'
userO = 'admin'
pwdO = 'gemi19nis'
modelO = 'res.partner'
conditionO = [['supplier', '=', True],['name', '!=' ,'']]
field_listO = ['name', 'street', 'phone',
               'mobile', 'email', 'website', 'lang', 'weigth',
               'property_product_pricelist']

clientes_origen = CreateXMLRCP( urlO, dbnameO, userO, pwdO, modelO )


# BBDD Destino
urlD = 'https://ortopediageminis-pruebas-pagos-12791939.dev.odoo.com/'
dbnameD = 'ortopediageminis-pruebas-pagos-12791939'
userD = 'admin'
pwdD = '5c805110a6ca0ea87722640d1734a915ce3a26fb'
modelD = modelO

clientes_destino = CreateXMLRCP( urlD, dbnameD, userD, pwdD, modelD )


ids_origen = clientes_origen.search_ids( conditionO )
data_origen = clientes_origen.mass_read_data(ids_origen, field_listO)

clientes_destino.create_reg(data_origen)