# -*- coding: utf-8 -*-
{
    'name': "cgu_hospital",

    'summary': """
        cgu_hospital Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0
    # /odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '15.0.1.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        # 'views/hr_hospital_doctor_views.xml',
        # 'views/hr_hospital_patient_views.xml',
        # 'views/hr_hospital_visit_to_doctor_views.xml',
        # 'views/hr_hospital_diagnosis_views.xml',
        #
        # 'views/hr_hospital_menu.xml',
        # 'views/hr_hospital_sick_views.xml',
        # 'views/hr_hospital_research_views.xml',
        # 'views/hr_hospital_personal_doctor_history_views.xml',
        # # 'views/templates.xml',
        # 'wizard/hr_hospital_set_doctor_wizard_views.xml',
        # 'wizard/hr_hospital_sick_report_wizard_views.xml',
        # 'report/hr_hospital_doctor_report.xml',
        # 'report/hr_hospital_doctor_reports_template.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}
