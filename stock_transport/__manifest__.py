{
    'name': 'Transport',
    'summary': 'Dispatch Management System',
    'depends': [
        'base',
        'fleet',
        'stock_picking_batch',
    ],
    'category': 'Transport/Dispatch',
    'data' : [
        'security/ir.model.access.csv',

        'views/inherited_views_categories.xml',
        'views/inherited_views_stock_picking.xml',
    ],
    'application': True,
    'installable': True,
}
