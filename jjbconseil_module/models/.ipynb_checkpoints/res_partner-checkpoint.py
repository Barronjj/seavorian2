# -*- coding: utf-8 -*-
from odoo import fields, models, api


class Partner(models.Model):
    _inherit = 'res.partner'
    
    active = fields.Boolean(default=True, tracking=True)