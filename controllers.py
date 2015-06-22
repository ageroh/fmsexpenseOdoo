# -*- coding: utf-8 -*-
from openerp import http

# class Fmsexpensess(http.Controller):
#     @http.route('/fmsexpensess/fmsexpensess/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fmsexpensess/fmsexpensess/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fmsexpensess.listing', {
#             'root': '/fmsexpensess/fmsexpensess',
#             'objects': http.request.env['fmsexpensess.fmsexpensess'].search([]),
#         })

#     @http.route('/fmsexpensess/fmsexpensess/objects/<model("fmsexpensess.fmsexpensess"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fmsexpensess.object', {
#             'object': obj
#         })