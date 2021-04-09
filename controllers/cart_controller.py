# from odoo import http
# from odoo.http import request
# from odoo import fields
# from werkzeug.exceptions import NotFound
#
#
# class override_review_page(http.Controller):
#     @http.route(['/shop/cart'], type='http', auth="public", website=True, sitemap=False)
#     def cart(self, access_token=None, revive='', **post):
#         """
#         Main cart management + abandoned cart revival
#         access_token: Abandoned cart SO access token
#         revive: Revival method when abandoned cart. Can be 'merge' or 'squash'
#         """
#         order = request.website.sale_get_order()
#         if order and order.state != 'draft':
#             request.session['sale_order_id'] = None
#             order = request.website.sale_get_order()
#         values = {}
#         if access_token:
#             abandoned_order = request.env['sale.order'].sudo().search([('access_token', '=', access_token)], limit=1)
#             if not abandoned_order:  # wrong token (or SO has been deleted)
#                 raise NotFound()
#             if abandoned_order.state != 'draft':  # abandoned cart already finished
#                 values.update({'abandoned_proceed': True})
#             elif revive == 'squash' or (revive == 'merge' and not request.session.get('sale_order_id')):  # restore old cart or merge with unexistant
#                 request.session['sale_order_id'] = abandoned_order.id
#                 return request.redirect('/shop/cart')
#             elif revive == 'merge':
#                 abandoned_order.order_line.write({'order_id': request.session['sale_order_id']})
#                 abandoned_order.action_cancel()
#             elif abandoned_order.id != request.session.get('sale_order_id'):  # abandoned cart found, user have to choose what to do
#                 values.update({'access_token': abandoned_order.access_token})
#
#         values.update({
#             'website_sale_order': order,
#             'date': fields.Date.today(),
#             'suggested_products': [],
#         })
#         if order:
#             order.order_line.filtered(lambda l: not l.product_id.active).unlink()
#             _order = order
#             if not request.env.context.get('pricelist'):
#                 _order = order.with_context(pricelist=order.pricelist_id.id)
#             values['suggested_products'] = _order._cart_accessories()
#
#         if post.get('type') == 'popover':
#             # force no-cache so IE11 doesn't cache this XHR
#             return request.render("website_sale.cart_popover", values, headers={'Cache-Control': 'no-cache'})
#
#         return request.render("hospital.cart_template", values)
