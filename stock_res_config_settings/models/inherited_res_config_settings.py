from odoo import models,fields,api

class InheritedStockPickingBatch(models.TransientModel):
    _inherit='res.config.settings'

    module_stock_transport=fields.Boolean("Dispatch Management System",
        help="Transport mangement: organize packs in your fleer, or carriers.")

