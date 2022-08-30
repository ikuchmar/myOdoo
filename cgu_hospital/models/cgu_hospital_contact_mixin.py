from odoo import models, fields, api, _

class CGUHospitalContactMixin(models.AbstractModel):
    _name = 'cgu_hospital.contact.mixin'
    _description = 'Contact mixin'

    name = fields.Char(string='Full name')

    LastName = fields.Char(string='Last Name')
    FirstName = fields.Char(string='First Name')
    Surname = fields.Char(string='Surname')

    phone = fields.Char(string='phone')
    email = fields.Char(string='email')
    photo = fields.Image("Image 128", max_width=128, max_height=128, store=True)
    sex = fields.Selection(
        selection=[
            ('man', _('man')),
            ('woman', _('woman'))],
        string='Sex',
        default='man')

    date_birth = fields.Date()
    date_today = fields.Date(default=fields.Date.today)
    age = fields.Char(string='age', compute='_compute_age', store=True)

    passport_series = fields.Char(string="passport_series", size=2, )
    passport_number = fields.Integer(string="passport_number", size=6, )
    passport_issued_when = fields.Date()
    passport_issued_whom = fields.Char()

    @api.onchange('LastName', 'FirstName', 'Surname')
    def _onchange_name(self):
        self.name = "%s %s %s" % (self.LastName, self.FirstName, self.Surname)

    @api.depends('date_birth')
    def _compute_age(self):
        for record in self:
            if record.date_birth:
                record.age = relativedelta(fields.Date.today(), record.date_birth).years
            else:
                record.age = 0
