db = DAL("sqlite://storage.sqlite")

from gluon.tools import Auth
auth = Auth(globals(), db)
auth.define_tables(username=False)
auth.settings.actions_disabled.append('register')

db.define_table('semen',
                Field('fecha_adquisicion','date'),
                Field('raza'),
                Field('granja_adquisicion'),
                Field('granja_adq_telefono'),
               format='muestra %(id)s %(raza)s'
               )
db.semen.fecha_adquisicion.requires = IS_DATE(error_message = "Debes poner la fecha de adquisicion!")
db.semen.raza.requires = IS_NOT_EMPTY(error_message = "Debes poner la raza!")
db.semen.granja_adquisicion.requires = IS_NOT_EMPTY(error_message = "Debes poner la granja de donde se adquirio!")

db.define_table('cerda',
                Field('raza', 'string'),
                Field('fecha_nacimiento', 'datetime'),
                Field('nombre', 'string'),
                Field('id_madre', 'reference cerda'),
                Field('padre', 'reference semen'),
               format='%(id)s %(nombre)s')
db.cerda.raza.requires = IS_NOT_EMPTY(error_message = "Debes poner la raza!")
db.cerda.fecha_nacimiento.requires = IS_DATETIME(error_message = "Debes poner la fecha de nacimiento!")
#db.cerda.id_madre.requires = IS_IN_DB(db, db.cerda.id, "%(id)s %(nombre)s", error_message = "Debes poner el numero de identificacion de la madre")


db.define_table('monta',
                Field('id_semen', 'reference semen'),
                Field('id_cerda', 'reference cerda'),
                Field('id_usuario', 'reference auth_user', writable=False, default=auth.user_id),
                Field('fecha_monta', 'datetime'),
                Field('fecha_registrar_preñez', 'datetime'),
                Field('fecha_posible_parto', 'datetime'),
                Field('prueba_preñez', requires=IS_IN_SET({'Sin determinar': None,'Positivo':'Positivo','Negativo':'Negativo'}, zero=None), writable=True),
               )
db.monta.id_semen.requires = IS_IN_DB(db, db.semen.id, "muestra %(id)s %(raza)s", error_message = "Debes poner el numero de identificacion del semen")
db.monta.id_cerda.requires = IS_IN_DB(db, db.cerda.id, "%(id)s %(nombre)s", error_message = "Debes poner el numero de identificacion de la cerda")
db.monta.fecha_monta.requires = IS_DATETIME(error_message = "Debes poner la fecha de la monta!")

db.define_table('tareasgestacion',
                Field('id_monta', 'reference monta'),
                Field('incrementar_alimento', 'datetime'),
                Field('desparasitacion_externa', 'datetime'),
                Field('vermifugacion', 'datetime'),
                Field('disminuir_alimento', 'datetime'),
                Field('ubicar_paridera', 'datetime'),
                format='Tarea de la monta %(id_monta)s'
               )
db.tareasgestacion.id_monta.requires = IS_NOT_EMPTY(error_message = "Debes poner la monta!")

db.define_table('parto',
                Field('id_tareas_gestacion', 'reference tareasgestacion'),
                Field('id_usuario', 'reference auth_user', writable=False, default=auth.user_id),
                Field('fecha_parto', 'datetime'),
                Field('cantidad_nacidos', 'integer'),
                Field('cantidad_nacidos_vivos', 'integer'),
                Field('cantidad_nacidos_muertos', 'integer'),
                Field('cantidad_nacidos_machos', 'integer'),
                Field('cantidad_nacidos_hembras', 'integer'),
                Field('registrados', 'boolean', default=False, readable=False, writable=False)
                )
db.parto.fecha_parto.requires = IS_DATETIME(error_message = "Debes poner la fecha del parto!")
db.define_table('lechon',
                Field('id_lote', 'reference parto'),
                Field('fecha_nacimiento', 'datetime'),
                Field('raza', 'string'),
                Field('peso_nacer', 'double'),
                Field('peso_destete', 'double'),
                Field('peso_prelevante', 'double'),
                Field('peso_levante', 'double'),
                Field('peso_precebo', 'double'),
                Field('peso_cebo', 'double'),
                Field('id_madre', 'reference cerda'),
                Field('id_padre', 'reference semen'))
db.lechon.id_padre.requires = IS_IN_DB(db, db.semen.id, "muestra %(id)s %(raza)s", error_message = "Debes poner el numero de identificacion del padre/semen")
db.lechon.id_madre.requires = IS_IN_DB(db, db.cerda.id, "%(id)s %(nombre)s", error_message = "Debes poner el numero de identificacion de la madre/cerda")
