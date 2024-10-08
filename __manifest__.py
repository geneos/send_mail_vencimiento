# -*- coding: utf-8 -*-
{
    'name': "Send mail vencimientos",
    'summary': """
      Envia listado de productos de lotes a vencer.""",
    'description': """
       Modulo desarrollado para Celimundo.
    """,
    'category': 'mail',
    'version': '13.0',
    'author': "Cooperativa GENEOS - Fernando Recci",
    'depends': ['base','stock'],
    'data': [
        'data/template.xml',
        'report/report.xml',
        'views/report_send_vencimiento.xml',
        'wizards/wizard_stock_vencimientos_view.xml'
    ],
    'demo': [
    ],

    'images': ['static/description/sedpdf.png'],
}