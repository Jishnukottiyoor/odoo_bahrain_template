# -*- coding: utf-8 -*-


{
    'name': 'Address template for E-invoice',
    'version': '14.0.1.0.0',
    'sequence': -102,
    'summary': """Customized Address template""",
    'description': """"New Address div for invoices
    """,
    'category': 'Accounting',
    'author': 'Sarathvc/McMWG',
    'company': 'McMillan Woods Global',
    'website': "http://www.mcmillanwoods.com/",
    'depends': ['base', 'account', 'odoo_fatoorah'],
    'data': [
        'report/address_template.xml',
             ],
    'qweb': [],
    'images': [],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
