# -*- coding: utf-8 -*-
from odoo import fields, models, api


class AccountAccount(models.Model):
    _inherit = 'account.account'
    
    s_analytic_account_default = fields.Many2one('account.analytic.account', String="Compte analytique par défaut")