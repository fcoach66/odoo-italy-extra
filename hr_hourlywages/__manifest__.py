# -*- coding: utf-8 -*-

{
    'name': 'Hourly Wages',
    'description': 'Pay Hourly Salary using Hourly wage field on the contact.',
    'version': '12.0.1.0',
    'website': 'https://github.com/fcoach66/odoo-italy-extra',
    'author': 'fcoach66',
    'license': 'AGPL-3',
    'category': 'Human Resources',
    'data': [
        'views/hr_contract_view.xml',
    ],
    'depends': [
        'hr_contract',
        'hr_payroll',
    ],
}
