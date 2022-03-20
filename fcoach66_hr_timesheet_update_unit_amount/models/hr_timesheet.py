from odoo import api, fields, models, _
#from odoo.exceptions import UserError, ValidationError


class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    @api.multi
    def update_unit_amount(self):
        for timesheet in self:
            cost = timesheet.employee_id.timesheet_cost or 0.0
            amount = -timesheet.unit_amount * cost
            amount_converted = timesheet.employee_id.currency_id._convert(
                amount, timesheet.account_id.currency_id, self.env.user.company_id, timesheet.date)
            timesheet.update({
                'amount': amount_converted,
            })
