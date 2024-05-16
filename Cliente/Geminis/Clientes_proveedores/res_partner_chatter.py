#!/usr/bin/python3
from createXMLRCP import CreateXMLRCP
from _11_field_list_res_partner import field_list_check

urlOrigen = "https://geminis.ntsystemwork.com.ar/"
dbnameOrigen = "geminis"
userOrigen = "admin"
pwdOrigen = "gemi19nis"
modelOrigen = "res.partner"
conditionOrigen = [["name", "!=", ""]]
field_listOrigen = field_list_check
clientes_origen = CreateXMLRCP(
    urlOrigen, dbnameOrigen, userOrigen, pwdOrigen, modelOrigen
)

urlDestino = "https://ortopediageminis-test-m2m-13187875.dev.odoo.com/"
dbnameDestino = "ortopediageminis-test-m2m-13187875"
userDestino = "admin"
pwdDestino = "fc04e238836028828d282db4e11e7aaae37f4975"
modelDestino = "res.partner"
conditionDestino = [["name", "!=", ""]]
field_listDestino = []
# clientes_destino = CreateXMLRCP(
#     urlDestino, dbnameDestino, userDestino, pwdDestino, modelDestino
# )

ids = clientes_origen.search_ids(
    [["name", "like", "**NEUQUEN** VELAZQUES BASCUNAN JAIME 1640324/4"]]
)

print(ids)

clientes_origen.read_data(ids, field_list_check)

# clientes_origen.models_fields_types()
# clientes_origen.models_field_props(["activity_ids","message_follower_ids","message_ids"])


# clientes_origen = CreateXMLRCP(
#     urlOrigen, dbnameOrigen, userOrigen, pwdOrigen, 'mail.followers'
# )

# clientes_origen.models_status()

# clientes_destino.models_compare_fields(field_listOrigen)

# data_origen = clientes_origen.mass_read_data(field_listOrigen)

# # data_origen = clientes_origen.change_data_keys(data_origen,'id','old_id')
# data_origen = clientes_origen.change_data_keys(data_origen,'cuit','vat')
# data_origen = clientes_origen.change_data_keys(data_origen,'customer','customer_rank')
# data_origen = clientes_origen.change_data_keys(data_origen,'receivable_debt_ids','property_account_receivable_id')
# data_origen = clientes_origen.change_data_keys(data_origen,'supplier','supplier_rank')

# clientes_destino.models_compare_fields(field_listOrigen)

# clientes_destino.mass_create_reg(data_origen)
