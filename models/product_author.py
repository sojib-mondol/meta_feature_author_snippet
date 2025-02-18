from odoo import models, fields

class ProductAuthor(models.Model):
    _inherit = 'product.author'

    feature = fields.Boolean(string='isFeatured', default=False, help='Check if this author has featured status')
