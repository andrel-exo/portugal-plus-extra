# Copyright 2019 Exo Software Lda.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.onchange('operating_unit_id')
    def _onchange_operating_unit(self):
        # Note that super doesn't have an _ prefix so we don't need
        # to call it
        # super(SaleOrder, self).onchange_operating_unit()
        if self.source_billing:
            domain = self._pt_get_fiscal_doc_domain(self.source_billing)
            fiscal_doc = self._pt_get_fiscal_doc_selection(
                domain, limit=1)
            if fiscal_doc:
                self.fiscal_document_type_id = fiscal_doc

    def _pt_get_fiscal_doc_domain(self, source_billing, vals=None):
        # Initialize on super
        domain = super()._pt_get_fiscal_doc_domain(
            source_billing, vals)

        # add operating unit filter to domain
        if 'operating_unit_id' in self._fields:
            operating_unit_id = vals and vals.get('operating_unit_id', False) \
                                or self.operating_unit_id.id

            domain.extend([
                ('operating_unit_id', 'in', (False, operating_unit_id)),
            ])
        return domain
