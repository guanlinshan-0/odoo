# -*- coding: utf-8 -*-
# from odoo import http


# class PurchaseSupplierPriceUpdate(http.Controller):
#     @http.route('/purchase_supplier_price_update/purchase_supplier_price_update', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/purchase_supplier_price_update/purchase_supplier_price_update/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('purchase_supplier_price_update.listing', {
#             'root': '/purchase_supplier_price_update/purchase_supplier_price_update',
#             'objects': http.request.env['purchase_supplier_price_update.purchase_supplier_price_update'].search([]),
#         })

#     @http.route('/purchase_supplier_price_update/purchase_supplier_price_update/objects/<model("purchase_supplier_price_update.purchase_supplier_price_update"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('purchase_supplier_price_update.object', {
#             'object': obj
#         })

