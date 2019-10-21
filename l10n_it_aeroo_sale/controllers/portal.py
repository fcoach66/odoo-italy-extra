# © 2018 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/gpl).

from odoo import http
from odoo.addons.account.controllers.portal import PortalAccount
from odoo.exceptions import AccessError, MissingError
from odoo.http import request

AEROO_SALE_ORDER_REPORT_REF = 'l10n_it_aeroo_sale.aeroo_it_sale_order_report_pdf'


class PortalAccountWithAerooSaleOrderReport(PortalAccount):

    @http.route(['/my/orders/<int:order_id>'], type='http', auth="public", website=True)
    def portal_my_orders(
        self, order_id, access_token=None, report_type=None, download=False, **kw
    ):
        template = request.env.ref(AEROO_SALE_ORDER_REPORT_REF, raise_if_not_found=False)

        if not template or report_type != 'pdf':
            return super().portal_my_orders(
                order_id, access_token=access_token, report_type=report_type,
                download=download, **kw)

        try:
            sale_order = self._document_check_access('sale.order', order_id, access_token)
        except (AccessError, MissingError):
            return request.redirect('/my')

        return self._show_aeroo_report(record=sale_order, template=template, download=download)
