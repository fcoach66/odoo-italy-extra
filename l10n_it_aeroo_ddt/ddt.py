# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class StockDdT(models.Model):
        _inherit = 'stock.picking.package.preparation'
        _description = 'DdT'

        @api.multi
        def print_ddt(self):
                return self.env.ref('l10n_it_aeroo_ddt.action_aeroo_report_it_ddt').report_action(self)

