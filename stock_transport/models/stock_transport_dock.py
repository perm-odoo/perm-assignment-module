from odoo import models,fields

class StockTransportDock(models.Model):
    _name='transport.dock'
    _description="Transport Dock Name"

    name = fields.Char(string="Dock Name", required=True)
