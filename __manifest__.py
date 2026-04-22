# -*- coding: utf-8 -*-
{
    "name": "sid_stock_picking_final_page",
    "version": "15.0.1.0.0",
    "category": "Inventory",
    "summary": "Migra y desacopla x_pagina_final a sid_pagina_final en stock.picking.",
    "author": "oscarsidsa81",
    "license": "LGPL-3",
    "depends": [
        "stock",
    ],
    "data": [
        "views/stock_picking_views.xml",
        "reports/stock_picking_report.xml",
    ],
    "post_init_hook": "post_init_hook",
    "installable": True,
    "application": False,
}
