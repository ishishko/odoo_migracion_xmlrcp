field_use_g = [
    "active",
    "arba_code",
    "available_in_pos",
    "available_threshold",
    "barcode",
    "categ_id",
    "code",
    "company_id",
    "contract_type",
    "cost_currency_id",
    "cost_method",
    "currency_id",
    "default_code",
    "description",
    "description_pickingout",
    "description_sale",
    "display_name",
    "event_ok",
    "event_ticket_ids",
    "expense_policy",
    "hs_code",
    "id",
    "image",
    "image_medium",
    "image_small",
    "incoming_qty",
    "inventory_availability",
    "invoice_policy",
    "is_product_variant",
    "item_ids",
    "l10n_ar_ncm_code",
    "list_price",
    "lst_price",
    "meli_state",
    "meli_status",
    "message_follower_ids",
    "message_ids",
    "message_is_follower",
    "message_partner_ids",
    "name",
    "outgoing_qty",
    "partner_ref",
    "pos_categ_id",
    "pricelist_item_ids",
    "product_tmpl_id",
    "product_variant_count",
    "product_variant_id",
    "product_variant_ids",
    "property_account_expense_id",
    "property_stock_inventory",
    "property_stock_production",
    "purchase_line_warn",
    "purchase_method",
    "purchase_ok",
    "qty_at_date",
    "qty_available",
    "responsible_id",
    "route_ids",
    "sale_line_warn",
    "sale_ok",
    "sales_count",
    "seller_ids",
    "sequence",
    "service_type",
    "standard_price",
    "stock_move_ids",
    "stock_quant_ids",
    "stock_value",
    "supplier_taxes_id",
    "taxed_lst_price",
    "taxes_id",
    "to_weight",
    "tracking",
    "type",
    "uom_id",
    "uom_po_id",
    "valuation",
    "variant_seller_ids",
    "virtual_available",
    "website_price",
    "website_price_difference",
    "website_public_price",
    "website_sequence",
    "website_size_x",
    "website_size_y",
    "website_url",
]


field_no_used_g = [
    "accessory_product_ids",
    "activity_date_deadline",
    "activity_ids",
    "activity_state",
    "activity_summary",
    "activity_type_id",
    "activity_user_id",
    "alternative_product_ids",
    "attribute_line_ids",
    "attribute_value_ids",
    "cart_qty",
    "color",
    "custom_message",
    "description_picking",
    "description_pickingin",
    "description_purchase",
    "image_variant",
    "location_id",
    "meli_attributes",
    "meli_available_quantity",
    "meli_brand",
    "meli_buying_mode",
    "meli_catalog_automatic_relist",
    "meli_catalog_item_relations",
    "meli_catalog_listing",
    "meli_catalog_product_id",
    "meli_category",
    "meli_condition",
    "meli_currency",
    "meli_default_stock_product",
    "meli_description",
    "meli_description_banner_id",
    "meli_dimensions",
    "meli_full_update",
    "meli_id",
    "meli_id_variation",
    "meli_ids",
    "meli_image_update",
    "meli_imagen_hash",
    "meli_imagen_id",
    "meli_imagen_link",
    "meli_imagen_logo",
    "meli_inventory_id",
    "meli_listing_type",
    "meli_manufacturing_time",
    "meli_master",
    "meli_max_purchase_quantity",
    "meli_mercadolibre_banner",
    "meli_model",
    "meli_multi_imagen_id",
    "meli_permalink",
    "meli_permalink_api",
    "meli_permalink_edit",
    "meli_post_required",
    "meli_price",
    "meli_price_error",
    "meli_price_fixed",
    "meli_price_update",
    "meli_product_bom",
    "meli_product_code",
    "meli_product_cost",
    "meli_product_price",
    "meli_product_supplier",
    "meli_pub",
    "meli_pub_as_variant",
    "meli_pub_principal_variant",
    "meli_pub_variant_attributes",
    "meli_publications",
    "meli_shipping_logistic_type",
    "meli_shipping_method",
    "meli_shipping_mode",
    "meli_stock",
    "meli_stock_error",
    "meli_stock_update",
    "meli_sub_status",
    "meli_title",
    "meli_update_error",
    "meli_update_stock_blocked",
    "meli_variants_status",
    "meli_video",
    "meli_warranty",
    "message_channel_ids",
    "message_last_post",
    "message_needaction",
    "message_needaction_counter",
    "message_unread",
    "message_unread_counter",
    "nbr_reordering_rules",
    "orderpoint_ids",
    "packaging_ids",
    "price",
    "price_extra",
    "pricelist_id",
    "product_image_ids",
    "property_account_creditor_price_difference",
    "property_account_income_id",
    "property_cost_method",
    "property_stock_account_input",
    "property_stock_account_output",
    "property_valuation",
    "public_categ_ids",
    "purchase_count",
    "purchase_line_warn_msg",
    "rating_count",
    "rating_ids",
    "rating_last_feedback",
    "rating_last_image",
    "rating_last_value",
    "rental",
    "reordering_max_qty",
    "reordering_min_qty",
    "route_from_categ_ids",
    "sale_delay",
    "sale_line_warn_msg",
    "stock_fifo_manual_move_ids",
    "stock_fifo_real_time_aml_ids",
    "volume",
    "warehouse_id",
    "website_description",
    "website_message_ids",
    "website_meta_description",
    "website_meta_keywords",
    "website_meta_title",
    "website_published",
    "website_style_ids",
    "weight",
]


field_system_g = [
    "__last_update",
    "create_date",
    "create_uid",
    "write_uid",
    "write_date",
]

field_m2o = [
    "currency_id",
    "meli_description_banner_id",
    "meli_default_stock_product",
    "property_stock_account_output",
    "location_id",
    "product_variant_id",
    "company_id",
    "cost_currency_id",
    "pricelist_id",
    "responsible_id",
    "create_uid",
    "pos_categ_id",
    "uom_id",
    "write_uid",
    "property_stock_production",
    "property_stock_inventory",
    "meli_pub_principal_variant",
    "property_stock_account_input",
    "property_account_expense_id",
    "activity_type_id",
    "product_tmpl_id",
    "meli_category",
    "property_account_income_id",
    "warehouse_id",
    "meli_mercadolibre_banner",
    "activity_user_id",
    "categ_id",
    "property_account_creditor_price_difference",
    "uom_po_id",
]

field_o2m_g = [
    "activity_ids",
    "attribute_line_ids",
    "orderpoint_ids",
    "packaging_ids",
    "product_image_ids",
    "rating_ids",
    "website_message_ids",
]

field_m2m_g = [
    "accessory_product_ids",
    "alternative_product_ids",
    "attribute_value_ids",
    "meli_pub_variant_attributes",
    "message_channel_ids",
    "public_categ_ids",
    "route_from_categ_ids",
    "stock_fifo_manual_move_ids",
    "stock_fifo_real_time_aml_ids",
    "website_style_ids",
]

field_error_g = [
    "partner_ref",
    "supplier_taxes_id",
    "message_ids",
    "seller_ids",
    "taxes_id",
    "variant_seller_ids",
    "product_variant_ids",
    "route_ids",
    "stock_move_ids",
    "message_follower_ids",
    "stock_quant_ids" "message_partner_ids",
    "stock_quant_ids",
    "message_partner_ids",
]

field_use_check_g = [
    "active",
    "arba_code",
    "available_in_pos",
    "available_threshold",
    "barcode",
    "code",
    "contract_type",
    "cost_method",
    "default_code",
    "description",
    "description_pickingout",
    "description_sale",
    "display_name",
    "event_ok",
    "event_ticket_ids",
    "expense_policy",
    "hs_code",
    "id",
    "image",
    "image_medium",
    "image_small",
    "incoming_qty",
    "inventory_availability",
    "invoice_policy",
    "is_product_variant",
    "item_ids",
    "l10n_ar_ncm_code",
    "list_price",
    "lst_price",
    "meli_state",
    "meli_status",
    "message_is_follower",
    "name",
    "outgoing_qty",
    "pricelist_item_ids",
    "product_variant_count",
    "purchase_line_warn",
    "purchase_method",
    "purchase_ok",
    "qty_at_date",
    "qty_available",
    "sale_line_warn",
    "sale_ok",
    "sales_count",
    "sequence",
    "service_type",
    "standard_price",
    "stock_value",
    "taxed_lst_price",
    "to_weight",
    "tracking",
    "type",
    "valuation",
    "virtual_available",
    "website_price",
    "website_price_difference",
    "website_public_price",
    "website_sequence",
    "website_size_x",
    "website_size_y",
    "website_url",
]

field_no_fiend_g = [
    "arba_code",
    "available_threshold",
    "contract_type",
    "event_ok",
    "event_ticket_ids",
    "inventory_availability",
    "item_ids",
    "meli_state",
    "meli_status",
    "pricelist_item_ids",
    "qty_at_date",
    "stock_value",
    "taxed_lst_price",
    "website_price",
    "website_price_difference",
    "website_public_price",
    "website_sequence",
    "website_size_x",
    "website_size_y",
    "website_url",
]

field_list_check_g = [x for x in field_use_check_g if x not in field_no_fiend_g]

field_ignore_g = field_system_g + field_error_g + field_no_used_g

field_special_g = field_m2o + field_o2m_g + field_m2m_g

# ==========================================================================

field_no_used_r = []

field_system_r = []

field_use_r = []

field_o2m_r = []

field_m2m_r = []

field_error_r = []

field_use_check_r = []

field_no_fiend_r = []

field_list_check_r = [x for x in field_use_check_r if x not in field_no_fiend_r]

field_ignore_r = field_system_r + field_error_r + field_no_used_r

field_special_r = field_o2m_r + field_m2m_r
