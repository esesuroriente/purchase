# -*- encoding: utf-8 -*-
# Copyright 2019 - ESE SURORIENTE CAUCA < >
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Calculate Unit Price',
    'version': '13.0.1.0.0-beta.1',
    'author': 'ESE SURORIENTE CAUCA',
    'license': 'AGPL-3',
    'category': 'Other',
    'depends': [
        'purchase',
    ],
    'data': [
    #    'security/ir.model.access.csv',
        'views/purchase_order.xml',

    ],
    'installable': True,
    'auto_install': False,
}
