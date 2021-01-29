# -*- coding: utf-8 -*-
from odoo import models, fields


class HrContract(models.Model):
    _inherit = 'hr.contract'

    hourlywage = fields.Monetary('Hourly Wage', digits=(16, 2), required=True, track_visibility="onchange", help="Employee's Hourly wage.", default= 0)
