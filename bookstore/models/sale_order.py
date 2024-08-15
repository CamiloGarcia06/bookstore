from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        for line in self.order_line:
            line.book_id._update_stock(line.product_uom_qty, decrease=True)
        return res


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    book_id = fields.Many2one('bookstore.book', string="Book", required=True)
    customer_id = fields.Many2one(
        'bookstore.customer', string="Customer", required=True)

    @api.onchange('product_uom_qty')
    def _onchange_product_uom_qty(self):
        if self.product_uom_qty and self.book_id:
            available_stock = self.book_id.quantity_in_stock
            if self.product_uom_qty > available_stock:
                warning = {
                    'title': "Insufficient Stock",
                    'message': "The quantity ordered exceeds the available stock."
                }
                return {'warning': warning}
