# -*- coding: utf-8 -*-
{
    'name': "Club deportivo",  # Module title
    'summary': "Gestión de un club deportivo",  # Module subtitle phrase
    'description': """Módulo creado con la finalidad de poder dar de alta a personas y otras gestiones""",  # You can also rst format
    'author': "Rubén López",
    'website': "http://www.example.com",
    'category': 'Deportes',
    'version': '12.0.1',
    'depends': ['base'],
    # This data files will be loaded at the installation (commented becaues file is not added in this example)
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/library_book.xml',
        'views/library_book_categ.xml'
    ],
    # This demo data files will be loaded if db initialize with demo data (commented becaues file is not added in this example)
    # 'demo': [
    #     'demo.xml'
    # ],
}
