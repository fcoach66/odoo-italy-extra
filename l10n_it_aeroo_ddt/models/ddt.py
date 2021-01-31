# © 2018 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/gpl).

from odoo import models


class DdtWithAerooReport(models.Model):

    _inherit = 'stock.picking.package.preparation'

    def action_send_ddt_mail(self):
        """Print the ddt using the aeroo invoice template if it is defined.

        If the aeroo ddt report is not setup, fallback to the qweb template.
        """
        report = self.env.ref('l10n_it_aeroo_ddt.aeroo_it_ddt_report_pdf', raise_if_not_found=False)
        if report:
            return report.report_action(self)
        else:
            return super().action_send_ddt_mail()

    def action_print_ddt_aeroo_pdf(self):
        report = self.env.ref('l10n_it_aeroo_ddt.aeroo_it_ddt_report_pdf', raise_if_not_found=False)
        if report:
            return report.report_action(self)
        else:
            return super().action_send_ddt_mail()

    def action_print_ddt_aeroo_odt(self):
        report = self.env.ref('l10n_it_aeroo_ddt.aeroo_it_ddt_report_odt', raise_if_not_found=False)
        if report:
            return report.report_action(self)
        else:
            return super().action_send_ddt_mail()
