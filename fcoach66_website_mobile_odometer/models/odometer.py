# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api, _

from odoo.addons.fleet.models.fleet_vehicle import FleetVehicle as OriginalFleetVehicle

def write(self, vals):
    res = super(OriginalFleetVehicle, self).write(vals)
    if 'active' in vals and not vals['active']:
        self.mapped('log_contracts').write({'active': False})
    return res

OriginalFleetVehicle.write = write


class Website(models.Model):
    _inherit = 'website'

    def get_vehicle_details(self):

        vehicle_details = self.env['fleet.vehicle'].sudo().search([])
        vehicle_ids = self.env['fleet.vehicle'].sudo().search([])
        partner = self.env['res.partner'].browse(self.env['res.users'].browse(self.env['res.users']._context['uid']).partner_id.id)
        vehicles = []
        for i in vehicle_ids:
            # if partner in i.message_partner_ids :
            vehicles.append(i)
        return vehicles

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

