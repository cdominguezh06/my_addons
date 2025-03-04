from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Mecanico(models.Model):
    _name = 'taller.mecanico'
    _description = 'Mecánico'

    name = fields.Char(string='Nombre', required=True)
    telefono = fields.Char(string='Teléfono', required=True)
    especialidad = fields.Selection([
        ('Motor', 'Motor'),
        ('Frenos', 'Frenos'),
        ('Suspensión', 'Suspensión'),
        ('Transmisión', 'Transmisión'),
        ('Dirección', 'Dirección')
    ], string='Especialidad', required=True)
    reparacion_ids = fields.One2many('taller.reparacion', 'mecanico_id', string='Reparaciones')
