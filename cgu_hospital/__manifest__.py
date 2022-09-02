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
        'security/cgu_hospital_groups.xml',
        'security/ir.model.access.csv',
        'views/cgu_hospital_menu.xml',
        'views/cgu_hospital_analysis_direction_views.xml',
        'views/cgu_hospital_analysis_result_views.xml',
        'views/cgu_hospital_analysis_type_views.xml',
        'views/cgu_hospital_doctor_appointment_views.xml',
        'views/cgu_hospital_doctor_views.xml',
        'views/cgu_hospital_patient_views.xml',
        'views/cgu_hospital_speciality_views.xml',
        'report/cgu_hospital_analysis_direction_report.xml',
        'report/cgu_hospital_analysis_direction_report_template.xml',
        'wizard/cgu_hospital_set_doctor_wizard_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'data/cgu_hospital_speciality_demo.xml',
        'data/cgu_hospital_analysis_type_demo.xml',
        'data/cgu_hospital_doctor_demo.xml',
        'data/cgu_hospital_patient_demo.xml',
    ],
}
