from odoo import models


class AccountPaymentRegister(models.TransientModel):
    _inherit = "account.payment.register"

    def _create_payments(self):
        return super(
            AccountPaymentRegister, self.with_context(pt_allow_draft=True)
        )._create_payments()
