# Copyright 2020 Mikel Arregi Etxaniz - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import api, fields, models, exceptions, _
from odoo.addons import decimal_precision as dp


class woo_product_template_ept(models.Model):
    _inherit = "woo.product.template.ept"

    @api.multi
    def get_stock(self, woo_product, warehouse_id,
                  stock_type='virtual_available'):
        res = super().get_stock(woo_product, warehouse_id, stock_type)
        product = self.env['product.product'].with_context(
           warehouse=warehouse_id).browse(woo_product.product_id.id)
        return product.b2b_virtual_available
