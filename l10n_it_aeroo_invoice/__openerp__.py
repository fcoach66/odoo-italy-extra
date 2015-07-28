# -*- coding: utf-8 -*-
{
    'name': 'Italian Invoice Aeroo Report',
    'version': '1.0',
    'category': 'Localization/Italy',
    'sequence': 14,
    'summary': '',
    'description': """
Italian Invoice Aeroo Report
    """,
    'author':  'fcoach66',
    'website': 'www.cocciari.com',
    'images': [
    ],
    'depends': [
		'account',
		'portal_sale',
        'l10n_it_aeroo_base',
		'l10n_it_fiscalcode',
	],
    'data': [
        'invoice_report.xml',
		'invoice_template.xml',
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