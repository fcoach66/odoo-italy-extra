# -*- coding: utf-8 -*-
#
#
#
from openerp import models, fields, api


class SaleAdditionalTextTemplate(models.Model):
    _name = "sale.additional_text.template"
    _description = "Sale Additional Text template"

    name = fields.Char('Additional text name', required=True)
    type = fields.Selection([('subjext', 'Subject'),
                                 ('description', 'Description'),('limitation', 'Limitation')],
                                'Type',
                                required=True,
                                default='subject',
                                help="Type of additional text")
    text = fields.Text('Text', translate=True, required=True)

    @api.multi
    def get_value(self, partner_id=False):
        self.ensure_one()
        lang = None
        if partner_id:
            lang = self.env['res.partner'].browse(partner_id).lang
        return self.with_context({'lang': lang}).text
