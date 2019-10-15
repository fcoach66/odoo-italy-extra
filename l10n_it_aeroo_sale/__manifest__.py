# -*- coding: utf-8 -*-
{
    'name': 'Italian Sale Order Aeroo Report',
    'version': '12.0.1.0',
    'category': 'Localization/Italy',
    'sequence': 14,
    'summary': '',
    'description': """
Italian Sale Order / Quotation Aeroo Report
    """,
    'author':  'fcoach66',
    'website': 'www.cocciari.com',
    'images': [
    ],
    'depends': [
        'l10n_it_aeroo_base',
		'website_quote',
		'l10n_it_fiscalcode',
		'sale_additional_text_template',
        'sale_mandatory_fields',
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
    'installable': False,
    'auto_install': False,
    'application': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: