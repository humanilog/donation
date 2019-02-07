# -*- coding: utf-8 -*-
# © 2017 Ben Brich <b.brich@humanilog.org>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models, _

class NonprofitPurpose(models.Model):
    _name = 'nonprofit.purpose'
    _description = 'Code for recognized non-profit purposes in Germany'
    _order = 'code'

    code = fields.Char(string='Code', size=2)
    name = fields.Char(string='Name', required=True)
    full_name = fields.Char(string='Full Name')   