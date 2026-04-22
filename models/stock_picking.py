from odoo import fields, models


class StockPicking(models.Model):
    _inherit = "stock.picking"

    sid_pagina_final = fields.Boolean(
        string="Mostrar hoja final",
        copy=True,
        help="Indica si el albaran debe incluir la hoja final de resumen y detalles en el PDF.",
    )
