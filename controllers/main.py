from odoo import http

class HelloOwlController(http.Controller):
    @http.route('/hello-owl', auth='public', website=True)
    def hello_owl(self, **kw):
        return http.request.render('reimbursement_tracking.hello_page_template', {}) # this method will call the hello_page_template
    
    @http.route('/login', auth='public', website=True)
    def hello_login(self, **kw):
        return http.request.render('reimbursement_tracking.login_page', {}) # this method will call the hello_page_template
    
