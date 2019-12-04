# -*- coding: utf-8 -*-

from datetime import datetime

from odoo import api, fields, models, _
from odoo.addons import decimal_precision as dp
from odoo.tools import float_compare

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    categ_id = fields.Many2one('product.category',
                               'Product category',
                               required=True,
                               tracking=True,
                               )


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    note = fields.Char('Note', size=256, tracking=True)
    categ_id = fields.Many2one('product.category',
                               'Product category',
                               related='order_id.categ_id',
#                               store=True,
                               tracking=True
                               )

    @api.onchange('categ_id')
    def onchange_categ_id(self):
        self.categ_id = self.order_id.categ_id


    def _update_line_quantity(self, values):
        requests = self.mapped('order_id')
        precision = self.env['decimal.precision'].precision_get('Product Unit of Measure')
        for req in requests:
            req_lines = self.filtered(lambda x: x.order_id == req)
            msg = "<b>The request quantity has been updated.</b><ul>"
            for line in req_lines:
                if float_compare(line.product_qty, values['product_qty'], precision_digits=precision) != 0:
                    msg += "<li> %s:" % (line.product_id.display_name,)
                    msg += "<br/>" + _("Request Quantity") + ": %s -> %s <br/>" % (
                    line.product_qty, float(values['product_qty']),)
                    msg += "</ul>"
                    req.message_post(body=msg)


    def write(self, values):
        if 'product_qty' in values:
            self._update_line_quantity(values)

        res = super(PurchaseOrderLine, self).write(values)
        return res
