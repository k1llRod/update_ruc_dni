# -*- coding: utf-8 -*-
# from odoo import http


# class UpdateRucDni(http.Controller):
#     @http.route('/update_ruc_dni/update_ruc_dni', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/update_ruc_dni/update_ruc_dni/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('update_ruc_dni.listing', {
#             'root': '/update_ruc_dni/update_ruc_dni',
#             'objects': http.request.env['update_ruc_dni.update_ruc_dni'].search([]),
#         })

#     @http.route('/update_ruc_dni/update_ruc_dni/objects/<model("update_ruc_dni.update_ruc_dni"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('update_ruc_dni.object', {
#             'object': obj
#         })
