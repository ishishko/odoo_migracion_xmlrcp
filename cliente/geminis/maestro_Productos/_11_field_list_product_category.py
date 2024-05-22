field_no_used_g = [
    "child_id",
    "property_account_creditor_price_difference_categ",
    "property_stock_account_input_categ_id",
    "property_stock_account_output_categ_id",
    "property_stock_valuation_account_id",
    "removal_strategy_id",
    "route_ids",
    "total_route_ids",
]

field_system_g = [
    "__last_update",
    "create_date",
    "create_uid",
    "create_uid",
    "write_uid",
    "write_date",
]

field_use_g = [
    "complete_name",
    "display_name",
    "id",
    "name",
    "parent_id",
    "parent_left",
    "parent_right",
    "product_count",
    "property_account_expense_categ_id",
    "property_account_income_categ_id",
    "property_cost_method",
    "property_stock_journal",
    "property_valuation",
]

field_o2m_g = []

field_m2m_g = []

field_error_g = [
]

field_use_check_g = [
    "complete_name",
    "display_name",
    "id",
    "name",
    # "parent_id", # hay parent id
    # "parent_left", # sin reemplazo
    # "parent_right", # sin reemplazo
    "product_count",
    # "property_account_expense_categ_id", #  no existe '4.1.01.00.010 Venta de mercaderia'
    # "property_account_income_categ_id", # No existe '4.1.01.02.010 Compra de mercadería'
    "property_cost_method",
    # "property_stock_journal", # no existe 'Diario de stock (ARS)'
    "property_valuation",
]


field_no_fiend_g = []

field_list_check_g = [x for x in field_use_check_g if x not in field_no_fiend_g]

field_ignore_g = field_system_g + field_error_g + field_no_used_g

field_special_g = field_o2m_g + field_m2m_g

# ==========================================================================

field_no_used_r = []

field_system_r = [
    "__last_update",
    "create_date",
    "create_uid",
    "create_uid",
    "write_uid",
    "write_date",
]

field_use_r = []

field_o2m_r = []

field_m2m_r = []

field_error_r = []

field_use_check_r = []

field_no_fiend_r = []

field_list_check_r = [x for x in field_use_check_r if x not in field_no_fiend_r]

field_ignore_r = field_system_r + field_error_r + field_no_used_r

field_special_r = field_o2m_r + field_m2m_r
