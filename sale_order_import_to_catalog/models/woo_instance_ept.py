# Copyright 2020 Mikel Arregi Etxaniz - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import api, fields, models, exceptions, _


class woo_instance_ept(models.Model):
    _inherit = "woo.instance.ept"

    order_catalog_id = fields.Many2one(
        comodel_name='product.catalog.web', string='Import to Catalog')
