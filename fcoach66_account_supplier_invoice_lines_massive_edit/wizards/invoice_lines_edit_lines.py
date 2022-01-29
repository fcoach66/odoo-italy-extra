###############################################################################
# For copyright and license notices, see __manifest__.py file in root directory
###############################################################################
from odoo import fields, models


class InvoiceSupplierLinesEditLines(models.TransientModel):
    _name = 'invoice.supplier.lines.edit.lines'
    _description = 'Invoice Supplier lines edit, lines'

    wizard_id = fields.Many2one(
        comodel_name='invoice.supplier.lines.edit',
        string='Wizard',
    )
    line_id = fields.Many2one(
        comodel_name='account.invoice.line',
        string='Invoice line',
    )
    product_id = fields.Many2one(
        comodel_name='product.product',
        string='Product',
    )
    account_analytic_id = fields.Many2one(
        comodel_name='account.analytic.account',
        string='Analytic Account',
    )
    quantity = fields.Float()
    price_unit = fields.Float()
    discount = fields.Float()
