# -*- coding: utf-8 -*-

from functools import partial

from num2words import num2words

from openerp import api, models


class ReportDonationTaxReceipt(models.AbstractModel):
    _name = 'report.donation_base.report_donationtaxreceipt'

    @api.multi
    def render_html(self, data=None):
        report_obj = self.env['report']
        report_name = '.'.join(self._name.split('.')[1:])
        report = report_obj._get_report_from_name(report_name)
        docargs = {
            'doc_ids': self._ids,
            'doc_model': report.model,
            'docs': self.env['donation.tax.receipt'].browse(self._ids),
            'num2words_de': partial(num2words, lang='de')
        }
        return report_obj.render(report_name, docargs)
