# -*- coding: utf-8 -*-
###################################################################################
#
#    Copyright (c) 2019 ESE SURORIENTE CAUCA.
#
    # This program is free software: you can redistribute it and/or modify
    # it under the terms of the GNU Affero General Public License as
    # published by the Free Software Foundation, either version 3 of the
    # License, or (at your option) any later version.
    #
    # This program is distributed in the hope that it will be useful,
    # but WITHOUT ANY WARRANTY; without even the implied warranty of
    # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    # GNU Affero General Public License for more details.
    #
    # You should have received a copy of the GNU Affero General Public License
    # along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
###################################################################################

{
    'name': 'Purchase by Product Category',
    'version': '12.0.1.0.0-beta.1',
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
