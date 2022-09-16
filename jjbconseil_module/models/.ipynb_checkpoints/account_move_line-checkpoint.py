# -*- coding: utf-8 -*-
from odoo import fields, models, api


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'
    
    @api.onchange('product_id')
    def _onchange_product_id_analytic_account(self):
        for line in self:
            if not line.product_id or line.display_type in ('line_section', 'line_note'):
                continue

            line.analytic_account_id = line._get_computed_analytic_account()
            
    
    def _get_computed_analytic_account(self):
        self.ensure_one()

        if not self.product_id:
            return False
        
        if self.product_id.categ_id.s_analytic_account_default:
            return self.product_id.categ_id.s_analytic_account_default
        
        return False