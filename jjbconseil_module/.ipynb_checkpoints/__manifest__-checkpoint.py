# -*- coding: utf-8 -*-
{
    'name': "jjbconseil_module",

    'summary': """
        Permet d'affecter à la sélection d'un produit dans les lignes de facture, un compte analytique par défaut en fonction de la catégorie d'article associée à l'article sélectionné. """,

    'description': """
        Permet d'affecter à sélection d'un produit dans les lignes de facture, un compte analytique par défaut en fonction de la catégorie d'article associée à l'article sélectionné. 
        Eléments impactés : 
        - Ajout du compte analytique par défaut à la catégorie d'article : s_analytic_account_default 
        - modification du XML de paramétrage d'une catégorie d'article 
        - surcharge de la fonction de création d'une ligne de facture 
    """,

    'author': "jjbconseil",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account','product','analytic','account_analytic_default','account_analytic_default_purchase','analytic_enterprise','account_accountant'],

    # always loaded
    'data': [
        'views/account_account.xml',
        'views/account_move.xml',
        'views/crm_team.xml',
        'views/product_category.xml',
    ],
}
