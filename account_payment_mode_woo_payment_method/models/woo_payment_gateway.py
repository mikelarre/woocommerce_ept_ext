# Copyright 2020 Mikel Arregi Etxaniz - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import api, fields, models, exceptions, _
from odoo.addons import decimal_precision as dp


class WooPaymentGateway(models.Model):
    _inherit = "woo.payment.gateway"

    payment_mode_id = fields.Many2one(comodel_name="account.payment.mode",
                                      string="Payment Mode")
