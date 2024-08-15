{
    'name': 'Bookstore Management',
    'version': '1.0',
    'summary': 'Manage books, authors, and customers in a bookstore',
    'sequence': 10,
    'description': """
        Custom module for managing a bookstore:
        - Books and Authors
        - Inventory management
        - Basic CRM functionalities
        - Dashboard and views
    """,
    'category': 'Sales/Management',
    'author': 'Juan Camilo Sandoval Garcia',
    'depends': ['base', 'sale_management', 'sale', 'crm'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',

        'views/author_views.xml',
        'views/customer_views.xml',
        'views/bookstore_dashboard_views.xml',
        'views/bookstore_menus.xml',
        'views/sale_order_views.xml',

        'data/bookstore_data.xml',
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
