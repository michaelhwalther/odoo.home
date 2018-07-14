# -*- coding: utf-8 -*-
{
    'name': 'Widescreen Sheet',
    'version': '1.0',
    'category': '',
    "sequence": 14,
    'complexity': "easy",
    'category': 'Hidden',
    'description': """
        Make the form sheet view use entire screen width
    """,
    'author': 'Michael Walther',
    'website': 'http://www.mmwalther.name/odoo',
    'depends': ["base"],
    'init_xml': [],
    'data': [
        "views/widescreen.xml",
    ],
    'demo_xml': [],
    'test': [
    ],
    'qweb' : [
        "static/src/xml/base.xml",
    ],
    'installable': True,
    'auto_install': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
