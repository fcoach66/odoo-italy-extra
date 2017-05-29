# -*- coding: utf-8 -*-
#
#  File: __init__.py
#  Module: l10n_it_hr_payroll
#
##############################################################################

{
    'name': 'Italy - Payroll',
    'category': 'Localization',
    'author': 'fcoach66',
    'depends': ['decimal_precision','hr_payroll', 'hr_payroll_account'],
    'version': '1.0.0',
    'description': """
Italy Payroll Rules.
=========================
    """,

    'auto_install': False,
    'demo': [],
    'website': '',
    'data': [
        'hr_contract_view.xml',
        'hr_employee_view.xml',
        'l10n_it_hr_payroll_data.xml',
        'data/hr.salary.rule-change.csv',
        'data/hr.salary.rule-new.csv',
    ],
    'installable': True
}
