# -*- coding: utf-8 -*-

{
    "name" : "Mobile Vehicle Odometer Line Insert",
    "version" : "12.0.1.0",
    "category" : "Website",
    "depends" : ['base','website','portal','fleet','fleet_vehicle_history_date_end'],
    "author": "fcoach66",
    'summary': 'mobile view for vehicle odometer',
    "description": """
    """,
    "data": [
        'views/website_add_new_odometer.xml',
        'views/website_mobile_odometer.xml',
    ],
    'qweb': [
    ],
    "auto_install": False,
    "installable": True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
