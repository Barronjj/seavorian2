# -*- coding: utf-8 -*-
from odoo import fields, models, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    
    def _prepare_invoice_line(self):
        res = super(SaleOrderLine, self)._prepare_invoice_line()
        
        ana = False
        if self.order_id.team_id.s_analytic_account_default:
            ana = self.order_id.team_id.s_analytic_account_default
            if ana:
                res.update({'analytic_account_id': ana})
            
        return res
    
    
#     def _get_computed_analytic_account(self): # fonction identique dans account_move_line.py
#         self.ensure_one()

#         if not self.product_id:
#             return False
        
#         if self.move_id.type in ('in_invoice','in_refund','in_receipt'):
#             # facture, avoir et reçu d'achat
#             if self.account_id.s_analytic_account_default:
#                 return self.account_id.s_analytic_account_default
#             elif self.product_id.categ_id.s_analytic_account_default:
#                 return self.product_id.categ_id.s_analytic_account_default
            
#         elif self.move_id.type in ('out_invoice','out_refund','out_receipt'):
#             # facture, avoir et reçu de vente
#             if self.order_id.
        
        
#         return False