{
    'name': "Sales Management",
    'version': "1.0",
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/employee_departments_views.xml',
        'views/menuitems.xml',
    ],
    'assets': {
        'web.assets_backend': [
        ],
    },
    'application': True,
}
