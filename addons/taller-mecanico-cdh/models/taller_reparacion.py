from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date

class TallerReparacion(models.Model):
    _name = 'taller.reparacion'
    _description = 'Reparación de Vehículo'

    name = fields.Char(string='Orden de Reparación', required=True, copy=False, default='Nuevo')
    vehiculo_id = fields.Many2one('taller.vehiculo', string='Vehículo', required=True)
    fecha_ingreso = fields.Date(string='Fecha de Ingreso', required=True, default=fields.Date.today)
    fecha_salida = fields.Date(string='Fecha de Salida')
    estado = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('en_proceso', 'En Proceso'),
        ('finalizado', 'Finalizado')
    ], string='Estado', required=True, default='pendiente')
    mecanico_id = fields.Many2one('taller.mecanico', string='Mecánico')
    repuesto_ids = fields.One2many('taller.repuesto.linea', 'reparacion_id', string='Repuestos Usados')
    total_repuestos = fields.Monetary(string='Total de Repuestos', compute='_compute_total_repuestos', store=True)
    currency_id = fields.Many2one('res.currency', string='Moneda', default=lambda self: self.env.company.currency_id)

    @api.depends('repuesto_ids.subtotal')
    def _compute_total_repuestos(self):
        for record in self:
            record.total_repuestos = sum(record.repuesto_ids.mapped('subtotal'))

    # @api.onchange('estado')
    def _onchange_estado(self):
        if self.estado == 'en_proceso':
            self.fecha_salida = False

        if self.estado == 'finalizado' and not self.fecha_salida:
            self.fecha_salida = fields.Date.today()

    @api.constrains('fecha_salida', 'fecha_ingreso')
    def _check_fechas(self):
        for record in self:
            if record.fecha_salida and record.fecha_salida < record.fecha_ingreso:
                raise ValidationError("La fecha de salida no puede ser anterior a la fecha de ingreso.")

    def action_iniciar_reparacion(self):
        for record in self:
            record.estado = 'en_proceso'
            record._onchange_estado()

    def action_finalizar_reparacion(self):
        for record in self:
            record.estado = 'finalizado'
            record._onchange_estado()
