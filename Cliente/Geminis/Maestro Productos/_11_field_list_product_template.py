field_system = ['calendar_last_notif_ack','create_date','create_uid',
                'has_unreconciled_entries','invoice_warn','message_follower_ids',
                'message_ids','message_is_follower','message_needaction',
                'message_needaction_counter','message_partner_ids','other_document_type_ids',
                'partner_share','partner_state','partner_state_enable','picking_warn',
                'self','signup_expiration','signup_token','signup_type',
                'signup_url','signup_valid','start_date','type','website_url'
                'write_date','write_uid']

field_no_need = []

field_error = []

field_no_used = ['meli_product_code', 'meli_catalog_product_id', 'meli_buying_mode', 
                 'accessory_product_ids', 'color', 'weight', 'rating_last_image', 
                 'is_product_variant', 'meli_publications', 'meli_full_update', 
                 'alternative_product_ids', 'property_stock_account_output', 
                 'meli_warranty', 'location_id', 'rating_count', 'rating_last_value', 
                 'meli_shipping_mode', 'sale_delay', 'pricelist_id', 'website_meta_title', 
                 'website_meta_description', 'rating_last_feedback', 
                 'nbr_reordering_rules', 'meli_product_price', 
                 'meli_pub_principal_variant', 'website_message_ids', 
                 'reordering_max_qty', 'website_style_ids', 'meli_brand', 'rental', 
                 'message_last_post', 'description_picking', 
                 'meli_catalog_automatic_relist', 'meli_shipping_method', 
                 'message_unread_counter', 'meli_update_error', 
                 'meli_variants_status', 'meli_pub_variant_attributes', 
                 'meli_product_cost', 'volume', 'meli_catalog_listing', 
                 'website_published', 'description_purchase', 'product_image_ids', 
                 'packaging_ids', 'property_valuation', 'meli_dimensions', 
                 'attribute_line_ids', 'meli_currency', 'activity_state', 
                 'property_stock_account_input', 'meli_condition', 
                 'meli_pub_as_variant', 'meli_ids', 'price', 
                 'activity_date_deadline', 'meli_stock_error', 'message_channel_ids', 
                 'meli_model', 'website_meta_keywords', 'meli_permalink_edit', 
                 'meli_title', 'custom_message', 'message_unread', 'activity_summary', 
                 'reordering_min_qty', 'meli_attributes', 'meli_description', 
                 'meli_master', 'meli_stock', 'activity_type_id', 
                 'message_needaction', 'meli_price', 'sale_line_warn_msg', 
                 'meli_category', 'message_needaction_counter', 'meli_stock_update', 
                 'purchase_line_warn_msg', 'meli_update_stock_blocked', 
                 'website_description', 'property_account_income_id', 
                 'public_categ_ids', 'meli_pub', 'route_from_categ_ids', 
                 'warehouse_id', 'activity_ids', 'meli_mercadolibre_banner', 
                 'meli_price_error', 'meli_product_bom', 'meli_listing_type', 
                 'meli_product_supplier', 'activity_user_id', 
                 'property_account_creditor_price_difference', 'meli_image_update', 
                 'description_pickingin', 'rating_ids', 'property_cost_method', 
                 'meli_catalog_item_relations', 'meli_price_update', 'purchase_count']

field_list_check = []

field_ignore = field_system + field_no_need + field_error + field_no_used