# -*- coding: utf-8 -*-
# © 2014-2016 Barroux Abbey (http://www.barroux.org)
# © 2014-2016 Akretion France (Alexis de Lattre <alexis.delattre@akretion.com>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, _


class ResCompany(models.Model):
    _inherit = 'res.company'

    donation_eligibility_purpose = fields.Char(
        string=_('Non-Profit Purpose'))
