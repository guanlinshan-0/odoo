# -*- coding: utf-8 -*-
{
    'name': "Purchase Supplier Price Update",
    'summary': "Auto update supplier price when purchase order confirmed",
    'description': """
Automatically update product supplier price when confirming a purchase order.
Key Features:
- Update supplier price automatically after PO confirmation
- Only update existing supplier info records
- Support currency synchronization
- Safe & stable without extra configuration
    """,
    'author': "guanlinshan",
    'website': "https://www.guanlinshan.com.cn",
    'category': 'Purchases',
    'version': '18.0.1.0.0',
    'license': 'OPL-1',
    'depends': ['purchase'],
    'price': 5.0,
    'currency': 'USD',
    'support': 'support@yourdomain.com',
    'installable': True,
    'application': False,
    'auto_install': False,
}
