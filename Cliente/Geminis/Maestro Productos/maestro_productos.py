import xmlrpc.client
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

field_listOrigen = ['name', 'street', 'phone', 'mobile', 'email', 'website', 'lang', 'weigth', 'main_id_numbre'
               'property_product_pricelist']
# Creacion de conexion origen
clientes_origen = CreateXMLRCP( urlOrigen, dbnameOrigen, userOrigen,
                                pwdOrigen, modelOrigen )