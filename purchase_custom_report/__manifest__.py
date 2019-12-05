# -*- encoding: utf-8 -*-
# Copyright 2019 - ESE SURORIENTE CAUCA < >
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Purchase custom PO',
    'version': '13.0.1.0.0-beta.1',
    'category': 'Purchase',
    'author':'ESE SURORIENTE CAUCA',
    'description': """
        Purchase custom PO.
    """,
    'website': '',
    'images': ['static/description/icon.jpg'],
    'data': [

        'views/purchase_order_view.xml',
        'views/purchase_quot_view.xml',
    ],
    'depends': [
        'purchase'

    ],
    'installable': True,
    'auto_install': False,
    'license': 'AGPL-3',
}
