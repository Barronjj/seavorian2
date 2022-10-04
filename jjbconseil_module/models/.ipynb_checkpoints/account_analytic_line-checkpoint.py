# -*- coding: utf-8 -*-
import lxml

from odoo import fields, models, api
from lxml import etree

class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'
    
    s_move_type = fields.Selection(related="move_id.move_id.type", string="Type Facture", store=False)
    
    @api.model
    def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
        res = super(AccountAnalyticLine, self).fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu)
        if view_type == 'form':
            doc = etree.XML(res['arch'])
            # on récupère le context envoyé par le bouton 'crayon'
            move_id = self.env.context.get('my_move_id')
            # on paramètre le domain
            my_domain = "[]"
            if move_id:
                if self.env['account.move'].browse(move_id).type == "in_invoice":
                    my_domain = "['|',('name', 'ilike', 'FCT_'),('name', 'ilike', 'PRJ_')]"
                if self.env['account.move'].browse(move_id).type == "out_invoice":
                    my_domain = "[('name', 'ilike', 'ACT_')]" 

            # on cherche le champ du compta ana dans le formulaire xml pour y reporter le domain
            for node in doc.xpath("//field[@name='account_id']"):
                node.set('domain', my_domain)
            res['arch'] = etree.tostring(doc)
        return res