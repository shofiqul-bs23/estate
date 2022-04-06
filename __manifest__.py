{
    'name': 'estate',
    'version': '1.0',
    'summary': 'testing',
    'description': 'A Real Estate Module',
    'category': 'realestate',
    'author': 'shofiqul',
    'depends': ['base',
                'report_xlsx'
                ],
    'installable': True,
    'license': 'LGPL-3',
    'auto_install': False,
    'application': True,

    'data': [
        'security/ir.model.access.csv',

        'wizard/print_offers_wizard_view.xml',

        'views/estate_property_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_tag_views.xml',
        'views/estate_property_offer_views.xml',
        'views/res_users_views.xml',

        'report/estate_property_reports.xml',
        'report/estate_property_templates.xml',
        'views/estate_menus.xml'

    ]
}
