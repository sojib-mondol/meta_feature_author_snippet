# -*- coding: utf-8 -*-
{
    'name': 'Meta Authors by Feature',
    'version': '17.0.1.0',
    'summary': """ 
        Meta Authors by Feature showcases authors categorized by their unique contributions, offering insights into diverse writing styles and themes.
    """,
    "description": """
        This resource highlights authors within the Meta ecosystem, organizing them by specific features or themes, helping readers discover new voices and understand the varied landscape of writing.
    """,
    'author': 'Sojib',
    'website': 'https://www.metamorphosis.com.bd',
    'category': 'Website',
    
    'depends': ['website','meta_book_info'],
    
    "data": [
        "views/authors_views.xml",
        "views/templates.xml",
    ],
    
    'assets': {
        'web.assets_frontend': [
            '/meta_feature_author/static/src/xml/featured_authors.xml',
            '/meta_feature_author/static/src/css/owl.carousel.min.css',
            '/meta_feature_author/static/src/css/style.css',
            '/meta_feature_author/static/src/css/owl.theme.default.min.css',
            
            '/meta_feature_author/static/src/js/owl.carousel.js',
            '/meta_feature_author/static/src/js/featured_authors.js'
           
        ],
    },
    
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}

