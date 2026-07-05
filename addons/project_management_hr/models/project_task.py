from odoo import models, fields

class ProjectTask(models.Model):
    _inherit = 'project.task'
    employee_id = fields.Many2one('hr.employee', string='Nhan vien phu trach')
