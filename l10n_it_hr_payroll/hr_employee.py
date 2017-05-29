# -*- coding: utf-8 -*-
from openerp.osv import fields, osv
from openerp.tools.translate import _


class hr_employee(osv.osv):
    _inherit = 'hr.employee'
    _columns = {
        'children': fields.integer('Number of Children at school'),
        'children_student': fields.integer('Number of Children student'),
        }

hr_employee()
