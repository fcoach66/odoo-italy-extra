
{
    "name": "Invoice Supplier Line",
    "version": "13.0.1.0.0",
    "author": "fcoach66",
    "website": "",
    "category": "Accounting",
    "depends": ["account"],
    "license": "LGPL-3",
    'depends': [
        'deltatech_invoice_line',
        'account_invoice_line_number',
        'account_analytic_default',
	],
    "data": ["views/account_invoice_view.xml"],
    "installable": False,
    "development_status": "stable",
    'installable': False,
    'application': False,
    'auto_install': False,
}
