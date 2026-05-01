# -*- coding: utf-8 -*-
{
    'name': "Purchase Supplier Price Auto Update",
    'summary': "Auto update product supplier price when purchase order confirmed",
    'description': """
This module automatically updates the product's supplier price in the product master data when a purchase order is confirmed.
Key Features:
1. Triggered after purchase order confirmation
2. Update the latest purchase price to product supplier info
3. Only update price and currency fields of supplier info
4. Skip empty product/supplier and non-material product lines
5. Detailed log records for update status
    """,
    'author': "guanlinshan",
    'website': "",
    'category': 'Purchases',
    'version': '18',
    'depends': ['purchase'],
    'data': [
        'views/views.xml',
        'views/templates.xml',
    ],
    'license': 'OPL-1',
    'installable': True,
    'application': False,
    'auto_install': False,
}