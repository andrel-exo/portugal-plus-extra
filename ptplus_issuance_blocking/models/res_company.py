##############################################################################
#
#    Copyright (C) 2016 Exo Software, Lda. (<https://exosoftware.pt>)
#
##############################################################################

from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    l10n_pt_issuance_blocking = fields.Boolean(
        string="Doc. Issuance Blocking",
        readonly=False,
    )

    l10n_pt_issuance_blocking_archived = fields.Boolean(
        string="Doc. Issuance Blocking (Archived)",
        readonly=False,
    )
