# -*- coding: utf-8 -*-
{
    'name': 'Stop Phoning Home',
    'version': '1.0',
    'category': '',
    "sequence": 14,
    'complexity': "easy",
    'category': 'Hidden',
    'description': """
        Remove Few Phoning home feature effect from Core OpenERP.
    """,
    'author': 'Ruchir Shukla, Michael Walther',
    'website': 'www.bizzappdev.com',
    'depends': ["mail",'web'],
    'init_xml': [],
    'data': [
        "base_view.xml",
        "mail_data.xml",
    ],
    'demo_xml': [],
    'test': [
    ],
    'assets' : {
        "web.assets_qweb": [
            "odoo_no_phoning_home/static/src/xml/base.xml",
        ],
    },
    'installable': True,
    'auto_install': True,
#    'auto_install': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
