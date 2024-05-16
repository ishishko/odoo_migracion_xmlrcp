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

urlDestino = "https://ortopediageminis-pruebas-pagos-12791939.dev.odoo.com/"
dbnameDestino = "ortopediageminis-pruebas-pagos-12791939"
userDestino = "admin"
pwdDestino = "258c94152632f1bd8980e7b6d6f9ec9d3345e4cc"
modelDestino = "res.partner"
conditionDestino = [["name", "!=", ""]]
field_listDestino = [
    "name",
    "street",
    "phone",
    "mobile",
    "email",
    "website",
    "lang",
    "weigth",
    "property_product_pricelist",
]
clientes_destino = CreateXMLRCP(
    urlDestino, dbnameDestino, userDestino, pwdDestino, modelDestino
)

data_origen = clientes_origen.mass_read_data(field_listOrigen)

# ids_origen = clientes_origen.search_ids()
# data_origen = clientes_origen.read_data(ids_origen, field_list_check)

data_origen = clientes_origen.change_data_keys(data_origen,'id','old_id')
# data_origen = clientes_origen.change_data_keys(data_origen,'afip_responsability_type_id','l10n_latam_identification_type_id')
data_origen = clientes_origen.change_data_keys(data_origen,'cuit','vat')
data_origen = clientes_origen.change_data_keys(data_origen,'customer','customer_rank')
# data_origen = clientes_origen.change_data_keys(data_origen,'gross_income_type','l10n_ar_gross_income_type')
# data_origen = clientes_origen.change_data_keys(data_origen,'gross_income_number','l10n_ar_gross_income_number')
# data_origen = clientes_origen.change_data_keys(data_origen,'main_id_category_id','category_id')
data_origen = clientes_origen.change_data_keys(data_origen,'receivable_debt_ids','property_account_receivable_id')
data_origen = clientes_origen.change_data_keys(data_origen,'supplier','supplier_rank')

clientes_destino.mass_create_reg(data_origen)

# ids_origen = clientes_origen.search_ids()
# data_origen = clientes_origen.read_data(ids_origen, field_list_check)
# data_origen = clientes_origen.change_data_keys(data_origen, "id", "old_id")

# clientes_origen.models_props()