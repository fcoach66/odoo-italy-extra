# -*- coding: utf-8 -*-
{
    'name': 'Italian Invoice Aeroo Report',
    'version': '12.0.1.0',
    'category': 'Generic Modules/Aeroo Reports',
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
        'report_aeroo',
		'l10n_it_fiscalcode',
        'l10n_it_rea',
        'l10n_it_pec',
	],
    'data': [
        'report/invoice_report.xml',
        'views/res_config_settings.xml',
        'views/portal.xml',
    ],
    'demo': [
    ],
    'test': [
    ],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
