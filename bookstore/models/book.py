from odoo import models, fields
from odoo.exceptions import ValidationError


class BookstoreBook(models.Model):
    _name = 'bookstore.book'
    _description = 'Book'

    title = fields.Char('Title', required=True)
    author_id = fields.Many2one(
        'bookstore.author', 'Author', required=True)
    published_date = fields.Date('Published Date')
    isbn = fields.Char('ISBN')
    price = fields.Float('Price')
    quantity_in_stock = fields.Integer('Quantity in Stock')
    sale_order_line_ids = fields.One2many(
        'sale.order.line', 'book_id', string="Related Sale Orders"
    )

    def _update_stock(self, quantity, decrease=False):
        """ Update the stock levels for the book """
        if decrease:
            self.quantity_in_stock -= quantity
        else:
            self.quantity_in_stock += quantity

        # Ensure the stock level is never negative
        if self.quantity_in_stock < 0:
            raise ValidationError('Stock level cannot be negative!')
