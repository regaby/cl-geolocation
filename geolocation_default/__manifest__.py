{
    'name': 'geolocation',
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
    'port': '8069',

    # list of url repos to install in the form 'repo-url directory'
    'git-repos': [
        'https://github.com/regaby/cl-geolocation.git',
        'https://github.com/regaby/odoo-custom.git',
        'https://github.com/jobiols/odoo-addons.git',
        ## localización
        'https://github.com/ingadhoc/odoo-argentina.git',
        'https://github.com/ingadhoc/odoo-argentina-ce.git',
        'https://github.com/ingadhoc/account-analytic.git',
        'https://github.com/ingadhoc/argentina-sale.git',
        'https://github.com/ingadhoc/account-payment.git',
        'https://github.com/ingadhoc/account-invoicing.git',
        'https://github.com/ingadhoc/account-financial-tools.git',
        'https://github.com/ingadhoc/sale.git',
        'https://github.com/ingadhoc/stock.git',
        'https://github.com/ingadhoc/aeroo_reports.git',
        'https://github.com/ingadhoc/miscellaneous.git',
        'https://github.com/ingadhoc/multi-company.git',
        'https://github.com/ingadhoc/multi-store.git',
        'https://github.com/ingadhoc/product.git ingadhoc-product',
        'https://github.com/ingadhoc/project.git ingadhoc-project',
        'https://github.com/ingadhoc/purchase.git ingadhoc-purchase',
        'https://github.com/ingadhoc/website.git ingadhoc-website',
        'https://github.com/OCA/account-financial-reporting.git',
        'https://github.com/OCA/mis-builder.git',
        # dependencias de wms , mas web
        'https://github.com/OCA/server-env.git',
        'https://github.com/OCA/rest-framework.git',
        'https://github.com/OCA/connector.git',
        'https://github.com/OCA/server-auth.git',
        ##
        # ## blancoamor
        # # 'https://code.gestionblancoamor.com/odoo/ba_delivery_zone.git',
        # # 'https://code.gestionblancoamor.com/odoo/ba_purchase.git',
        # 'git@code.gestionblancoamor.com:odoo/ba_delivery_zone.git',
        # 'git@code.gestionblancoamor.com:odoo/ba_purchase.git',
        # #'https://code.gestionblancoamor.com/odoo/cruz-del-sur.git',
        # 'git@code.gestionblancoamor.com:odoo/cruz-del-sur.git',
        ## operating unit
        'https://github.com/OCA/operating-unit.git',
        'https://github.com/OCA/web.git',
        'https://github.com/OCA/hr.git oca-hr',
        'https://github.com/OCA/hr-attendance.git oca-hr-attendance',
        'https://github.com/OCA/hr-expense.git oca-hr-expense',
        'https://github.com/OCA/hr-holidays.git oca-hr-holidays',
        'https://github.com/OCA/knowledge.git oca-knowledge',
        'https://github.com/OCA/maintenance.git oca-maintenance',
        'https://github.com/OCA/management-system.git oca-management-system',
        'https://github.com/OCA/partner-contact.git oca-partner-contact',
        'https://github.com/OCA/product-pack.git oca-product-pack',
        'https://github.com/OCA/project.git oca-project',
        'https://github.com/OCA/queue.git oca-queue',
        'https://github.com/OCA/reporting-engine.git',
        'https://github.com/OCA/sale-financial.git oca-sale-financial',
        'https://github.com/OCA/sale-workflow.git',
        'https://github.com/OCA/server-brand.git oca-server-brand',
        'https://github.com/OCA/server-tools.git',
        'https://github.com/OCA/server-ux.git',
        'https://github.com/OCA/stock-logistics-warehouse.git',
        'https://github.com/OCA/stock-logistics-workflow.git',
        'https://github.com/OCA/social.git oca-social',
        'https://github.com/OCA/wms.git',
        'https://github.com/OCA/geospatial.git',
        'https://github.com/OCA/product-attribute.git',
    ],

    'docker-images': [
        'odoo regaby/odoo-ce:13.0',
        # 'postgres postgres:10.1-alpine',
        'postgres mdillon/postgis:11-alpine',
        'nginx nginx'
    ]
}
