#!/usr/bin/python3
from createXMLRCP import CreateXMLRCP
from _11_field_list_res_partner import field_list_check

urlOrigen = "https://geminis.ntsystemwork.com.ar/"
dbnameOrigen = "geminis"
userOrigen = "admin"
pwdOrigen = "gemi19nis"
modelOrigen = "mail.followers"
conditionOrigen = [["id", "!=", 0]]
field_listOrigen = [
    "partner_id",
    "subtype_ids",
    "display_name",
    "res_model",
    "channel_id",
    "res_id",
]
# # clientes_origen = CreateXMLRCP(
# #     urlOrigen, dbnameOrigen, userOrigen, pwdOrigen, modelOrigen
# # )

# # clientes_origen.models_status()


# # del editor de mensajes en odoo obtengo este modelo
# modelOrigen = "mail.compose.message"
# # creo conexion con el modelo
# clientes_origen = CreateXMLRCP(
#     urlOrigen, dbnameOrigen, userOrigen, pwdOrigen, modelOrigen
# )

# # veo todos los campos tiene el modelo "mail.compose.message"
# clientes_origen.models_fields_types()

# # el modelo tiene un campo llamado 'attachment_ids'
# # veo las propiedades del campo
# clientes_origen.models_field_props(["attachment_ids"])

# el campo 'attachment_ids' tiene el siguiente valor 'relation': 'ir.attachment'
# cambio el modelo a analizar
modelOrigen = "ir.attachment"

# creo conexion con el modelos
clientes_origen = CreateXMLRCP(
    urlOrigen, dbnameOrigen, userOrigen, pwdOrigen, modelOrigen
)

# veo todos los campos tiene el modelo "mail.compose.message"
clientes_origen.models_fields_types()

# el modelo tiene 28 campos
field_listOrigen = [
    "url",
]

# veo las propiedades de todos los campos
clientes_origen.models_field_props(field_listOrigen)

# El campo "datas" es Bina
# El campo "datas_fname" tiene el nombre del archivo
# El campo "db_datas" es Bina

clientes_origen.mass_read_data(field_listOrigen,[['url','!=',False]])