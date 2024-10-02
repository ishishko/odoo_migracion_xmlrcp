#!/usr/bin/python3
from createXMLRCP import CreateXMLRCP
from _11_field_list_product_product import *

url_origen_g = "https://geminis.ntsystemwork.com.ar/"
dbname_origen_g = "geminis"
user_origen_g = "admin"
pwd_origen_g = "gemi19nis"
field_origen_g = ['name', 'image', 'image_medium', 'image_small']

# url_origen_r = "https://rake.ntsystemwork.com.ar/"
# dbname_origen_r = "rake_prod"
# user_origen_r = "admin"
# pwd_origen_r = "ra21ke"

url_destino = "https://ortopediageminis.odoo.com/"
dbname_destino = "ntsystemwork-cl-geminis17-14-0-12548781"
user_destino = "admin"
pwd_destino = "128fb3dfd05bc86e461ec8c09b10a59fdb4f107e"
field_destino = ['name']

# ========================================================================
model_origen_g = "product.template"
# model_origen_r = "product.product"
# model_destino = "product.product"

1
clientes_origen_g = CreateXMLRCP(
    url_origen_g, dbname_origen_g, user_origen_g, pwd_origen_g, model_origen_g
)

# clientes_origen_g.models_use()
# clientes_origen_g.models_fields_types(field_no_used_g)
# clientes_origen_g.models_use(field_ignore_g + field_special_g)

# 2
cliente_destino = CreateXMLRCP(
    url_destino, dbname_destino, user_destino, pwd_destino, model_origen_g
)

# cliente_destino.models_compare_fields(field_list_check_g)

# 3
data_g = clientes_origen_g.mass_read_data(field_origen_g)
# data_g = clientes_origen_g.change_data_keys(data_g, 'image', 'image_1920')
# data_g = clientes_origen_g.change_data_keys(data_g, 'image_medium', 'image_1024')
# data_g = clientes_origen_g.change_data_keys(data_g, 'image_small', 'image_128')
# data_g = clientes_origen_g.change_data_keys(data_g, 'pos_categ_id', 'pos_categ_ids')

# 4
# cliente_destino.mass_create_reg(data_g)
data_d = cliente_destino.mass_read_data(field_destino)


cliente_destino.models_update(data_g, data_d)