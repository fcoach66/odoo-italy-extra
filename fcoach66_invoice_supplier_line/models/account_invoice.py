
from odoo import api, fields, models


class AccountInvoiceSupplier(models.Model):
    _inherit = "account.invoice"

    def button_invoice_supplier_show_lines(self):
        action = self.env.ref("fcoach66_invoice_supplier_line.action_invoice_supplier_line").read()[0]
        action["domain"] = [("invoice_id", "=", self.id)]
        action["context"] = {"active_id": self.id, "active_model": self._name}
        return action


class AccountInvoiceSupplierLine(models.Model):
    _inherit = "account.invoice.line"

    checked = fields.Selection([("ok", "OK"), ("not_ok", "NOT OK")], string="Checked")

    @api.multi
    def set_checked(self, value):
        self.write({"checked": value})

#    @api.multi
#    def compute_taxes(self):
#        invoices = self.env["account.invoice"]
#        for line in self:
#            invoices |= line.invoice_id
#
#        invoices.compute_taxes()
