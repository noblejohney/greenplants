# -*- coding: utf-8 -*-
{
    'name' : 'Budget Allocation',
    'author'  :  "Noble Johney",
    'license' :  "Other proprietary",
    'version' : '1.0',
    'summary': 'Budget Allocation and Split up for Projects.',
    'description': "Budget Allocation and Split up for Projects.",
    'category': 'Invoicing Management',
    'depends' : ['project'],
    'data': [
        'views/purchase_order_view.xml',
        'views/configuration.xml',
        'views/sequences.xml',
        'security/ir.model.access.csv'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
