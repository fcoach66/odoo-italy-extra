# -*- coding: utf-8 -*-
{
    'name': 'Italian Like Sale Order Aeroo Report',
    'version': '1.0',
    'category': 'Localization/Italy',
    'sequence': 14,
    'summary': '',
    'description': """
Italian Like Sale Order / Quotation Aeroo Report
====================================================
Parameters requirements:
* total_discount: require module "sale_pricelist_discount"
* print_validity: require module "sale_order_validity"
    """,
    'author':  'fcoach66',
    'website': 'www.cocciari.com',
    'images': [
    ],
    'depends': [
        'report_extended_sale',
        'l10n_it_aeroo_base',
		'l10n_it_ddt',
		'sale_validity',
		'l10n_it_fiscalcode',
	],
    'data': [
        'report_configuration_defaults_data.xml',
        'sale_order_report.xml',
        'sale_order_template.xml',
    ],
    'demo': [
    ],
    'test': [
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: