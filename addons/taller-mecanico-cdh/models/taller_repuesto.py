from odoo import models, fields

class TallerRepuesto(models.Model):
    _name = 'taller.repuesto'
    _description = 'Repuesto'

    name = fields.Char(string='Nombre', required=True)
    precio = fields.Monetary(string='Precio', required=True)
    currency_id = fields.Many2one('res.currency', string='Moneda', default=lambda self: self.env.company.currency_id)
