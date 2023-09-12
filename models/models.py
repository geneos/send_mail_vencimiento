# -*- coding: utf-8 -*-
import base64

from odoo import models, fields, api


class SendMailVencimiento(models.Model):
    _inherit = 'stock.production.lot'

    def send_email_with_attachment(self):
        report_template_id = self.env.ref(
            'send_mail_vencimiento.action_report_product').render_qweb_pdf(self.id)
        data_record = base64.b64encode(report_template_id[0])

        ir_values = {
            'name': "Informe_lotes_a_vencer",
            'type': 'binary',
            'datas': data_record,
            'store_fname': 'data_record',
            'mimetype': 'application/x-pdf',
        }
        data_id = self.env['ir.attachment'].sudo().create(ir_values)
        template = self.env.ref('send_mail_vencimiento.report_template')
        template.attachment_ids = [(6, 0, [data_id.id])]
        email_values = {'email_to': 'servitel01@gmail.com',
                        'email_from': 'info@geneos.com.ar',
                        'subject': 'Productos a vencer'}

        template.sudo().send_mail(self.id, email_values=email_values, force_send=True)

        template.attachment_ids = [(3, data_id.id)]
        return True
