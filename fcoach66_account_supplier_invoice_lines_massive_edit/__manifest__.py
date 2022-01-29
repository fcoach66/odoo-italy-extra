###############################################################################
###############################################################################

{
    'name': 'Account Invoice Supplier Lines Massive Edit',
    'category': 'Account',
    'summary': 'Wizard for edit faster invoice supplier lines',
    'version': '12.0.1.0.0',
    'description': '',
    'author': 'fcoach66',
    'license': 'AGPL-3',
    'depends': [
        'account',
    ],
    'data': [
        'wizards/invoice_lines_edit_views.xml',
        'views/account_invoice_views.xml',
    ],
}
