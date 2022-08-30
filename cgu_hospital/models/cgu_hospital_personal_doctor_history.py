from odoo import models, fields, api


class CGUHospitalDoctorHistory(models.Model):
    _name = 'cgu_hospital.personal.doctor.history'
    _description = 'HR Hospital personal_doctor_history'

    name = fields.Char()
    active = fields.Boolean(default=True)

    # дату діагностування(date     of     diagnosis)
    date_medication = fields.Date()

    # лікарь(doctor)
    doctor_id = fields.Many2one(
        comodel_name='hr_hospital.doctor',
        string='Doctor')

    # patient
    patient_id = fields.Many2one(
        comodel_name='hr_hospital.patient',
        string='patient')

    # хвороба
    sick_id = fields.Many2one(
        comodel_name='hr_hospital.sick',
        string='sick')

    sick_type_color = fields.Integer(related='sick_id.sick_type_id.color')

    sick_type_id = fields.Many2one(related='sick_id.sick_type_id')


    @api.onchange('patient_id', 'doctor_id', 'doctor_id', 'date_medication')
    def _onchange_name(self):
        self.name = f'{self.patient_id.name} | {self.doctor_id.name} ({self.date_medication})'

# @api.model
    # def write(self, vals_list):
    #     # for val in vals_list:
    #         # a = 1
    #         # val.name = f'{val.patient_id.name} | {val.doctor_id.name} | {val.sick_id.name} ({val.sdate_medication})'
    #         # val.name = "%s | %s | %s | %s" % (val.patient_id.name, val.doctor_id.name, val.sick_id.name, val.sdate_medication)
    #     return super().write(vals_list)
