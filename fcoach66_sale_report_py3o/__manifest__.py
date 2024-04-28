{
    'name': 'Sale Reports Py3o',
    'version': '12.0.1.0.0',
    'category': 'Sales',
    'license': 'AGPL-3',
    'summary': 'py3o sale reports',
    'description': """
Sale Reports Py3o
=================

This module adds py3o sale reports.

    """,
    'author': 'fcoach66',
    'depends': [
        'report_py3o',
        'sale_commercial_partner',
        'base_company_extension',
        'base_usability',  # to have res_partner.name_title
        'sale_usability',  # for layout
        'account_payment_sale',
        ],
    'data': ['report.xml'],
    'installable': True,
}
