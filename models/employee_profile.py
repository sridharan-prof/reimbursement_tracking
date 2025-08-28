from odoo import models, fields, api
import pytz 

class EmployeeProfile(models.Model):
    _name = 'employee.profile'
    _description = 'Employee Profile details'

    # Links
    user_id = fields.Many2one('res.users', string="User")
    hr_employee_id = fields.Many2one('hr.employee', string='HR Employee')

    # Related fields (avoid duplication, always in sync)
    name = fields.Char(related="hr_employee_id.name", store=True)
    image = fields.Image(related="hr_employee_id.image_1920", store=True)
    job_position = fields.Char(related="hr_employee_id.job_title", store=True)
    work_mobile = fields.Char(related="hr_employee_id.mobile_phone", store=True)
    work_email = fields.Char(related="hr_employee_id.work_email", store=True)
    work_address = fields.Char(related="hr_employee_id.work_location_id.name", store=True)
    department = fields.Many2one(related="hr_employee_id.department_id", store=True)
    company_id = fields.Many2one(related="hr_employee_id.company_id", store=True)

    # Extra fields (only in profile)
    working_hours = fields.Char("Working Hours", tracking=True)
    timezone = fields.Selection(selection='_tz_get', string="Time Zone", tracking=True)

    # Private contact
    personal_email = fields.Char(string="Personal Email", tracking=True)
    phone = fields.Char(string="Phone", tracking=True)
    language = fields.Char(string="Language", tracking=True)

    marital_status = fields.Char(string="Marital Status", tracking=True)

    # Emergency contact
    contact_name = fields.Char(string="Contact Name", tracking=True)
    contact_number = fields.Char(string="Contact Number", tracking=True)

    # Education
    certificate_level = fields.Selection([
        ("graduate", "Graduate"),
        ("bachelor", "Bachelor"),
        ("master", "Master"),
        ("other", "Other")
    ], default="other", tracking=True)
    field_of_study = fields.Char(string="Field of Study", tracking=True)
    school = fields.Char(string="School", tracking=True)
    employee_code = fields.Char(string="Employee Code",readonly=True,copy=False,default="NEW")

    reimbursements = fields.One2many('reimbursement.details', 'employee_id', string="Reimbursements")

    @staticmethod
    def _tz_get():
        return [(tz, tz) for tz in pytz.all_timezones]

    @api.model_create_multi
    def create(self, val_list):
        for vals in val_list:
            if not vals.get('employee_code') or vals['employee_code'] == 'NEW':
                vals['employee_code'] = self.env['ir.sequence'].next_by_code('employee.profile')
        return super().create(val_list)