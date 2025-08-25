from odoo import models, fields, api

class EmployeeDepartments(models.Model):
    _name = 'employee.departments'
    _description = 'Department Details'

    dept_id = fields.Char(string= 'Dept_Id', default= 'New')
    name = fields.Char(string= "Name")
    
    @api.model_create_multi
    def create(self, val_list):
        for vals in val_list:
            if not vals.get('dept_id') or vals['dept_id'] == 'New':
                vals['dept_id'] = self.env['ir.sequence'].next_by_code('employee.departments')
        return val_list
