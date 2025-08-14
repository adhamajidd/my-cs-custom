{
    'name': 'Abajoo Reporting Purchasing',
    'version': '1.0',
    'description': 'Modification of the Odoo Purchasing module to add reporting features',
    'summary': '',
    'author': 'Abajoo',
    'website': '',
    'license': 'LGPL-3',
    'category': 'purchasing',
    'depends': [
        'purchase',
    ],
    'data': [
        'reports/custom_po_report.xml',
        'reports/custom_po_template.xml',
    ],
    'demo': [
        ''
    ],
    'auto_install': False,
    'application': False,
    'icon': '/abajoo_reporting_purchasing/static/description/icon.png',
    'assets': {
        
    }
}