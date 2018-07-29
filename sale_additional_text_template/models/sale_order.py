# -*- coding: utf-8 -*-
from odoo import models, fields


class SaleOrder(models.Model):

	_inherit = "sale.order"
	_columns = {
		'additional_text_template1_id': fields.Many2one(
			'sale.additional_text.template',
			'Subject'),
		'additional_text_template2_id': fields.Many2one(
			'sale.additional_text.template',
			'Description'),
		'additional_text_template3_id': fields.Many2one(
			'sale.additional_text.template',
			'Limitation'),
		
		'additional_text_1': fields.text('Subject'),
		'additional_text_2': fields.text('Description'),
		'additional_text_3': fields.text('Limitation'),
		
	}

	
	def set_additional_text(self, cr, uid, cond_id, field_name, partner_id):
		if not cond_id:
			return {'value': {field_name: ''}}
		cond_obj = self.pool['sale.additional_text.template']
		text = cond_obj.get_value(cr, uid, cond_id, partner_id)
		return {'value': {field_name: text}}

	def set_additional_text_1(self, cr, uid, so_id, cond_id, partner_id):
		return self.set_additional_text(cr, uid, cond_id, 'additional_text_1', partner_id)

	def set_additional_text_2(self, cr, uid, so_id, cond_id, partner_id):
		return self.set_additional_text(cr, uid, cond_id, 'additional_text_2', partner_id)

	def set_additional_text_3(self, cr, uid, so_id, cond_id, partner_id):
		return self.set_additional_text(cr, uid, cond_id, 'additional_text_3', partner_id)

