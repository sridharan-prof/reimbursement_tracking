from odoo import http
from odoo.http import request

class EmployeeDetailFrontEnd(http.Controller):

    @http.route('/details', auth = 'public', wesite = True)
    def departments_page(self, **kwargs):
        details = request.env['employee.details'].sudo().search([])
        return request.render('reimbursement_tracking.details_page_template', {
            'details': details
        })