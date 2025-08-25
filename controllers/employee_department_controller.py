from odoo import http
from odoo.http import request

class EmployeeDepartmentsFrontend(http.Controller):

    @http.route('/departments', auth='public', website=True)
    def departments_page(self, **kwargs):
        departments = request.env['employee.departments'].sudo().search([])
        return request.render('reimbursement_tracking.departments_page_template', {
            'departments': departments
        })
