from odoo import SUPERUSER_ID, api


def post_init_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    Picking = env["stock.picking"].sudo()

    if "x_pagina_final" not in Picking._fields:
        return
    if "sid_pagina_final" not in Picking._fields:
        return

    recs = Picking.search([("x_pagina_final", "=", True)])
    for rec in recs:
        if rec.sid_pagina_final != rec.x_pagina_final:
            rec.write({"sid_pagina_final": rec.x_pagina_final})
