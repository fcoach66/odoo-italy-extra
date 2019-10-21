# © 2018 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/gpl).

from odoo import models


class SaleOrderWithAerooReport(models.Model):

    _inherit = 'sale.order'

    def print_quotation(self):
        """Print the sale order using the aeroo invoice template if it is defined.

        If the aeroo sale order report is not setup, fallback to the qweb template.
        """
        report = self.env.ref('l10n_it_aeroo_sale.aeroo_it_sale_order_report_pdf', raise_if_not_found=False)
        if report:
            return report.report_action(self)
        else:
            return super().print_quotation()
