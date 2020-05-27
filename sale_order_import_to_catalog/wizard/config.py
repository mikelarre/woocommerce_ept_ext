# Copyright 2020 Mikel Arregi Etxaniz - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import api, fields, models, exceptions, _


class woo_config_settings(models.TransientModel):
    _inherit = 'res.config.settings'

    woo_order_catalog_id = fields.Many2one(
        comodel_name='product.catalog.web', string='Import to Catalog')

    @api.multi
    def onchange_woo_instance_id(self):
        instance = self.woo_instance_id or False
        self.woo_order_catalog_id = instance and \
                                    instance.woo_order_catalog_id and \
                                    instance.woo_order_catalog_id or False
        return super().onchange_woo_instance_id

    @api.multi
    def execute(self):
        instance = self.woo_instance_id
        values = {}
        res = super(woo_config_settings, self).execute()
        if instance:
            values['order_catalog_id'] = self.woo_order_catalog_id and \
                                         self.woo_order_catalog_id.id or False
        return res