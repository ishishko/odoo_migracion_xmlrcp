#!/usr/bin/python3
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
field_listOrigen = ['name', 'street', 'phone', 'afip_responsability_type_id',
               'mobile', 'email', 'website', 'lang', 'weigth', 'main_id_numbre'
               'property_product_pricelist',]
# Creacion de conexion origen
clientes_origen = CreateXMLRCP( urlOrigen, dbnameOrigen, userOrigen,
                                pwdOrigen, modelOrigen )

# BBDD Destino // Configuracion de conexion y modelo afectado.
urlDestino = 'https://geminis.ntsystemwork.com.ar/'
dbnameDestino = 'geminis'
userDestino = 'admin'
pwdDestino = 'gemi19nis'
# Model de BBDD afectado
modelDestino = 'res.partner'
# Condicion requeriada para search
conditionDestino = [['name', '!=' ,'']]
field_listDestino = ['name', 'street', 'phone',
               'mobile', 'email', 'website', 'lang', 'weigth',
               'property_product_pricelist']
# Creacion de conexion Destino
clientes_Destino = CreateXMLRCP( urlDestino, dbnameDestino, userDestino,
                                pwdDestino, modelDestino )

res_partner_keys_11 = ['sale_order_count','message_is_follower','activity_summary',
                    'partner_state_enable','barcode','color','weight',
                    'gross_income_number','payment_token_count','currency_id',
                    'parent_name','invoice_ids','contracts_count','meli_update_forbidden',
                    'property_payment_term_id','zip','cuit','write_date',
                    'afip_responsability_type_id','purchase_order_count','category_id',
                    'phone','function','sale_order_ids','email_formatted',
                    'user_ids','signup_token','contact_address','trust','employee',
                    'gross_income_type','other_document_type_ids','website_meta_title',
                    'website_url','ref','commercial_partner_country_id','channel_ids',
                    'nro_socio','sale_warn','company_type','street','id','commercial_partner_id',
                    'is_company','type','monotributo_padron','child_ids','last_website_so_id',
                    'patient','message_ids','actividades_padron','website_message_ids',
                    'property_account_position_id','journal_item_count','company_id',
                    'property_account_payable_id','team_id','vat','image','event_count',
                    'impuestos_padron','impuestos_padron','website_meta_description'
                    ,'supplier_invoice_count','ref_company_ids','credit','create_uid',
                    'message_unread_counter','partner_state','empleador_padron','industry_id',
                    'last_update_padron','supplier','country_id','payment_token_ids',
                    'website','lang','receivable_debt_ids','website_description',
                    'website_published','imp_ganancias_padron','message_partner_ids'
                    ,'message_bounce','drei','property_stock_customer','__last_update',
                    'meeting_ids','city','invoice_warn','pos_order_count','activity_state',
                    'bank_ids','image_medium','activity_date_deadline','property_purchase_currency_id',
                    'mobile','message_channel_ids','email','start_date',
                    'meeting_count','website_meta_keywords','tz_offset','main_id_category_id',
                    'signup_expiration','debt_balance','date','integrante_soc_padron',
                    'total_invoiced','self','message_unread','signup_type',
                    'id_numbers','debit','create_date','property_product_pricelist',
                    'user_id','write_uid','last_time_entries_checked',
                    'name','property_stock_supplier','commercial_company_name','formated_cuit',
                    'opt_out','tz','picking_warn_msg','activity_type_id',
                    'gross_income_jurisdiction_ids','message_needaction','debit_limit',
                    'title','opportunity_count','street2','sale_warn_msg','arba_alicuot_ids',
                    'property_account_receivable_id','payable_debt_ids','purchase_warn_msg',
                    'credit_limit','actividad_monotributo_padron','message_needaction_counter',
                    'display_name','website_short_description','has_unreconciled_entries',
                    'main_id_number','company_name','opportunity_ids','invoice_warn_msg',
                    'meli_order_id','meli_buyer_id','customer','activity_ids',
                    'social_work','parent_id','active','picking_warn','state_id',
                    'property_delivery_carrier_id','activity_user_id','categ_id',
                    'property_supplier_payment_term_id','bank_account_count','default_regimen_ganancias_id',
                    'estado_padron','signup_url','calendar_last_notif_ack','message_follower_ids',
                    'purchase_warn','signup_valid','partner_share','comment','im_status',
                    'contract_ids','image_small','imp_iva_padron','meli_buyer']

# # Obtengo todos registros en una lista
# datosClientes = clientes_origen.mass_read_data(conditionOrigen, field_listOrigen)
# datosClientes = clientes_origen.update_reg_keys(datosClientes,'id','old_id')

campos = clientes_origen.models_use(res_partner_keys_11)