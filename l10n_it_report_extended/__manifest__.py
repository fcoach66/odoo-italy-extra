# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2015  ADHOC SA  (http://www.adhoc.com.ar)
#    All Rights Reserved.
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
{
    'name': 'Report Configurator for italian reports',
    'version': '11.0.1.0.0',
    'category': 'Reporting Subsystem',
    'sequence': 14,
    'summary': '',
    'description': """
Report Configurator
===================
This module allows users to define reports for different
objects such as invoice or sale order.
It creates the menu to the configuration objects in:
    Configuration / Personalization / Aeroo Reports / Report Configuration

The parser proved a serie of fields an functions to use in the odt:
    
    o report_configuration: The associated report configuration object.
    o company: The company object.
    o logo: If not False it contains the logo of the company.
    o use_background_image: Boolean indicating if the background image should
      be used or not.
    o background_image: The background image to be used.
    o format_vat: Function that takes a string an format is as a vat.
    o address_from_partner: Return the default address from a partner object,
      or False.
    o minus: Given 2 values x1 and x2 returns x1 - x2.
    o number_to_string: Takes a string of a quantity and returns the textual
      representation of the quantity.
    o net_price: Takes a gross quantity and a discount and return the gross
      applying the discount.
    """,
    'author':  'ADHOC SA, fcoach66',
    'website': '',
    'license': 'AGPL-3',
    'images': [
    ],
    'depends': [
        'base',
		'report_aeroo',
    ],
    'data': [
       'views/company_view.xml',
        'views/ir_actions_report_views.xml',
        'views/report_configuration_default_views.xml',
        'views/report_configuration_line_views.xml',
        'security/report_extended_security.xml',
        'security/ir.model.access.csv',    ],
    'demo': [
    ],
    'test': [
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
