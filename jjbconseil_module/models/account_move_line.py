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
            
    @api.onchange('product_id')
    def onchange_product_id(self):
        if self.move_id.type in ('in_invoice','in_refund','in_receipt'):
            res = {
                'domain' : {
                'analytic_account_id' : ['|',('name', 'ilike', "FCT_"),('name', 'ilike', "PRJ_")],
                }
            }
        else:
            res = {}
        
        return res
            
   
    @api.model_create_multi
    def create(self, values):
        record = super(AccountMoveLine, self).create(values)
        if record:
            for line in record:                
                if line.move_id.type in ('in_invoice','in_refund','in_receipt','out_invoice','out_refund','out_receipt'):
                    line.update({'analytic_account_id' : line._get_computed_analytic_account()})
        
        return record            
    
    def _get_computed_analytic_account(self):
        self.ensure_one()

        if not self.product_id:
            return False
        
        if self.move_id.type in ('in_invoice','in_refund','in_receipt'):
            # facture, avoir et reçu d'achat
            if self.account_id.s_analytic_account_default:
                return self.account_id.s_analytic_account_default
            elif self.product_id.categ_id.s_analytic_account_default:
                return self.product_id.categ_id.s_analytic_account_default
            
        elif self.move_id.type in ('out_invoice','out_refund','out_receipt'):
            # facture, avoir et reçu de vente
            if self.move_id.team_id.s_analytic_account_default:
                return self.move_id.team_id.s_analytic_account_default
        
        
        return False
    
    
    def action_view_account_analytic_line(self):
        my_id = self.env['account.analytic.line'].search([('move_id', '=', self.id)])
        if my_id:
            return {
                'name': 'Ligne analytique',
                'type': 'ir.actions.act_window',
                'res_model': 'account.analytic.line',
                'view_mode': 'form',
                'res_id': my_id.id,
                'target': 'current'
            }
        else:
            return False