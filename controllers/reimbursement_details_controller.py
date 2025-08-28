from odoo import http
from odoo.http import request

class ReimbursementController(http.Controller):

    @http.route(['/reimbursement_form'], type='http', auth="user", website=True)
    def reimbursement_form(self, **kwargs):
        # Get current logged-in user
        user = request.env.user
        
        employee = request.env['employee.profile'].sudo().search([('user_id', '=', user.id)], limit=1)

        return request.render("reimbursement_tracking.reimbursement_form_template", {
            'employee': employee,
        })

    @http.route(['/reimbursement/submit'], type='http', auth="user", website=True, csrf=True)
    def submit_reimbursement(self, **post):
        user = request.env.user
        employee = request.env['employee.profile'].sudo().search([('user_id', '=', user.id)], limit=1)

        if employee:
            request.env['reimbursement.details'].sudo().create({
                'employee_id': employee.id,
                'type_id': int(post.get('type_id')) if post.get('type_id') else False,
                'amount': float(post.get('amount')) if post.get('amount') else 0.0,
                'remarks': post.get('remarks'),
            })

        return request.redirect('/reimbursement_form?submitted=1')
