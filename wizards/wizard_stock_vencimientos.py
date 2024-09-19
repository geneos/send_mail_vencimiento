from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class WizardStockVencimiento(models.TransientModel):
    _name = "stock.production.vencimientos_lotes"
    _description = "Wizard Stock Vencimientos"


    def print_report(self):
        return self.env.ref(
            "send_mail_vencimiento.action_report_product").report_action(self)
