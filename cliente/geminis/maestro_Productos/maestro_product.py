#!/usr/bin/python3
from createXMLRCP import CreateXMLRCP
from _11_field_list_product_template import *

url_origen_g = "https://geminis.ntsystemwork.com.ar/"
dbname_origen_g = "geminis"
user_origen_g = "admin"
pwd_origen_g = "gemi19nis"

url_origen_r = "https://rake.ntsystemwork.com.ar/"
dbname_origen_r = "rake_prod"
user_origen_r = "admin"
pwd_origen_r = "ra21ke"

url_destino = "https://ortopediageminis-pruebas-pagos-12791939.dev.odoo.com/"
dbname_destino = "ortopediageminis-pruebas-pagos-12791939"
user_destino = "admin"
pwd_destino = "258c94152632f1bd8980e7b6d6f9ec9d3345e4cc"

# ========================================================================
model_origen_g = "product.template"
model_origen_r = "product.template"
model_destino = "product.template"

# 1
# clientes_origen_g = CreateXMLRCP(
#     url_origen_g, dbname_origen_g, user_origen_g, pwd_origen_g, model_origen_g
# )

# clientes_origen_g.models_use()
# clientes_origen_g.models_fields_types(field_use)
# clientes_origen_g.models_use(field_ignore + field_special)

# 2
# cliente_destino = CreateXMLRCP(
#     url_destino, dbname_destino, user_destino, pwd_destino, model_origen_g
# )

# cliente_destino.models_compare_fields(field_list_check)

# 3
# data_g = clientes_origen_g.mass_read_data(field_list_check)
# data_g = clientes_origen_g.change_data_keys(data_g, 'image', 'image_1920')
# data_g = clientes_origen_g.change_data_keys(data_g, 'image_medium', 'image_1024')
# data_g = clientes_origen_g.change_data_keys(data_g, 'image_small', 'image_128')
# data_g = clientes_origen_g.change_data_keys(data_g, 'pos_categ_id', 'pos_categ_ids')

# 4
# cliente_destino.mass_create_reg(data_g)


# 1
clientes_origen_r = CreateXMLRCP(url_origen_r,dbname_origen_r,user_origen_r,pwd_origen_r,model_origen_r)

clientes_origen_r.models_use()






#=========================================================================

