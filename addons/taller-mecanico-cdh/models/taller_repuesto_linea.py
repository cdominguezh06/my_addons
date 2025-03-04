from odoo import models, fields, api

class TallerRepuestoLinea(models.Model):
    _name = 'taller.repuesto.linea'
    _description = 'Línea de Repuestos'

    reparacion_id = fields.Many2one('taller.reparacion', string='Reparación', required=True)
    repuesto_id = fields.Many2one('taller.repuesto', string='Repuesto', required=True)
    cantidad = fields.Integer(string='Cantidad', required=True, default=1)
    subtotal = fields.Monetary(string='Subtotal', compute='_compute_subtotal', store=True)
    currency_id = fields.Many2one('res.currency', string='Moneda', related='repuesto_id.currency_id', readonly=True)

    @api.depends('repuesto_id.precio', 'cantidad')
    def _compute_subtotal(self):
        for record in self:
            record.subtotal = record.cantidad * record.repuesto_id.precio