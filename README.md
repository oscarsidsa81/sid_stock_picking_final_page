# sid_stock_picking_final_page

## Proposito
Modulo pequeno para desacoplar el campo Studio `x_pagina_final` de `stock.picking` y sustituirlo por un campo propio de modulo: `sid_pagina_final`.

## Que hace
- Crea `sid_pagina_final` en `stock.picking`.
- Migra los valores `True` desde `x_pagina_final` mediante `post_init_hook`.
- Anade el nuevo campo al formulario de albaran con la etiqueta **Mostrar hoja final**.
- Reengancha `x_motivo` para que siga apareciendo despues del nuevo campo.
- Anade una herencia de `stock.report_delivery_document` para que la pagina final del PDF dependa de `sid_pagina_final`.

## Base tecnica validada
En la base actual se ha comprobado que:
- `x_pagina_final` existe solo en `stock.picking`.
- Es un campo manual/Studio `boolean` con columna fisica en `stock_picking`.
- Tiene pocos registros a `True`.
- No tiene automatizaciones, server actions ni filtros guardados asociados.
- Se usa en:
  - una vista QWeb del albaran
  - una vista formulario que muestra el booleano
  - una vista formulario que inserta `x_motivo` despues de ese campo

## Importante antes o despues de instalar
Para evitar duplicidades o que siga usandose el campo legacy en vistas antiguas, conviene desactivar estas vistas exportadas de Studio si siguen activas:

- `__export__.ir_ui_view_2334_eb00c462`
- `__export__.ir_ui_view_2628_f3896426`
- `__export__.ir_ui_view_2423_093898bc`

## Script shell recomendado para desactivar vistas legacy
```python
xmlids_to_disable = [
    "__export__.ir_ui_view_2334_eb00c462",
    "__export__.ir_ui_view_2628_f3896426",
    "__export__.ir_ui_view_2423_093898bc",
]

for xmlid in xmlids_to_disable:
    try:
        view = env.ref(xmlid)
        print("Desactivando:", xmlid, "|", view.name)
        view.active = False
    except Exception as e:
        print("No se pudo resolver:", xmlid, "|", e)

env.cr.commit()
print("OK")
```

## Validacion posterior
```python
Picking = env["stock.picking"]
print("sid_pagina_final en _fields:", "sid_pagina_final" in Picking._fields)
print("sid_pagina_final=True:", Picking.search_count([("sid_pagina_final", "=", True)]))

recs = Picking.search(["|", ("x_pagina_final", "!=", False), ("sid_pagina_final", "!=", False)])
mismatch = recs.filtered(lambda r: bool(r.x_pagina_final) != bool(r.sid_pagina_final))
print("Descuadres:", len(mismatch))
```

## Nota
El modulo no elimina el campo legacy `x_pagina_final`; simplemente deja de depender funcionalmente de el.
