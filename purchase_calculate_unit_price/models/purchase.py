# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT

class PurchaseOrder(models.Model):
    _name = "purchase.order"
    _inherit = 'purchase.order'

    @api.depends('product_id', 'partner_id')
    def action_price_update_lines(self):
        if not self.product_id:
            return

        for line in self.order_line:
            seller = line.product_id._select_seller(
                    partner_id=self.partner_id,
                    quantity=line.product_qty,
                    date=self.date_order and self.date_order.date(),
                    uom_id=line.product_uom
                )

            # if seller or not self.date_planned:
            #     self.order_line.date_planned = self.order_line._get_date_planned(seller).strftime(DEFAULT_SERVER_DATETIME_FORMAT)

            # if not seller:
            #     if self.product_id.seller_ids.filtered(lambda s: s.name.id == self.partner_id.id):
            #         self.price_unit = 0.0
            #     return

            price_unit = seller.price

            if price_unit and seller and self.currency_id and seller.currency_id != self.currency_id:
                price_unit = seller.currency_id._convert(
                    price_unit, self.currency_id, self.company_id, self.date_order or fields.Date.today())

            if seller and line.product_uom and seller.product_uom != line.product_uom:
                price_unit = seller.product_uom._compute_price(price_unit, line.product_uom)

            line.price_unit = price_unit
