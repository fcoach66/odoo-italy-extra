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
	    	'report_extended_account',
		'l10n_it_aeroo_base',
		'l10n_it_fiscalcode',
        'l10n_it_rea',
        'l10n_it_pec',
	],
    'data': [
        'invoice_report.xml',
        'report_configuration_defaults_data.xml',
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
