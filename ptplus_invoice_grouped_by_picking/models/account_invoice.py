import logging

from odoo import api, models
from odoo.tools import float_compare

_logger = logging.getLogger(__name__)  # pylint: disable=C0103


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    @api.model
    def lines_grouped_contains_returns(self, lines_grouped):
        for gl in lines_grouped:
            precision = gl["line"].uom_id.rounding
            if gl["picking"]:
                if (
                    float_compare(
                        gl["quantity"],
                        gl["quantity_invoiced"],
                        precision_digits=precision,
                    )
                    != 0
                ):
                    return True
        return False

    def lines_grouped_by_picking(self):
        grouped_lines = super(AccountInvoice, self).lines_grouped_by_picking()
        for gl in grouped_lines:
            gl["quantity_invoiced"] = gl["quantity"]
            if gl["picking"]:
                # Compute the inverse (usually returned) quantity
                inverse_qty = 0.0
                for move in gl["picking"].move_lines:
                    if move.returned_move_ids:
                        inverse_qty = sum(
                            move.returned_move_ids.filtered(
                                lambda m: gl["line"] in m.invoice_line_ids
                            ).mapped("quantity_done")
                        )
                    elif move.origin_returned_move_id:
                        inverse_qty = sum(
                            move.origin_returned_move_id.filtered(
                                lambda m: gl["line"] in m.invoice_line_ids
                            ).mapped("quantity_done")
                        )
                    inverse_qty = min(inverse_qty, move.quantity_done)
                sign = gl["quantity"] / abs(gl["quantity"])
                gl["quantity_invoiced"] = gl["quantity"] - inverse_qty * sign

        return grouped_lines
