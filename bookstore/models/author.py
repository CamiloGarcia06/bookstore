from odoo import models, fields


class Author(models.Model):
    _name = 'bookstore.author'
    _description = 'Author'

    name = fields.Char('Name', required=True)
    biography = fields.Text('Biography')
    book_ids = fields.One2many('bookstore.book', 'author_id', string='Books')
