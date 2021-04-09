# -*- coding: utf-8 -*-
{
    'name': "Hospital",

    'summary': """
        This is test module for my personal use please contact the following site for more information""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Kshitij Saini",
    'website': "https://k1941996.github.io/k1941996/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Services',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','website','sale','website_form','website_sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/patient_view.xml',
        'views/doctor_view.xml',
        'views/website_form.xml',
        'views/snippets/snippets.xml',
        'views/prev_purchased_product_template.xml',
        'views/cart_template.xml'

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application':True,
    'sequence':-100
}
