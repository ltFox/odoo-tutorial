{
    'name': 'My First Component',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'An example of creating a front-end component in Odoo',
    'author': 'ltFox',
    'depends': ['base', 'web'],
    'data': [
        'views/my_action_view.xml',
    ],
    'assets': {
        'web.assets_backend': [
            '/my_first_component/static/src/my_button/my_button.js',
            '/my_first_component/static//src/my_button/my_button.xml',
        ],
    },
}
