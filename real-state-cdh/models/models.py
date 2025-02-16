# -*- coding: utf-8 -*-

from odoo import models, fields


class real_state_cdh(models.Model):
    _name = 'real-state-cdh.real-state-cdh'
    _description = 'real-state-cdh.real-state-cdh'

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date()
    expected_price = fields.Float(required=True)
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(selection=["Norte", "Sur", "Este", "Oeste"])