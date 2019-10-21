# © 2018 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/gpl).

from odoo import models


class InvoiceWithAerooReport(models.Model):

    _inherit = 'account.invoice'

    def action_invoice_sent(self):
        """Print the invoice using the aeroo invoice template if it is defined.

        If the aeroo invoice report is not setup, fallback to the qweb template.
        """
        report = self.env.ref('l10n_it_aeroo_invoice.aeroo_it_invoice_report_pdf', raise_if_not_found=False)
        if report:
            return report.report_action(self)
        else:
            return super().action_invoice_sent()
