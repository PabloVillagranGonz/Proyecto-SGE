# -*- coding: utf-8 -*-
# from odoo import http


# class Managepablo(http.Controller):
#     @http.route('/managepablo/managepablo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/managepablo/managepablo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('managepablo.listing', {
#             'root': '/managepablo/managepablo',
#             'objects': http.request.env['managepablo.managepablo'].search([]),
#         })

#     @http.route('/managepablo/managepablo/objects/<model("managepablo.managepablo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('managepablo.object', {
#             'object': obj
#         })
