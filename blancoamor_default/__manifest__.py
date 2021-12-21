{
    'name': 'dck_blancoamor',
    'version': '13.0.0.0',
    'category': 'Tools',
    'summary': "Proyecto geolocation",
    'author': 'Ing. Gabriela Rivero',
    'depends': [
        'base',
    ],
    'data': [
    ],
    'installable': True,
    'application': False,

    'limit_request': '8196',
    'limit_memory_soft': '640000000',
    'limit_memory_hard': '760000000',
    'limit_time_cpu': '60',
    'limit_time_real': '120',

    # manifest version, if omitted it is backward compatible
    'env-ver': '2',

    # if Enterprise it installs in a different directory than community
    'odoo-license': 'CE',

    # port where odoo starts serving pages
    'port': '8016',
    'longpolling_port': '8078',

    # list of url repos to install in the form 'repo-url directory'
    'git-repos': [
        'https://github.com/filoquin/cl-blancoamor.git',
        'git@code.gestionblancoamor.com:odoo-13/blancoamor.git'
    ],
    'docker-images': [
        'odoo regaby/odoo-ce:13.0',
        # 'postgres postgres:10.1-alpine',
        'postgres mdillon/postgis:11-alpine',
        #'nginx nginx'
    ]
    #'base_dir': '/opt/odoo/docker_files/'
}
