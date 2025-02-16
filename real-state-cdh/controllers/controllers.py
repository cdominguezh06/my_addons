# -*- coding: utf-8 -*-
# from odoo import http


# class Real-state-cdh(http.Controller):
#     @http.route('/real-state-cdh/real-state-cdh', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/real-state-cdh/real-state-cdh/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('real-state-cdh.listing', {
#             'root': '/real-state-cdh/real-state-cdh',
#             'objects': http.request.env['real-state-cdh.real-state-cdh'].search([]),
#         })

#     @http.route('/real-state-cdh/real-state-cdh/objects/<model("real-state-cdh.real-state-cdh"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('real-state-cdh.object', {
#             'object': obj
#         })
