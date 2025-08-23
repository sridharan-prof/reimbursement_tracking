from odoo import models, fields

class ReimbursementStateChange(models.Model):
    _name = 'reimbursement.state.change.details'
    _description = 'Reimbursement State Change Details'

    reimbursement_id = fields.Many2one('reimbursement.details', string="Reimbursement", required=True)
    previous_state = fields.Char(string="Previous State")
    new_state = fields.Char(string="New State")
    changed_on = fields.Datetime(string="Changed On", default=fields.Datetime.now)
    changed_by = fields.Char(string="Changed By")
    remarks = fields.Text(string="Remarks")
