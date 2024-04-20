#!/usr/bin/python3
from xmlrpc import client
# para importar contactos solo clientes

# Conexion xmlrcp a servidor
url = 'https://geminis.ntsystemwork.com.ar/'
common = client.ServerProxy('{}/xmlrpc/2/common'.format(url))

# Obtener version Odoo // Test conexion
test = common.version()
print('Test conexion: OK', test['server_version_info'])

# Carga de usuario y autentificacion para obtener ID
dbname = 'geminis'
user = 'admin'
pwd = 'gemi19nis'
userId = common.authenticate(dbname,user,pwd,{})
print('Id de Usuario:',userId)

# Obtener IDs Clientes
models = client.ServerProxy('{}/xmlrpc/2/object'.format(url))
# Search para obtener las ids Contactos
contactosIDs = models.execute_kw(dbname, userId, pwd, 'res.partner',
           'search', [[['name', '!=', '']]])
print('Cantidad de Contactos:', len(contactosIDs))
# Search para obtener ids Contactos
# IDs todos los Clientes
clientesIDS = models.execute_kw(dbname, userId, pwd, 'res.partner',
           'search', [[['customer', '=', True]]])
print('Cantidad de clientes:', len(clientesIDS))

proveedoresIDS = models.execute_kw(dbname, userId, pwd, 'res.partner',
           'search', [[['supplier', '=', True]]])
print('Cantidad de Proveedores:', len(proveedoresIDS))
ambosIDS = models.execute_kw(dbname, userId, pwd, 'res.partner',
           'search', [[['customer', '=', True], ['supplier', '=', True]]])
print('Cantidad de Clientes/Proveedores:', len(ambosIDS))
ningunoIDS = models.execute_kw(dbname, userId, pwd, 'res.partner',
           'search', [[['customer', '=', False], ['supplier', '=', False]]])
print('Cantidad de Contactos:', len(ningunoIDS))


# Extraer Clientes
client_prov=[]
numero=0
print('--- Obteniendo Clientes/Proveedores ---')
for id in ambosIDS:
    data = models.execute_kw(dbname, userId, pwd, 'res.partner', 'read', [
    [id], ['name','street']])
    client_prov.append(data)
    numero = numero + 1
    if numero % 100 == 0: print('Obtenidos',numero, 'de', len(ambosIDS))
print('Obtener Finalizado')
print("---Se han obtenido", numero , 'de' , len(ambosIDS),'Clientes/Proveedores---')

# Extraer Clientes
ninguno=[]
numero=0
print('--- Obteniendo Contacto no Asignado ---')
for id in ningunoIDS:
    data = models.execute_kw(dbname, userId, pwd, 'res.partner', 'read', [
    [id], ['name','street']])
    ninguno.append(data)
    numero = numero + 1
    if numero % 100 == 0: print('Obtenidos',numero, 'de', len(ningunoIDS))
print('Obtener Finalizado')
print("---Se han obtenido", numero , 'de' , len(ninguno),'Contacto no Asignado---')

# Extraer Proveedores
proveedores=[]
numero=0
print('--- Obteniendo Proveedores ---')
for id in proveedoresIDS:
    data = models.execute_kw(dbname, userId, pwd, 'res.partner', 'read', [
    [id], ['name','street']])
    proveedores.append(data)
    numero = numero + 1
    if numero % 100 == 0: print('Obtenidos',numero, 'de', len(proveedoresIDS))
print('Obtener Finalizado')
print("---Se han obtenido", numero , 'de' , len(proveedores),'---')

# Extraer Clientes
clientes=[]
numero=0
print('--- Obteniendo Clientes ---')
for id in clientesIDS:
    data = models.execute_kw(dbname, userId, pwd, 'res.partner', 'read', [
    [id], ['name','street']])
    proveedores.append(data)
    numero = numero + 1
    if numero % 100 == 0: print('Obtenidos',numero, 'de', len(clientesIDS))
print('Obtener Finalizado')
print("---Se han obtenido", numero , 'de' , len(proveedores),'Clientes---')


