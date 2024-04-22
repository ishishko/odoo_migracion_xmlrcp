#!/usr/bin/python3

from createXMLRCP import CreateXMLRCP


# BBDD Origen // Configuracion de conexion y modelo afectado.
urlO = 'https://geminis.ntsystemwork.com.ar/'
dbnameO = 'geminis'
userO = 'admin'
pwdO = 'gemi19nis'
modelO = 'res.partner'
conditionO = [['supplier', '=', True],['name', '!=' ,'']]
field_listO = ['name', 'street', 'phone',
               'mobile', 'email', 'website', 'lang', 'weigth',
               'property_product_pricelist']
# Creacion de conexion origen
# clientes_origen = CreateXMLRCP( urlO, dbnameO, userO, pwdO, modelO )


# BBDD Destino // Configuracion de conexion y modelo afectado.
urlD = 'https://ortopediageminis-pruebas-pagos-12791939.dev.odoo.com/'
dbnameD = 'ortopediageminis-pruebas-pagos-12791939'
userD = 'admin'
pwdD = '5c805110a6ca0ea87722640d1734a915ce3a26fb'
conditionD = []
modelD = 'res.country'
# Creacion de conexion destino
clientes_destino = CreateXMLRCP( urlD, dbnameD, userD, pwdD, modelD )

# Lextura y obtencion de datos BBDD origen.
# ids_origen = clientes_origen.search_ids( conditionO )
# data_origen = clientes_origen.read_data(ids_origen, field_listO)
field_pais = ['name']

ids_destino_pais= clientes_destino.search_ids(conditionD)
data_destino = clientes_destino.read_data(ids_destino_pais, field_pais)


# Escritura de datos BBDD destino.
# clientes_destino.create_reg(data_origen)


# suplier_rank customer_rank
print(data_destino)
n = 0
for data in data_destino:
    print(data[0]['id'])
    data[0]['id'] = 1
    print(data[0]['id'])
