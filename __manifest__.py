
{
    'name': 'estate',
    'version': '1.0',
    'summary': 'testing',
    'description': 'A Real Estate Module',
    'category': 'realestate',
    'author': 'shofiqul',
    'depends': ['base'],
    'installable': True,
    'license': 'LGPL-3',
    'auto_install': False,
    'application': True,

    'data': [
        'security/ir.model.access.csv',


        'views/estate_property_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_tag_views.xml',
        'views/estate_property_offer_views.xml',

        'views/estate_menus.xml'

    ]
}
