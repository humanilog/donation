# -*- coding: utf-8 -*-

from functools import partial

from num2words import num2words

from openerp import api, models


class ReportDonationTaxReceipt(models.AbstractModel):
    _name = 'report.donation_base.report_donationtaxreceipt'

    @api.multi
    def render_html(self, docids, data=None):
        report_obj = self.env['report']
        report_name = '.'.join(self._name.split('.')[1:])
        docargs = {
            'doc_ids': docids,
            'doc_model': 'donation.tax.receipt',
            'docs': self.env['donation.tax.receipt'].browse(docids),
            'num2words_de': partial(num2words, lang='de')
        }
        return report_obj.render(report_name, docargs)
