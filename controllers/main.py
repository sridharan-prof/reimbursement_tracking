from odoo import http
from odoo.http import request

class HelloOwlController(http.Controller):
    @http.route('/hello-owl', auth='public', website=True)
    def hello_owl(self, **kw):
        return http.request.render('reimbursement_tracking.hello_page_template', {}) # this method will call the hello_page_template
    
    @http.route('/login', auth='public', website=True, csrf=True, methods=['GET', 'POST'])
    def hello_login(self, **post):
        if request.httprequest.method == 'POST':
            login = post.get('login')
            password = post.get('password')
            uid = request.session.authenticate(request.db, login, password)
            if uid:
                return request.redirect('/')  # Redirect to homepage or a custom page
            else:
                return request.render('reimbursement_tracking.login_page', {'error': 'Invalid credentials'})
        return request.render('reimbursement_tracking.login_page')
    
    @http.route('/employeeprofile', type='http', auth='user', website=True)
    def employee_profile(self, **kw):
        emp = request.env['employee.profile'].sudo().search([
            ('user_id', '=', request.env.user.id)
        ], limit=1)
        return request.render('reimbursement_tracking.employee_profile_page', {'employee': emp})