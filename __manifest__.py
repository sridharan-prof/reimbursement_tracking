{
    'name': "Reimbursement Tracking",
    'version': "1.0",
    'depends': ['base', 'web','website'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/employee_departments_views.xml',
        'views/templates.xml',
        'views/login.xml',
        'views/employee_profile.xml',
        'views/menuitems.xml',
    ],
    'assets': {
        'web.assets_backend': [
        ],
        'web.assets_frontend': [
            'reimbursement_tracking/static/src/js/hello_component.js',
            'reimbursement_tracking/static/src/xml/hello_component.xml',
            'reimbursement_tracking/static/src/css/custom.css',
        ],
    },
    'application': True,
    'installable': True,
}
