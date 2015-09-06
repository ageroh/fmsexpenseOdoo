# -*- coding: utf-8 -*-
{
    'name': "Expenses",

    'summary': """Manage Expenses""",

    'description': """
        Module for managing Expenses for FMS
            - ...
    """,

    'author': "A.Gerogiannis",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
        'views/expenses.xml',
        'views/guards.xml',
        'views/vessels.xml',
    ],
    
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}
