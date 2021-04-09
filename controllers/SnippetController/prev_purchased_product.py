from odoo import http
from odoo.http import request


class PreviousPurchasedProductsSnippet(http.Controller):
    @http.route('/shop/previously_purchased_products', auth="public", website=True, type="json")
    def purchasedProducts(self):

        # print(request.website.is_user()) # ->> returns true or false
        # print(request.website.is_public_user()) # ->> returns true or false

        orders = request.env.user.partner_id.sale_order_ids.filtered(lambda l: l.website_id == request.website and l.state in ('sale', 'done'))
        purchased_products = []

        for order in orders:
            for p in order.order_line:

                field = {'display_name': p.product_id.product_tmpl_id.name,
                         'id': p.product_id.id,
                         'list_price': p.product_id.product_tmpl_id.list_price,
                         'website_url': p.product_id.product_tmpl_id.website_url,
                         'image': request.env['website'].image_url(p.product_id, 'image_512'),
                         'quantity': p.product_uom_qty,
                         }
                purchased_products.append(field)

        print(purchased_products)
        count_ids={}
        for i in purchased_products:
            e = i['id']
            count_ids[e] = 0
        print(count_ids)

        for i in purchased_products:
            count_ids[i['id']] = i['quantity']+count_ids[i['id']]

        print(count_ids)

        count_ids_top_10={k: count_ids[k] for k in list(count_ids)[:10]}

        print(count_ids_top_10)


        unique_purchased_products = list({v['id']: v for v in purchased_products}.values())

        purchased_products=[]
        for i in unique_purchased_products:
            for j in count_ids_top_10:
                if i['id'] == j:
                    field = {
                         'display_name': i['display_name'],
                         'id': i['id'],
                         'list_price': i['list_price'],
                         'website_url': i['website_url'],
                         'image': i['image'],
                         }
                    purchased_products.append(field)

        print(purchased_products)

        return http.request.env['ir.ui.view']._render_template('hospital.s_previously_purchased_products_card',
                                                               {'products': purchased_products})
