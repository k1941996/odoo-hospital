odoo.define('recently_purchased.s_previously_purchased_products_card',function(require){

'use strict';
const publicWidget = require('web.public.widget')
const DynamicSnippetCarousel = require('website.s_dynamic_snippet_carousel');

publicWidget.registry.dynamic_snippet_products = DynamicSnippetCarousel.extend({
    selector : '.dynamic_snippet_template',
    _fetchData : async function (){
    const cards = await this._rpc({
        route:'/shop/previously_purchased_products',
    });
//    console.log([...$(cards)].filter(node => node.nodeType === 1).map(el => el.outerHTML))
    let dx = [...$(cards)].filter(node => node.nodeType === 1).map(el => el.outerHTML)

    document.querySelector('.dynamic_snippet_template').outerHTML = dx
//    this.data = [...$(cards)].filter(node => node.nodeType === 1).map(el => el.outerHTML);
    },
});
})



odoo.define('hospital.add_to_cart',function(require){
    'use strict';
    var publicWidget = require('web.public.widget');
    var wSaleUtils = require('website_sale.utils');

    console.log(publicWidget.registry)

    publicWidget.registry.product_add_to_cart= publicWidget.Widget.extend({
        selector:'.s_prev_purchased_products',
        read_events: {
        'click .js_add_cart': '_onAddToCart',
        },

        _onAddToCart: function (ev) {
            console.log("ev",ev)
            var $card = $(ev.currentTarget).closest('.card');
            console.log("$card",$card)
            var product_id = $card.find('input[data-product-id]').data().productId
            console.log(product_id)
            this._rpc({
                route: "/shop/cart/update_json",
                params: {
                    product_id:product_id,
                    add_qty: 1
                },
            }).
            then(function (data) {
                wSaleUtils.updateCartNavBar(data);
                var $navButton = $('header .o_wsale_my_cart').first();
//                var fetch = _fetch();
                var animation = wSaleUtils.animateClone($navButton, $(ev.currentTarget).parents('.o_carousel_product_card'), 25, 40);
//                Promise.all([fetch, animation]).then(function (values) {
//                    self._render(values[0]);
//                });
            });

        },

        start: function () {
            console.log("kshitij")
            return this._super.apply(this, arguments);
        }
    });

})