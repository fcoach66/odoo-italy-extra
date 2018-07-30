from datetime import datetime, timedelta
import time
from openerp import models, fields
from openerp.tools.translate import _
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT
import openerp.addons.decimal_precision as dp
from openerp import workflow


class sale_order(models.Model):
    _inherit = 'sale.order'
    _description = 'Sale Order'


    def print_quotation(self, cr, uid, ids, context=None):
        '''
            This function prints the sales order and mark it as sent, so that we can see more easily the next step of the workflow
            '''
        assert len(ids) == 1, 'This option should only be used for a single id at a time'
        return self.pool['report'].get_action(cr, uid, ids, 'sale.report_saleorder_aeroo', context=context)

    def print_quotation_pdf(self, cr, uid, ids, context=None):
        '''
            This function prints the sales order and mark it as sent, so that we can see more easily the next step of the workflow
            '''
        assert len(ids) == 1, 'This option should only be used for a single id at a time'
        return self.pool['report'].get_action(cr, uid, ids, 'sale.report_saleorder_aeroo_pdf', context=context)
		
	
    def action_quotation_send(self, cr, uid, ids, context=None):
        '''
            This function opens a window to compose an email, with the edi sale template message loaded by default
            '''
        assert len(ids) == 1, 'This option should only be used for a single id at a time.'
        ir_model_data = self.pool.get('ir.model.data')
        try:
            template_id = ir_model_data.get_object_reference(cr, uid, 'sale', 'email_template_edi_sale_aeroo')[1]
        except ValueError:
            template_id = False
        try:
            compose_form_id = ir_model_data.get_object_reference(cr, uid, 'mail', 'email_compose_message_wizard_form')[1]
        except ValueError:
            compose_form_id = False
        ctx = dict()
        ctx.update({
            'default_model': 'sale.order',
            'default_res_id': ids[0],
            'default_use_template': bool(template_id),
            'default_template_id': template_id,
            'default_composition_mode': 'comment',
            'mark_so_as_sent': True
        })
        return {
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'views': [(compose_form_id, 'form')],
            'view_id': compose_form_id,
            'target': 'new',
            'context': ctx,
        }
