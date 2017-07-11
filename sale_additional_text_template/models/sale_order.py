# -*- coding: utf-8 -*-
#
from odoo import models, fields, api


class SaleOrder(models.Model):

        _inherit = "sale.order"
        additional_text_template1_id = fields.Many2one('sale.additional_text.template', String='Subject')
        additional_text_template2_id = fields.Many2one('sale.additional_text.template', String='Description')
        additional_text_template3_id = fields.Many2one('sale.additional_text.template', String='Limitation')
        additional_text_1 = fields.Text('Subject')
        additional_text_2 = fields.Text('Description')
        additional_text_3 = fields.Text('Limitation')


        @api.onchange('additional_text_template1_id')
        def _set_additional_text_1(self):
            additional_text = self.additional_text_template1_id
            if additional_text:
                self.additional_text_1 = additional_text.get_value(self.partner_id.id)

        @api.onchange('additional_text_template2_id')
        def _set_additional_text_2(self):
            additional_text = self.additional_text_template2_id
            if additional_text:
                self.additional_text_2 = additional_text.get_value(self.partner_id.id)

        @api.onchange('additional_text_template3_id')
        def _set_additional_text_3(self):
            additional_text = self.additiona3_text_template1_id
            if additional_text:
                self.additional_text_3 = additional_text.get_value(self.partner_id.id)
				