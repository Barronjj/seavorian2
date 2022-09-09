# -*- coding: utf-8 -*-
# from odoo import http


# class JjbconseilModule(http.Controller):
#     @http.route('/jjbconseil_module/jjbconseil_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/jjbconseil_module/jjbconseil_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('jjbconseil_module.listing', {
#             'root': '/jjbconseil_module/jjbconseil_module',
#             'objects': http.request.env['jjbconseil_module.jjbconseil_module'].search([]),
#         })

#     @http.route('/jjbconseil_module/jjbconseil_module/objects/<model("jjbconseil_module.jjbconseil_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('jjbconseil_module.object', {
#             'object': obj
#         })
