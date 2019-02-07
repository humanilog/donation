# -*- coding: utf-8 -*-
# © 2017 Stefan Becker <s.becker@humanilog.org>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models, _


class ResCompany(models.Model):
    _inherit = 'res.company'

    responsible_tax_authority = fields.Char(
        string='Tax Authority')
    ao_check_date = fields.Date(
        string='Excemption criteria proofen')
    notice_of_exemption_received = fields.Boolean(
        string='Notice of exemption received')
    current_certificate_of_tax_exemption = fields.Date(
        string='Current certificate of tax exemption')
    last_assessment_period = fields.Char(
        string='Last assessment period')
    authorized_representative = fields.Many2one(
        'res.users', string='Authorized Representative')
    nonprofit_purpose_ids = fields.Many2many(
        comodel_name='nonprofit.purpose', string='Non-Profit Purposes')