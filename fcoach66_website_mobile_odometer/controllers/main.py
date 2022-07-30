# -*- coding: utf-8 -*-

from odoo import http, _
from odoo.http import request
from datetime import datetime, date, timedelta
from odoo.addons.website.controllers.main import QueryURL
from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo.addons.portal.controllers.portal import CustomerPortal
from dateutil.relativedelta import relativedelta
import time
from odoo.tools import groupby as groupbyelem
from operator import itemgetter


class AddOdometer(http.Controller):

    @http.route(['/my/add_new_odometer'], type='http', auth="user", website=True)
    def add_new_odometer(self, page=1, **kwargs):
        
        partner = request.env.user.partner_id
        return request.render("fcoach66_website_mobile_odometer.fcoach66_new_odometer_form")

    @http.route(['/my/new_odometer_submit'], type='http', auth="user", website=True)
    def submit_new_odometer(self, **post):
        
        if post:
            vehicle = post['vehicle']
            date = post['date']
            chilometers = post['chilometers']


            odometer_obj = request.env['fleet.vehicle.odometer']
            fleet_vehicle_assignation_log_obj = request.env['fleet.vehicle.assignation.log']
            vehicle_obj = request.env['fleet.vehicle'].sudo().browse(int(vehicle))

            chilometers_replace = chilometers.replace(':', '.') 

            odometer_obj = odometer_obj.sudo().create({
                'date':date,
#                'driver_id': request.env.user.partner_id.id,
                'vehicle_id': vehicle_obj.id,
                'value': float(chilometers_replace),
            })
            
            fleet_vehicle_assignation_log_obj = fleet_vehicle_assignation_log_obj.sudo().create({
                'vehicle_id': vehicle_obj.id,
                'driver_id': request.env.user.partner_id.id,
                'date_start': date,
                'date_end': date,
            })

#            return request.redirect("/my/add_new_odometer")
            return request.render("fcoach66_website_mobile_odometer.odometer_added")
        else:
            request.render("fcoach66_website_mobile_odometer.odometer_failed")

