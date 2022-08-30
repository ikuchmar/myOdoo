from odoo import models, fields, api


class CGUHospitalDoctorAppointment(models.Model):
    _name = 'cgu_hospital.doctor.appointment'
    _description = 'Doctor Appointment'

    name = fields.Char()
    active = fields.Boolean(default=True)

    date = fields.Date()
    time = fields.Datetime()

    state = fields.Integer()

    doctor_id = fields.Many2one(
        comodel_name='cgu_hospital.doctor',
        string='Doctor')

    patient_id = fields.Many2one(
        comodel_name='cgu_hospital.patient',
        string='patient')

    # # діагноз
    # diagnosis_id = fields.Many2one(
    #     comodel_name='hr_hospital.diagnosis',
    #     string='diagnosis')
    #
    # # рекомендації
    # recommendations = fields.Text()
    #
    # research_ids = fields.Many2many(
    #     string="Researchs",
    #     relation="visit_to_doctor_and_research",
    #     comodel_name='hr_hospital.research',
    #     column1='visit_to_doctor_id',
    #     column2='research_id'
    # )

    @api.onchange('patient_id', 'doctor_id', 'doctor_id', 'date_visit')
    def _onchange_name(self):
        self.name = f'{self.patient_id.name} | {self.doctor_id.name} ({self.date_visit})'
