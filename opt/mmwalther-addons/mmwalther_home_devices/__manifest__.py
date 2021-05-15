# -*- coding: utf-8 -*-

{
    'name' : 'MmWalther Home Devices',
    'version': '1.0',
    'author':   'Michael Walther',
    'website' : 'https://www.mmwalther.name/odoo',
    'category': 'Smart Home',
    'depends' : ['base', 'mmwalther', 'mail'],
    'description': """
Electronic devices in a home
    """,
    'data': [
        'security/home_security.xml',
        'security/ir.model.access.csv',
        'views/home_views.xml',
        'views/home_device_views.xml',
        'views/home_device_discovery_views.xml',
        'views/certificate_views.xml',
    ],
    'demo': [       # demo data is required to execute tests
         'data/devices.xml',
#        'data/analytic_demo.xml',
#        'data/analytic_account_demo.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
