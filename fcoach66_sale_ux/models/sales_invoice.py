# -*- coding : utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class SaleOrderUpdateInvoicedOnTree(models.Model):
	_inherit = 'sale.order'

	invoiced_amount_tree = fields.Float(String = 'Invoiced Amount' ,compute ='_computetotaltree')

	
	@api.one
	def _computetotaltree(self):
		invoice_id = self.env['account.invoice'].search(['&',('origin','=', self.name),'|',('state','=','open'),('state','=','paid')])
		total = 0
		for comp in invoice_id:
			total += comp.amount_total
		self.invoiced_amount_tree = total

				
