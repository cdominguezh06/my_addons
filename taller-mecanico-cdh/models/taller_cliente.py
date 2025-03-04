from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re

class TallerCliente(models.Model):
    _name = 'taller.cliente'
    _description = 'Cliente del taller'
    _sql_constraints = [
        ('email_unique', 'unique(email)', 'El correo electrónico debe ser único.')
    ]
    name = fields.Char(string='Nombre', required=True)
    telefono = fields.Char(string='Teléfono', required=True)
    email = fields.Char(string='Correo Electrónico', required=True, unique=True)
    direccion = fields.Text(string='Dirección')
    vehiculo_ids = fields.One2many('taller.vehiculo', 'cliente_id', string='Vehículos')

    @api.constrains('email')
    def _check_email(self):
        """ Valida que el email tenga un formato correcto y sea único """
        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        for record in self:
            if not re.match(email_regex, record.email):
                raise ValidationError('El correo electrónico no es válido.')
