# -*- coding: utf-8 -*-
from odoo import fields, models


class ProductCategory(models.Model):
    _inherit = 'product.category'
    
    s_analytic_account_default = fields.Many2one('account.analytic.account', String="Compte analytique par défaut")