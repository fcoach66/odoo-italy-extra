# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class StockDdT(models.Model):
        _inherit = 'stock.picking.package.preparation'
        _description = 'DdT'

        def print_ddt(self, cr, uid, ids, context=None):
                assert len(ids) == 1, 'This option should only be used for a single id at a time'
		return self.env.ref('l10n_it_aeroo_ddt.action_aeroo_report_it_ddt').report_action(self)

