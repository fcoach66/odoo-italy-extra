# -*- coding: utf-8 -*-
#
from odoo import models, fields


class SaleOrder(models.Model):

        _inherit = "sale.order"
        additional_text_template1_id = fields.Many2one('sale.additional_text.template', String='Subject')
        additional_text_template2_id = fields.Many2one('sale.additional_text.template', String='Description')
        additional_text_template3_id = fields.Many2one('sale.additional_text.template', String='Limitation')
        additional_text_1 = fields.Text('Subject')
        additional_text_2 = fields.Text('Description')
        additional_text_3 = fields.Text('Limitation')


        def set_additional_text(self, cond_id, field_name, partner_id):
                if not cond_id:
                        return {'value': {field_name: ''}}
                cond_obj = self.env['sale.additional_text.template']
                text = cond_obj.get_value(cond_id, partner_id)
                return {'value': {field_name: text}}

        def set_additional_text_1(self, so_id, cond_id, partner_id):
                return self.set_additional_text(cond_id, 'additional_text_1', partner_id)

        def set_additional_text_2(self, so_id, cond_id, partner_id):
                return self.set_additional_text(cond_id, 'additional_text_2', partner_id)

        def set_additional_text_3(self, so_id, cond_id, partner_id):
                return self.set_additional_text(cond_id, 'additional_text_3', partner_id)