from odoo import models,fields,api

class InheritedStockPickingBatch(models.Model):
    _inherit='stock.picking.batch'
    
    dock_id=fields.Many2one('transport.dock',string="Dock")
    vehicle_id=fields.Many2one('fleet.vehicle', string='Vehicle')
    vehicle_category_id=fields.Many2one('fleet.vehicle.model.category', string='Vehicle Category')
    weight=fields.Float(compute="_compute_total_weight", store=True)
    volume=fields.Float(compute="_compute_total_volume", store=True)

    @api.depends("weight", "volume")
    def _compute_display_name(self):

        for record in self:
            record.display_name = f"{record.name} ({record.weight}kg, {record.volume}㎥) - {record.vehicle_id.driver_id.name}"


    @api.depends("vehicle_category_id.max_volume", "picking_ids.move_ids_without_package.product_id.volume", "picking_ids.move_ids_without_package")
    def _compute_total_volume(self):
        for batch in self:
            total = 0
            for transfer in batch.picking_ids:
                for product in transfer.move_ids_without_package:
                    total = total + (product.product_id.volume) * (product.quantity)

            if(batch.vehicle_category_id.max_volume!=0):
                batch.volume = 100 * (total / batch.vehicle_category_id.max_volume)

            else:
                batch.volume = 0
            

    @api.depends("vehicle_category_id.max_weight", "picking_ids.move_ids_without_package.product_id.weight", "picking_ids.move_ids_without_package")
    def _compute_total_weight(self):
        for batch in self:
            total = 0
            for stock_pick in batch.picking_ids:
                for stock_move in stock_pick.move_ids_without_package:
                    total = total + (stock_move.product_id.weight) * (stock_move.quantity)

            if(batch.vehicle_category_id.max_weight!=0):
                batch.weight = 100 * (total / batch.vehicle_category_id.max_weight)
            else:
                batch.weight = 0

            print(total)
