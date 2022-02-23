from odoo import fields, models


class ResUsers(models.Model):
    _inherit = 'res.users'

    signature_text = fields.Text('Signature Text')