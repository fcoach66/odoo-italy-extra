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
		'sale_quotation_builder',
        'report_aeroo',
		'l10n_it_fiscalcode',
		'sale_additional_text_template',
        'sale_mandatory_fields',
		'sale_ux',
		'
	],
    'data': [
        'report/sale_order_report.xml',
        'views/res_config_settings.xml',
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