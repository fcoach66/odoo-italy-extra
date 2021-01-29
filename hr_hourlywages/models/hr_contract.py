# -*- coding: utf-8 -*-
from odoo import models, fields
import odoo.addons.decimal_precision as dp

class HrContract(models.Model):
    _inherit = 'hr.contract'

    hourlywage = fields.Float('Hourly Wage', digits=dp.get_precision('Hourly Wage'), required=True, track_visibility="onchange", help="Employee's Hourly wage.", default= 0)
