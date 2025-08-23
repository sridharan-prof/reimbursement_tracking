from odoo import models, fields, api

class EmployeeProfile(models.Model):
    _name = 'employee.profile'
    _description = 'Employee Profile details'

    first_name = fields.Char(string= "First Name", required= True)
    middle_name = fields.Char(string= "Middle Name")
    last_name = fields.Char(string= "Last Name", required= True)

    department = fields.Many2one('employee.departments', string= "Department")
    email = fields.Char(string="Email")
    employee_id = fields.Char(string="Employee ID", required=True, default= 'New')

    reimbursements = fields.One2many('reimbursement.details', 'employee_id', string="Reimbursements")

    display_name = fields.Char(compute="_compute_display_name")

    company_id = fields.Many2one('res.company', string="Company", required=True, default=lambda self: self.env.company)
    user_id = fields.Many2one('res.users', string="User")
    
    @api.depends('first_name','middle_name','last_name')
    def _compute_display_name(self):
        for rec in self:
            parts = [rec.first_name, rec.middle_name, rec.last_name]
            rec.display_name = " ".join(filter(None, parts))

    @api.model_create_multi
    def create(self, val_list):
        for vals in val_list:
            if not vals.get('employee_id') or vals['employee_id'] == 'New':
                vals['employee_id'] = self.env['ir.sequence'].next_by_code('employee.profile')
        return val_list
