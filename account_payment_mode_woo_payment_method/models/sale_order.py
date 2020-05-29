# Copyright 2020 Mikel Arregi Etxaniz - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import api, fields, models, exceptions, _


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
        payment_gateway_id = res.get('payment_gateway_id')
        if payment_gateway_id:
            payment_gateway = self.env['woo.payment.gateway'].browse(
                payment_gateway_id)
            res.update({'payment_mode_id': payment_gateway.payment_mode_id.id})
        return res
