from odoo import models, fields, api, _
import logging
from datetime import date

_logger = logging.getLogger(__name__)


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def _update_supplier_price(self, line):
        try:
            product = line.product_id
            supplier = self.partner_id

            if not product or not supplier:
                _logger.warning(f"Skip update: Product or supplier is empty (Product: {product}, Supplier: {supplier})")
                return

            domain = [
                ('product_tmpl_id', '=', product.product_tmpl_id.id),
                ('partner_id', '=', supplier.id)
            ]

            supplier_info = self.env['product.supplierinfo'].search(domain, limit=1)
            seller_price = line.price_unit

            update_vals = {
                'price': seller_price,
                'currency_id': line.currency_id.id,
            }

            if supplier_info:
                supplier_info.write(update_vals)
                _logger.info(
                    f"Update supplier price: Product {product.display_name} - Supplier {supplier.name} - Price {seller_price}")
            else:
                _logger.info(
                    f"Skip creation: Product {product.display_name} - Supplier {supplier.name} has no supplier info, do not create new record")

        except Exception as e:
            _logger.error(f"Failed to update supplier price: {str(e)}", exc_info=True)

    def button_confirm(self):
        result = super(PurchaseOrder, self).button_confirm()

        for order in self:
            for line in order.order_line:
                if (line.product_id and
                        line.product_id.type in ['product', 'consu'] and
                        line.price_unit > 0):
                    self._update_supplier_price(line)

        return result