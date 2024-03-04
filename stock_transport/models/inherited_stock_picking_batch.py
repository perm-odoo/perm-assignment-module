from odoo import models,fields,api

class InheritedStockPickingBatch(models.Model):
    _inherit='stock.picking.batch'
    
    dock=fields.Many2one('transport.dock',string="Dock", copy='False')
    vehicle_id=fields.Many2one('fleet.vehicle', string='Vehicle')
    vehicle_category_id=fields.Many2one('fleet.vehicle.model.category', string='Vehicle Category')
    weight=fields.Float(compute="_compute_total_weight", store=True)
    volume=fields.Float(compute="_compute_total_volume", store=True)

    @api.depends("vehicle_category_id", "move_line_ids")
    def _compute_total_volume(self):
        total = 0
        for transfer in self.move_ids:
            total = total + (transfer.product_id.volume) * (transfer.quantity)

        if(self.vehicle_category_id.max_volume!=0):
            self.volume = round(total / self.vehicle_category_id.max_volume)
        else:
            self.volume = 0

    @api.depends("vehicle_category_id", "move_line_ids")
    def _compute_total_weight(self):
        total = 0
        for transfer in self.move_ids:
            total = total + (transfer.product_id.weight) * (transfer.quantity)

        if(self.vehicle_category_id.max_volume!=0):
            self.weight = round(total / self.vehicle_category_id.max_weight)
        else:
            self.weight = 0