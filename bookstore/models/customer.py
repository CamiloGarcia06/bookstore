from odoo import models, fields


class Customer(models.Model):
    _name = 'bookstore.customer'
    _description = 'Customer'

    name = fields.Char(required=True)
    contact_details = fields.Char()
    customer_since = fields.Date()
    sale_history_ids = fields.One2many(
        'sale.order.line', 'customer_id', string="Purchase History"
    )
