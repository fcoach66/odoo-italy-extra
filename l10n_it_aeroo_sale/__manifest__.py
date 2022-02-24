# -*- coding: utf-8 -*-
{
    'name': 'Italian Sale Order Aeroo Report',
    'version': '12.0.1.0',
    'category': 'Generic Modules/Aeroo Reports',
    'summary': '',
    'description': """
Italian Sale Order / Quotation Aeroo Report
    """,
    'author':  'fcoach66',
    'website': 'www.cocciari.com',
    'images': [
    ],
    'depends': [
        'report_aeroo',
		'l10n_it_fiscalcode',
		'sale_additional_text_template',
        'sale_mandatory_fields',
        'fcoach66_res_users_signature_text',
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