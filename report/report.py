# -*- coding: utf-8 -*-

from odoo import api, models, fields, _
from datetime import datetime, timedelta, date


class product_static(models.AbstractModel):
    _name = "report.send_mail_vencimiento.report_product"

    @api.model
    def _get_report_values(self, docids, data):
        today = datetime.today()
        tope = today + timedelta(days=30)
        tope = tope.strftime("%Y-%m-%d %H:%M:%S")
        product_ids = self.env['stock.production.lot'].search(
        [
            ('life_date', '<', tope),
        ], order="life_date asc")
        productos = []
        for item in product_ids:
            if item.product_qty != 0 and item.active:
                productos.append(item)

        return {
           'product': productos,
         }