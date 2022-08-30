from odoo import models, fields


class CGUHospitalSpecialty(models.Model):
    _name = 'cgu_hospital.specialty'
    _description = 'specialty'

    name = fields.Char()

    active = fields.Boolean(default=True)

    parent_id = fields.Many2one(
        comodel_name='cgu_hospital.specialty',
        string='Parent Category',
        index=True,
        ondelete='cascade')
