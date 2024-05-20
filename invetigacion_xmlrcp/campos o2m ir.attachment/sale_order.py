#!/usr/bin/python3
from createXMLRCP import CreateXMLRCP
from _11_field_list_res_partner import field_list_check

url_origen = "https://geminis.ntsystemwork.com.ar/"
dbname_origen = "geminis"
user_origen = "admin"
pwd_origen = "gemi19nis"
model_origen = "sale.order"
condition_origen = [["id", "!=", 0]]
field_list_origen = [
    "id",
    "name",
    "display_name",
    "message_ids",
    "message_follower_ids",
    "activity_ids",
]

clientes_origen = CreateXMLRCP(
    url_origen, dbname_origen, user_origen, pwd_origen, model_origen
)

clientes_origen.models_fields_types()

data = clientes_origen.mass_read_data(field_list_origen, [["name", "=", "SO48968"]])


model_origen = "mail.compose.message"
clientes_origen = CreateXMLRCP(
    url_origen, dbname_origen, user_origen, pwd_origen, model_origen
)

clientes_origen.models_fields_types()
field_list_origen = [
    "id",
    "display_name",
    "partner_ids",
    "parent_id",
    "res_id",
]

data = clientes_origen.mass_read_data(
    field_list_origen, [["id", "=", 26393]]
)
