#!/usr/bin/python3
from xmlrpc import client
#para importar contactos solo clientes

# Conexion xmlrcp a servidor
url = 'https://geminis.ntsystemwork.com.ar/'
common = client.ServerProxy('{}/xmlrpc/2/common'.format(url))


# Obtener version Odoo // Test conexion
res = common.version()


# Carga de usuario y autentificacion geminis para obtener ID
dbname = 'geminis'
user = 'admin'
pwd = 'gemi19nis'
uid = common.authenticate(dbname,user,pwd,{})


# obtener usuarios
# models = client.ServerProxy('{}/xmlrpc/2/object'.format(url))
# primero hago un search para obtener las ids
# clientes = models.execute_kw(dbname, uid, pwd, 'res.partner', 'search', 
# [[['name', '!=', '']]])

# leo los contactos pasando la lista de clientes con un for
# contacto = models.execute_kw(dbname, uid, pwd, 'res.partner', 'read', [
# [1], ['name','street']])

# contactos = []
# numero = 0

# obtener facuras
# conectar con url
# models = client.ServerProxy('{}/xmlrpc/2/object'.format(url))
# con los datos de usuario executo el model
# primero hago un search para obtener las ids
# facturas = models.execute_kw(dbname, uid, pwd, 'account.invoice', 'search', 
# [[['display_name', '!=', '']]])


# for cliente in clientes:
#     contacto = models.execute_kw(dbname, uid, pwd, 'res.partner', 'read', [
#     [cliente], ['name','street']])
#     contactos.append(contacto)
#     numero = numero + 1
#     print(numero)

# models = client.ServerProxy('{}/xmlrpc/2/object'.format(url))
# contacto = models.execute_kw(dbname, uid, pwd, 'res.partner', 'read', [
# [1], ['name','street','afip_responsability_type_id','categ_id','nro_socio',
#       'phone','email','title','lang','customer','user_id','optout']])
models = client.ServerProxy('{}/xmlrpc/2/object'.format(url))
contacto = models.execute_kw(dbname, uid, pwd, 'res.partner', 'read', [
[1], ['state_id']])




# Respuestas
# print(res)
# print(uid)
# print(clientes)
print (contacto)

# print(len(facturas))