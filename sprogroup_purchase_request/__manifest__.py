# -*- encoding: utf-8 -*-

{
    'name': 'Purchase Request',
    'version': '1.0-beta1',
    'category': 'Purchase',
    'author':'ESE SURORIENTE CAUCA, tung.tung11191@gmail.com',
    'description': """
Use Purchase Request module for requesting product.
    """,
    'summary': 'Create purchase request',
    'website': '',
    'images': ['static/description/icon.jpg'],
    'data': [
        'security/sprogroup_purchase_request_security.xml',
        'security/ir.model.access.csv',
        'data/sprogroup_purchase_request_data.xml',
        'views/sprogroup_purchase_request_view.xml',
    ],
    'depends': ['mail'
                ,'purchase'
                ,'stock'
                ],
    'installable': True,
    'auto_install': False,
#    'application': True,
    'sequence': 105,
    'license': 'AGPL-3',
}
