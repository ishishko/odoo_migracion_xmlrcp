#!/usr/bin/python3

from importContact import CreateXMLRCP


# BBDD Origen
urlO = 'https://geminis.ntsystemwork.com.ar/'
dbnameO = 'geminis'
userO = 'admin'
pwdO = 'gemi19nis'
modelO = 'res.partner'
conditionO = [['supplier', '=', True],['name', '!=' ,'']]
field_listO = ['name', 'street', 'supplier', 'phone',
               'mobile', 'email', 'website', 'lang', 'weigth',
               'patient', 'property_product_pricelist', 'main_id_number',
               'categ_id']

clientes_origen = CreateXMLRCP( urlO, dbnameO, userO, pwdO, modelO )


# BBDD Destino
urlD = 'https://ortopediageminis-pruebas-pagos-12791939.dev.odoo.com/'
dbnameD = 'ortopediageminis-pruebas-pagos-12791939'
userD = 'admin'
pwdD = '5c805110a6ca0ea87722640d1734a915ce3a26fb'
modelD = modelO

clientes_destino = CreateXMLRCP( urlD, dbnameD, userD, pwdD, modelD )


ids_origen = clientes_origen.search_ids( conditionO )
data_origen = clientes_origen.read_data(ids_origen, field_listO)

clientes_destino.create_reg(data_origen)