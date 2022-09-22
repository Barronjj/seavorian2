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
    
    