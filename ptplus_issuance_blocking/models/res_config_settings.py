#############################################################################
#
#    Copyright (C) 2016 Exo Software, Lda. (<https://exosoftware.pt>)
#
#############################################################################
from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    l10n_pt_issuance_blocking = fields.Boolean(
        string="Doc. Issuance Blocking",
        related="company_id.l10n_pt_issuance_blocking",
        readonly=False,
    )

    l10n_pt_issuance_blocking_archived = fields.Boolean(
        string="Doc. Issuance Blocking (Archived)",
        related="company_id.l10n_pt_issuance_blocking_archived",
        readonly=False,
    )
