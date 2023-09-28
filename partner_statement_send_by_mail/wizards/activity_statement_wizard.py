from odoo import models
from odoo.tools.translate import _


class ActivityStatementWizard(models.TransientModel):
    _inherit = "activity.statement.wizard"

    def _send_mail(self):
        """Compose and send statement by e-mail."""
        self.ensure_one()
        template = self.env.ref(
            "partner_statement_send_by_mail."
            "email_template_partner_activity_statement",
            False,
        )
        compose_form = self.env.ref("mail.email_compose_message_wizard_form", False)
        ctx = dict(
            default_model="res.partner",
            default_res_id=self.env.context.get("active_id", False),
            default_use_template=bool(template),
            default_template_id=template.id,
            default_composition_mode="comment",
            custom_layout="mail.mail_notification_light",
            mark_coupon_as_sent=True,
            force_email=True,
            date_start=self.date_start,
            date_end=self.date_end,
        )
        return {
            "name": _("Compose Email"),
            "type": "ir.actions.act_window",
            "view_mode": "form",
            "res_model": "mail.compose.message",
            "views": [(compose_form.id, "form")],
            "view_id": compose_form.id,
            "target": "new",
            "context": ctx,
        }
