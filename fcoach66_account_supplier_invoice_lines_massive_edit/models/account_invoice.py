###############################################################################
# For copyright and license notices, see __manifest__.py file in root directory
###############################################################################
from odoo import api, models


class AccountInvoiceSupplier(models.Model):
    _inherit = 'account.invoice'

    @api.multi
    def action_lines_massive_edit(self):
        self.ensure_one()
        wiz = self.env['invoice.supplier.lines.edit'].create({})
        for line in self[0].invoice_line_ids:
            self.env['invoice.supplier.lines.edit.lines'].create({
                'wizard_id': wiz.id,
                'line_id': line.id,
                'product_id': line.product_id.id,
                'account_analytic_id': line.account_analytic_id.id,
                'quantity': line.quantity,
                'price_unit': line.price_unit,
                'discount': line.discount})
        view = self.env.ref(
            'fcoach66_account_supplier_invoice_lines_massive_edit.wiz_invoice_supplier_lines_edit')
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'invoice.supplier.lines.edit',
            'res_id': wiz.id,
            'view_id': view.id,
            'view_mode': 'form',
            'view_type': 'form',
            'target': 'new',
        }
