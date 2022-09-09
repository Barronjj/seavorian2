# -*- coding: utf-8 -*-
from odoo import fields, models


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'
    
    @api.model
    def create(self, values):
        record = super(AccountMoveLine, self).create(values)
        
        if record:
            # on cherche la catégorie de l'article, puis si elle a un compte analytique par défaut, on le met dans la ligne de facture
            if record.product_id.categ_id.s_analytic_account_default:
                record.analytic_account_id = record.product_id.categ_id.s_analytic_account_default
                
        return record