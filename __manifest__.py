{
    'name': "Reimbursement Tracking",
    'version': "1.0",
    'depends': ['base', 'web', 'website'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/employee_departments_views.xml',
        'views/templates.xml',
        'views/login.xml',
        'views/employee_profile.xml',
        'views/employee_detail_views.xml',
        'views/menuitems.xml',
        'views/employee_department_templates.xml',
        'views/employee_detail_template.xml',
    ],
    'assets': {
        'web.assets_backend': [
        ],
        'web.assets_frontend': [
            'reimbursement_tracking/static/src/js/hello_component.js',
            'reimbursement_tracking/static/src/xml/hello_component.xml',
            'reimbursement_tracking/static/src/css/custom.css',
            'reimbursement_details/static/src/css/employee_department.css',
            'reimbursement_details/static/src/css/employee_detail.css',
            'reimbursement_details/static/src/js/employee_departments.js',
            'reimbursement_details/static/src/js/employee_detail.js',
            'reimbursement_details/static/src/xml/employee_departments.xml',
        ],
    },
    'application': True,
    'installable': True,
}
