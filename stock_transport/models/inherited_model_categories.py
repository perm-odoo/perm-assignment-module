from odoo import models,fields

class InheritedStockPickingBatch(models.Model):
    _inherit='fleet.vehicle.model.category'
    _rec_name_search = ['complete_name']

    max_weight=fields.Float(string="Max Weight(Kg)")
    max_volume=fields.Float(string="Max Volume(cubic meters)")
    display_name = fields.Char(compute='_compute_display_name')

    def _compute_display_name(self):
        for record in self:
            record.display_name = f"{record.name} ({record.max_weight}kg, {record.max_volume}㎥)"