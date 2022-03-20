# -*- coding: utf-8 -*-

{
    'name': 'Update Timesheet Amount',
    'version': '1.0',
    'category': 'Human Resources',
    'sequence': 23,
    'summary': 'Update Timesheet Amount',
    'description': """
    """,
    'depends': ['hr_timesheet'],
    'data': [
        'views/hr_timesheet_view.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}