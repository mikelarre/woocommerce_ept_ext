# Copyright 2020 Mikel Arregi Etxaniz - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import api, fields, models, exceptions, _
from odoo.addons import decimal_precision as dp


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def get_woo_order_vals(
            self, result, workflow, invoice_address, instance, partner,
            shipping_address, pricelist_id, fiscal_position,
            payment_term, payment_gateway):
        res = super().get_woo_order_vals(result, workflow, invoice_address,
                                         instance, partner, shipping_address,
                                         pricelist_id, fiscal_position,
                                         payment_term, payment_gateway)
        catalog_id = instance.catalog_id.id
        res.update({'catalog_id': catalog_id})
        return res
