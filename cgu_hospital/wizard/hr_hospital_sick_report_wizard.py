from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class HrHospitalSickReportWizard(models.TransientModel):
    _name = 'hr_hospital.sick.report.wizard'
    _description = "Wizard sick report "

    # Створити   звіт     хвороб     за     місяць, який
    # є тимчасовою     моделлю, з     вибором     року     і
    # місяця, яка     розраховує     хвороби     та
    # кількість     діагнозів     цієї     хвороби.

    # хвороба
    sick_id = fields.Many2one(
        comodel_name='hr_hospital.sick',
        string='sick')

    # кількість     діагнозів
    sick_qty = fields.Integer(string='sick qty')

    #
    date_visit = fields.Date()

