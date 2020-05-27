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
                                    instance.order_catalog_id and \
                                    instance.order_catalog_id or False
        return super().onchange_woo_instance_id()

    @api.multi
    def execute(self):
        instance = self.woo_instance_id
        values = {}
        res = super(woo_config_settings,self).execute()
        if instance:
            values['company_id'] = self.woo_company_id and self.woo_company_id.id or False
            values['order_catalog_id'] = self.woo_order_catalog_id and \
                                         self.woo_order_catalog_id.id or False
            values['warehouse_id'] = self.woo_warehouse_id and self.woo_warehouse_id.id or False
            values['country_id'] = self.woo_country_id and self.woo_country_id.id or False
            values['lang_id'] = self.woo_lang_id and self.woo_lang_id.id or False
            values['use_custom_order_prefix'] = self.woo_use_custom_order_prefix or False
            values['order_prefix'] = self.woo_order_prefix or ''
            values['import_order_status_ids'] = [(6,0,self.woo_import_order_status_ids.ids)]
            values['stock_field'] = self.woo_stock_field and self.woo_stock_field.id or False
            values['pricelist_id'] = self.woo_pricelist_id and self.woo_pricelist_id.id or False
            values['payment_term_id'] = self.woo_payment_term_id and self.woo_payment_term_id.id or False
            values['fiscal_position_id'] = self.woo_fiscal_position_id and self.woo_fiscal_position_id.id or False
            values['discount_product_id']=self.woo_discount_product_id.id or False
            values['fee_line_id']=self.woo_fee_line_id.id or False
            values['order_auto_import']=self.woo_order_auto_import
            values['stock_auto_export']=self.woo_stock_auto_export
            values['order_auto_update']=self.woo_order_auto_update
            values['section_id']=self.woo_team_id and self.woo_team_id.id or False
            values['auto_import_product']=self.woo_auto_import_product
            values['is_set_price']=self.woo_is_set_price or False
            values['is_set_stock']=self.woo_is_set_stock or False
            values['is_publish']=self.woo_is_publish or False
            values['is_set_image']=self.woo_is_set_image or False
            values['sync_images_with_product']=self.woo_sync_images_with_product or False
            values['sync_price_with_product']=self.woo_sync_price_with_product or False
            values['is_show_debug_info']=self.woo_is_show_debug_info or False
            values['global_channel_id']=self.woo_global_channel_id and self.woo_global_channel_id.id or False
            #account Fields
            values['woo_property_account_payable_id'] = self.woo_property_account_payable_id and self.woo_property_account_payable_id.id or False
            values['woo_property_account_receivable_id'] = self.woo_property_account_receivable_id and self.woo_property_account_receivable_id.id or False
            values['last_synced_order_date'] = self.last_synced_order_date
            values['store_timezone'] = self.store_timezone

            instance.write(values)
            self.setup_woo_order_import_cron(instance)
            self.setup_woo_order_status_update_cron(instance)
            self.setup_woo_update_stock_cron(instance)

        return res
