import logging
from odoo import http
from odoo.http import request
from odoo.addons.http_routing.models.ir_http import slug # type: ignore

_logger = logging.getLogger(__name__)


class AuthorController(http.Controller):

    @http.route('/featured_authors', type='json', auth='public', website=True)
    def get_featured_authors(self):
        try:
            # featured authors are take from product.author model
            # _logger.info("Fetching featured authors ")
            featured_authors = request.env['product.author'].search([('feature', '=', True)])
            # _logger.info(f"Found {len(featured_authors)} featured authors ")
            
            result = []
            for author in featured_authors:
                result.append({
                    'id': author.id,
                    'name': author.name,
                    'author_url' : f"/shop/author/{slug(author)}",
                    "imageUrl": f"/web/image/product.author/{author.id}/logo/512x512/{author.name}_{author.id}.jpg",
                })

            values = {
                "featured_authors": result,
            }
            
            # print(f"values ----------------------------->>>{values}")
            return values

        except Exception as e:
            # _logger.error("Error retrieving featured authors : %s", str(e))
            return {'error': str(e), 'message': 'Failed to retrieve featured authors.'}
