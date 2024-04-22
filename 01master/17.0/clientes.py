#!/usr/bin/python3
from xmlrpc import client
# para importar contactos solo clientes

#---------------------------------------------------------------------------

# Conexion xmlrcp a servidor
urlC = 'https://geminis.ntsystemwork.com.ar/'
commonC = client.ServerProxy('{}/xmlrpc/2/common'.format(urlC))

# Obtener version Odoo // Test conexion
testC = commonC.version()
print('Test conexion: OK', testC['server_version_info'])

# Carga de usuario y autentificacion para obtener ID
dbnameC = 'geminis'
userC = 'admin'
pwdC = 'gemi19nis'
userIdC = commonC.authenticate(dbnameC,userC,pwdC,{})
print('Id de Usuario:',userIdC)

# Obtener IDs Clientes
modelsC = client.ServerProxy('{}/xmlrpc/2/object'.format(urlC))
# Search para obtener las ids Contactos
contactosIDsC = modelsC.execute_kw(dbnameC, userIdC, pwdC, 'res.partner',
           'search', [[['name', '!=', '']]])
print('Cantidad de Contactos:', len(contactosIDsC))

# Search para obtener ids Contactos
ambosIDSC = modelsC.execute_kw(dbnameC, userIdC, pwdC, 'res.partner',
           'search', [[['customer', '=', True], ['supplier', '=', True]]])
print('Cantidad de Clientes/Proveedores:', len(ambosIDSC))

# # Extraer Clientes
client_provC=[]
numeroC=0
print('--- Obteniendo Clientes/Proveedores ---')
for id in ambosIDSC:
    data = modelsC.execute_kw(dbnameC, userIdC, pwdC, 'res.partner', 'read', [
    [id], ['name','street']])
    client_provC.append(data)
    numeroC = numeroC + 1
    if numeroC % 100 == 0: print('Obtenidos',numeroC, 'de', len(ambosIDSC))
print('Obtener Finalizado')
print("---Se han obtenido", numeroC , 'de' , len(ambosIDSC),'Clientes/Proveedores---')
print(client_provC)

#---------------------------------------------------------------------------

#---------------------------------------------------------------------------

# Conexion xmlrcp a servidor
urlI = 'https://ortopediageminis-pruebas-pagos-12791939.dev.odoo.com/'
commonI = client.ServerProxy('{}/xmlrpc/2/common'.format(urlI))

# Obtener version Odoo // Test conexion
testI = commonI.version()
print('Test conexion: OK', testI['server_version_info'])

# Carga de usuario y autentificacion para obtener ID
dbnameI = 'ortopediageminis-pruebas-pagos-12791939'
userI = 'admin'
pwdI = '5c805110a6ca0ea87722640d1734a915ce3a26fb'
userIdI = commonI.authenticate(dbnameI,userI,pwdI,{})
print('Id de Usuario:',userIdI)

# Obtener IDs Clientes
modelsI = client.ServerProxy('{}/xmlrpc/2/object'.format(urlI))
# Search para obtener las ids Contactos
contactosIDsI = modelsI.execute_kw(dbnameI, userIdI, pwdI, 'res.partner',
           'search', [[['name', '!=', '']]])
print('Cantidad de Contactos:', len(contactosIDsI))

#---------------------------------------------------------------------------

for user in client_provC:
    return_id = modelsI.execute_kw( dbnameI, userIdI, pwdI, 'res.country', 'create', [user])