from odoo import models, fields

class ReimbursementDetails(models.Model):
    _name = 'reimbursement.details'
    _description = "Reimbursement Details"
    
    employee_id = fields.Many2one('employee.profile', string="Employee", required=True)
    type_id = fields.Many2one('reimbursement.type', string="Reimbursement Type")
    amount = fields.Float(string="Amount", required=True)
    submitted_date = fields.Date(string= "Submitted On", default= fields.Date.today)
    current_status = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('approved', 'Approved'),
        ('rejected','Rejected'),
        ('paid', 'Paid')
    ], string="Status", default='draft')
    state_changes = fields.One2many('reimbursement.state.change.details', 'reimbursement_id', string="Status Detail")


    def action_submit(self):
        self.write({
            'current_status': 'submitted',
            'submitted_date': fields.Datetime.now()
        })
        self.env['reimbursement.state.change.details'].create({
            'reimbursement_id': self.id,
            'previous_state': 'draft',
            'new_state': 'submitted',
            'changed_by': self.env.user.name,
            'remarks': 'Submitted by employee'
        })
