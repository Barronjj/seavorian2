# -*- coding: utf-8 -*-
{
    'name': "jjbconseil_module",

    'summary': """
        Permet d'affecter à la création des lignes de facture un compte analytique par défaut en fonction de la catégorie d'article associée à l'article sélectionné. """,

    'description': """
        Permet d'affecter à la création des lignes de facture un compte analytique par défaut en fonction de la catégorie d'article associée à l'article sélectionné. 
    """,

    'author': "jjbconseil",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account','product'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/product_category.xml',
    ],
}
