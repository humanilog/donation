# -*- coding: utf-8 -*-
# © 2017 Stefan Becker <s.becker@humanilog.org>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models, _


class ResCompany(models.Model):
    _inherit = 'res.company'

    responsible_tax_authority = fields.Char(
        string=_('Responsible Tax Authority'))
    current_certificate_of_tax_exemption = fields.Date(
        string=_('current certificate of tax exemption'))
    last_assessment_period = fields.Char(
        string=_('Last assessment period'))
