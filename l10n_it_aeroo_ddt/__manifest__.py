# -*- coding: utf-8 -*-
{
    'name': 'Italian Ddt Aeroo Report',
    'version': '12.0.1.0',
    'category': 'Generic Modules/Aeroo Reports',
    'summary': '',
    'description': """
Italian Ddt Aeroo Report
    """,
    'author':  'fcoach66',
    'website': 'www.cocciari.com',
    'images': [
    ],
    'depends': [
        'report_aeroo',
		'l10n_it_ddt',
	],
    'data': [
		'report/ddt_report.xml',
        'views/res_config_settings.xml',
        'views/l10n_it_aeroo_ddt_views.xml',
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
