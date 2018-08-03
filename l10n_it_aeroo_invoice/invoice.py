# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from odoo import models, fields, api, _
#from openerp.exceptions import except_orm, Warning, RedirectWarning
#from openerp.tools import float_compare

class account_invoice(models.Model):
    _inherit = ['account.invoice']
    _description = "Invoice"

    @api.multi
    def invoice_print_aeroo_pdf(self):
        """ Print the invoice and mark it as sent, so that we can see more
            easily the next step of the workflow
        """
        assert len(self) == 1, 'This option should only be used for a single id at a time.'
        self.sent = True
        return self.env['report'].get_action(self, 'account.aeroo_report_it_invoice_pdf')

#    @api.multi
#    def action_invoice_sent(self):
#        """ Open a window to compose an email, with the edi invoice template
#            message loaded by default
#        """
#        assert len(self) == 1, 'This option should only be used for a single id at a time.'
#        template = self.env.ref('account.email_template_edi_invoice_aeroo', False)
#        compose_form = self.env.ref('mail.email_compose_message_wizard_form', False)
#        ctx = dict(
#            default_model='account.invoice',
#            default_res_id=self.id,
#            default_use_template=bool(template),
#            default_template_id=template.id,
#            default_composition_mode='comment',
#            mark_invoice_as_sent=True,
#        )
#        return {
#            'name': _('Compose Email'),
#            'type': 'ir.actions.act_window',
#            'view_type': 'form',
#            'view_mode': 'form',
#            'res_model': 'mail.compose.message',
#            'views': [(compose_form.id, 'form')],
#            'view_id': compose_form.id,
#            'target': 'new',
#            'context': ctx,
#        }
