###############################################################################
# For copyright and license notices, see __manifest__.py file in root directory
###############################################################################
from odoo import api, fields, models


class InvoiceSupplierLinesEdit(models.TransientModel):
    _name = 'invoice.supplier.lines.edit'
    _description = 'Invoice Supplier lines edit'

    line_ids = fields.One2many(
        comodel_name='invoice.supplier.lines.edit.lines',
        inverse_name='wizard_id',
        string='Lines',
    )

    @api.multi
    def button_accept(self):
        for line in self.line_ids:
            line.line_id.write({
                'product_id': line.product_id.id,
                'account_analytic_id': line.account_analytic_id.id,
                'quantity': line.quantity,
                'price_unit': line.price_unit,
                'discount': line.discount})
