from odoo import models,fields,api

class InheritedStockPickingBatch(models.Model):
    _inherit='stock.picking'

    volume=fields.Float(string="Volume", compute="_compute_volume")
    
    @api.depends('move_ids_without_package')
    def _compute_volume(self):
            total = 0
            for transfer in self:
                for product in transfer.move_ids_without_package:
                    total = total + (product.product_id.volume) * (product.quantity)

                transfer.volume = total