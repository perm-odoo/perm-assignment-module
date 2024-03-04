from odoo import models,fields

class StockTransportDock(models.Model):
    _name='transport.dock'
    _description="Transport Dock Name"

    name = fields.Char(string="Dock Name", required=True)

    def _compute_display_name(self):
        for record in self:
            record.display_name = f"{record.name} ({record.max_weight}kg, {record.max_volume}㎥)"
