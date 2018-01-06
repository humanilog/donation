# -*- coding: utf-8 -*-
# © 2017 Stefan Becker <s.becker@humanilog.org>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Donation DE",
    "summary": "Everything you need for managing donations in Germany",
    "version": "9.0.1.0.0",
    "category": "Donation Management",
    'website': 'http://www.humanilog.org',
    'author': 'Humanilog, '
              'Odoo Community Association (OCA)',
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "donation",
    ],
    "data": [
        'report/report.xml',
        'views/donation_views.xml'
    ],
}
