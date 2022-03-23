{
    'name': 'estate',
    'version': '1.0',
    'summary' : 'testing',
    'description': 'A Real Estate Module',
    'category': 'realestate',
    'author': 'shofiqul',
    'depends': ['base'],
    'installable': True,
    'auto_install': False,
    'application' : True,

    'data':[
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_menus.xml'

    ]
}
