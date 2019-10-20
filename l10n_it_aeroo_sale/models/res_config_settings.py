# © 2018 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/gpl).

from odoo import api, fields, models


class ResConfigSettingsWithAerooSaleOrderTemplate(models.TransientModel):

    _inherit = 'res.config.settings'

    aeroo_sale_order_template_id = fields.Many2one(
        'ir.actions.report', 'Aeroo Sale Order Report',
        domain="[('report_type', '=', 'aeroo'), ('model', '=', 'sale.order')]")

    @api.model
    def get_values(self):
        res = super().get_values()
        template = self.env.ref(
            'l10n_it_aeroo_sale.aeroo_invoice_report', raise_if_not_found=False)
        res['aeroo_sale_order_template_id'] = template.id if template else False
        return res

    @api.model
    def set_values(self):
        super().set_values()
        if self.aeroo_sale_order_template_id:
            self._update_aeroo_sale_order_template()
        else:
            self._empty_aeroo_sale_order_template()

    def _update_aeroo_sale_order_template(self):
        ref = self.env['ir.model.data'].search([
            ('module', '=', 'l10n_it_aeroo_sale'),
            ('name', '=', 'aeroo_invoice_report'),
        ], limit=1)

        if ref:
            ref.res_id = self.aeroo_sale_order_template_id.id
        else:
            self.env['ir.model.data'].create({
                'module': 'l10n_it_aeroo_sale',
                'name': 'aeroo_invoice_report',
                'model': 'ir.actions.report',
                'res_id': self.aeroo_sale_order_template_id.id,
                'noupdate': True,
            })

    def _empty_aeroo_sale_order_template(self):
        self.env['ir.model.data'].search([
            ('module', '=', 'l10n_it_aeroo_sale'),
            ('name', '=', 'aeroo_invoice_report'),
        ]).unlink()
