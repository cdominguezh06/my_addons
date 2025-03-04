from odoo import models, fields, api
from odoo.exceptions import ValidationError

class TallerVehiculo(models.Model):
    _name = 'taller.vehiculo'
    _description = 'Vehículo del taller'

    matricula = fields.Char(string='Matrícula', required=True, unique=True)
    marca = fields.Selection([
        ('toyota', 'Toyota'),
        ('ford', 'Ford'),
        ('chevrolet', 'Chevrolet'),
        ('nissan', 'Nissan'),
        ('honda', 'Honda'),
        ('bmw', 'BMW'),
    ], string='Marca', required=True)
    modelo = fields.Char(string='Modelo', required=True)
    anio = fields.Integer(string='Año de Fabricación', required=True)
    cliente_id = fields.Many2one('taller.cliente', string='Propietario', required=True)
    reparacion_ids = fields.One2many('taller.reparacion', 'vehiculo_id', string='Historial de Reparaciones')