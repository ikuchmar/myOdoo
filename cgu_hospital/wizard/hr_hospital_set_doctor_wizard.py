from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class HrHospitalSetDoctorForPatientsWizard(models.TransientModel):
    _name = 'hr_hospital.set.doctor.wizard'
    _description = "Wizard to set_doctor_for_patients"

    # names = fields.Char(
    #     string='Patients Names',
    #     required=False,
    # )

    patient_ids = fields.Many2many(
        string="patients",
        comodel_name='hr_hospital.patient',
        relation = 'set_doctor_wizard_rel'
        # column2='patient_id'
        )

    # лікарь(doctor)
    doctor_id = fields.Many2one(
        comodel_name='hr_hospital.doctor',
        string='Doctor')

    def action_set_personal_doctor(self):
        self.ensure_one()
        self.patient_ids.write({"personal_doctor_id": self.doctor_id.id})

    # def action_open_wizard(self):
    #     return {
    #         'name': _('Create Partners Wizard'),
    #         'type': 'ir.actions.act_window',
    #         'view_mode': 'form',
    #         'res_model': 'create.partner.multi.wizard',
    #         'target': 'new',
    #         'context': {'default_country_id': self.env.user.country_id.id},
    #     }
    #
    # def action_create(self):
    #     self.ensure_one()
    #     for name in self.names.split(','):
    #         self.env['res.partner'].create({
    #             'name': name,
    #             'company_type': self.company_type,
    #             'country_id': self.country_id.id,
    #         })