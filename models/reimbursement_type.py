from odoo import models, fields, api

class ReimbursementType(models.Model):
    _name = 'reimbursement.type'
    _description = 'Reimburesment Type'
    
    name = fields.Char(string='Reimbursement Type', required= True)
    description = fields.Text(string="Description")
    active = fields.Boolean(string="Active", default=True)