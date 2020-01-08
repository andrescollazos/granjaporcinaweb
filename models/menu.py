# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------

response.menu = [
    (T('Home'), False, URL('default', 'index'), []),
    (T('Semen'), False, URL('default', 'semen_manager'), []),
    (T('Cerdas'), False, URL('default', 'cerda_manager'), []),
    (T('Montas'), False, URL('default', 'monta_manager'), []),
    (T('Tareas'), False, URL('default', 'tareasgestacion_manager'), []),
    (T('Partos'), False, URL('default', 'parto_manager'), []),
    (T('Lechones'), False, URL('default', 'lechon_manager'), [])
]

# ----------------------------------------------------------------------------------------------------------------------
# provide shortcuts for development. you can remove everything below in production
# -
