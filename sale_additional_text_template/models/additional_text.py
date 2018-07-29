# -*- coding: utf-8 -*-
#
#
#
from odoo import fields, models, api


class SaleAdditionalTextTemplate(models.Model):
    _name = "sale.additional_text.template"
    _description = "Sale Additional Text template"
	@api.multi
    name = fields.Char('Additional text name', required=True)
    type = fields.Selection([('subject', 'Subject'),('description', 'Description'),('limitation', 'Limitation')],'Type',required=True,default='subject',help="Type of additional text")
    text = fields.Text('Text', translate=True, required=True)

    @api.multi
    def get_value(self, partner_id=False):
        self.ensure_one()
        lang = None
        if partner_id:
            lang = self.env['res.partner'].browse(partner_id).lang
        return self.with_context({'lang': lang}).text
