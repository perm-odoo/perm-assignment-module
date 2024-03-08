from odoo import models,fields,api

class InheritedStockPickingBatch(models.Model):
    _inherit='fleet.vehicle.model.category'
    _rec_name_search = ['complete_name']

    max_weight=fields.Float(string="Max Weight(Kg)")
    max_volume=fields.Float(string="Max Volume(\u33A5)")
    

    @api.depends('max_weight', 'max_volume')
    def _compute_display_name(self):
        for record in self:
            record.display_name = f"{record.name} ({round(record.max_weight)}kg, {round(record.max_volume)}\u33A5)"
