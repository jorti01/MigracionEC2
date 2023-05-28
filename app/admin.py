# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from app.models import DocumentosHojaVida,AsistenciaCapacitacion,Ausentismo,SubCategoriasCalificacion,CalificacionesProveedores,CalificacionProveedores,Requerimiento,ProductosServicios,Bitacoras, Temas,BitacorasRegistro,Capacitaciones,HojasdeVida,SolicitudesC,Proveedores,OrdenCompra,Correspondencia

admin.site.register(Bitacoras)
admin.site.register(Temas)
admin.site.register(BitacorasRegistro)
admin.site.register(AsistenciaCapacitacion)
admin.site.register(Capacitaciones)
admin.site.register(HojasdeVida)
admin.site.register(SolicitudesC)
admin.site.register(Proveedores)
admin.site.register(CalificacionProveedores)
admin.site.register(OrdenCompra)
admin.site.register(ProductosServicios)
admin.site.register(Correspondencia)
admin.site.register(Requerimiento)
admin.site.register(CalificacionesProveedores)
admin.site.register(SubCategoriasCalificacion)
admin.site.register(DocumentosHojaVida)
admin.site.register(Ausentismo)
