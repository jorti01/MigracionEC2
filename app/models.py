# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta,datetime,date



class ImagenRequerimiento(models.Model):
    imagen = models.ImageField(upload_to='imagenesrequerimientos')
    requerimiento_relacionado = models.IntegerField(null = True, blank = True)



class CalificacionProveedores(models.Model):
    id = models.AutoField(primary_key=True)
    categoria = models.TextField()
    peso = models.IntegerField()
    def __str__(self):
        return self.categoria

class EvaluacionesSeleccion(models.Model):
    id = models.AutoField(primary_key=True)
    documentos_legales = models.IntegerField()
    forma_pago = models.IntegerField()
    precio = models.IntegerField()
    gestion_cotizaciones = models.IntegerField()
    certificaciones_calidad = models.IntegerField()
    implementacion_sgsst = models.IntegerField()
    documentos_ambientales = models.IntegerField()
    proveedor_relacionado = models.IntegerField(null = True, blank = True)
    fecha = models.DateTimeField(auto_now_add=True)
class CalificacionesProveedores(models.Model):
    id = models.AutoField(primary_key=True)
    categoria = models.ManyToManyField(CalificacionProveedores)
    calificacion = models.IntegerField(null = True, blank = True)
    sub_categoria = models.TextField()
    proveedor_relacionado = models.IntegerField(null = True, blank = True)
    fecha = models.DateTimeField(auto_now_add=True)

class SubCategoriasCalificacion(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField()
    categoria_principal = models.ForeignKey(CalificacionProveedores, on_delete = models.CASCADE)
    peso = models.IntegerField()
    def __str__(self):
        return self.nombre

class BitacorasRegistro(models.Model):
    id = models.AutoField(primary_key=True)
    entrada = models.TextField()
    Usuario = models.TextField()
    fecha = models.DateField()
    bitacora_relacionada = models.IntegerField(null=True)


class Bitacoras(models.Model):
    id = models.AutoField(primary_key=True)
    tema = models.TextField()
    estado = models.IntegerField()
    fecha = models.DateField()
    usuario = models.IntegerField()


class Temas(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField()
    def __str__(self):
        return self.nombre

class Capacitaciones(models.Model):

    id = models.AutoField(primary_key=True)
    tema = models.ForeignKey(Temas,on_delete=models.SET_NULL, null = True)
    fecha = models.DateField()
    responsable = models.TextField()
    duracion = models.TextField()
    tipo = models.TextField()
    evaluacion = models.TextField()
    sede = models.TextField()
    adjunto = models.FileField(blank = True, null = True,upload_to='Adjunto_Capacitaciones')
    tema_texto = models.TextField("Temas de la Capacitación")
    objetivo = models.TextField()
    evaluacion_texto = models.TextField("Evaluación del Capacitador")
    estado = models.TextField()
    class Meta:
        ordering = ('-fecha',)
class CentroCosto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField()
    def __str__(self):
        return self.nombre



class Documentos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField()
    observaciones = models.TextField()
    tipo = models.TextField()
    adjunto = models.FileField(upload_to='Documentos')


class HojasdeVida(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,blank=True)
    id = models.AutoField(primary_key=True)
    foto = models.ImageField(null = True, blank = True,upload_to = 'fotosHojasVida')
    nombre = models.TextField()
    apellidos = models.TextField()
    tipo_documento = models.TextField()
    documento = models.TextField()
    sexo = models.TextField()
    correo = models.TextField()
    telefono = models.IntegerField()
    lugar_nacimiento = models.TextField()
    direccion_residencia = models.TextField()
    fecha_nacimiento = models.DateField()
    ciudad = models.TextField()
    departamento = models.TextField()
    cargo = models.TextField()
    fecha_ingreso = models.DateField()
    salario = models.TextField()
    numero_cuenta = models.IntegerField()
    tipo_contrato = models.TextField()
    sede = models.TextField()
    rol = models.TextField()
    estado = models.TextField()
    nombre_usuario = models.TextField()
    def __str__(self):
        return self.nombre +' '+ self.apellidos

class DocumentosHojaVida(models.Model):
    hoja_relacionada = models.IntegerField(blank=True)
    descripcion = models.TextField()
    documento = models.FileField(upload_to='Documentos_HojaVida')
    categoria = models.TextField(blank=True)



class AsistenciaCapacitacion(models.Model):
    persona = models.TextField(null =True, blank= True)
    asistencia = models.BooleanField(default=False, blank=False)
    invitacion = models.BooleanField(default=False, blank=False)
    calificacion = models.IntegerField(default = 0,null =True, blank= True)
    capacitacion_relacionada = models.IntegerField(null =True, blank= True)


class Ausentismo(models.Model):
    id = models.AutoField(primary_key=True)
    solicitante = models.TextField()
    solicitado = models.ManyToManyField(HojasdeVida,verbose_name="Solicitar a")
    codigo_enfermedad = models.TextField(null = True, blank = True)
    adjunto = models.FileField(null = True, blank = True,upload_to='Adjuntos_Ausentismo')
    motivo = models.TextField()
    fecha = models.DateField()
    estado = models.TextField(default = "Creada")
    duracion_cantidad = models.TextField(null = True, blank = True)
    duracion_unidad = models.TextField()
    detalle = models.TextField()
    hora_inicio = models.TextField(null = True, blank = True)
    hora_final = models.TextField(null = True, blank = True)

class Requerimiento(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField(default = date.today)
    requerimiento = models.TextField()
    solicita = models.ForeignKey(HojasdeVida, on_delete=models.CASCADE, null=True,related_name='solicitante')
    encargado = models.ForeignKey(HojasdeVida, on_delete=models.CASCADE, null=True,related_name='encargado')
    fecha_planeada = models.DateField()
    plazo = models.DateField()
    plazo_retraso = models.TextField(null = True, blank = True)
    OC = models.TextField(null = True, blank = True)
    fecha_oc = models.DateField(null = True, blank = True)
    cierre_oportuno = models.TextField(null = True, blank = True)
    etapa = models.IntegerField(null = True, blank = True,default = 0)
    dias_cierre = models.IntegerField(null = True, blank = True)
    observaciones = models.TextField(null = True, blank = True)
    sugerencia_proveedor1 = models.TextField(null = True, blank = True)
    sugerencia_proveedor2 = models.TextField(null = True, blank = True)
    sugerencia_proveedor3 = models.TextField(null = True, blank = True)
    resumen =  models.TextField(null = True, blank = True)
    plazo_etapa = models.IntegerField(null = True, blank = True)
class Contratos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField()
    numero = models.IntegerField()

class PlanTrabajo(models.Model):
    id = models.AutoField(primary_key=True)
    actividad = models.TextField()
    periodicidad = models.TextField()
    observaciones = models.TextField()
    contrato_relacionado = models.IntegerField(null = True)

class Productos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField()
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Proveedores(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField()
    telefono = models.IntegerField()
    email = models.TextField()
    ciudad = models.TextField()
    direccion = models.TextField()
    productos_ofrecidos = models.ManyToManyField(Productos,blank=True)
    identificacion = models.IntegerField()
    evaluacion = models.TextField(null=True,blank=True,default ="0")
    tipo_empresa = models.TextField()
    tipo_identificacion = models.TextField()
    ultima_reevaluacion = models.TextField(null=True,blank=True, default ="0")
    clasificacion = models.TextField(null=True,blank=True,default ="0")
    nombre_contacto = models.TextField()
    telefono_contacto = models.IntegerField()
    email_contacto = models.TextField(null=True,blank=True)
    camara_comercio = models.FileField(null=True,blank=True,upload_to='Proveedores_CamaraComercio')
    rut = models.FileField(null=True,blank=True,upload_to='Proveedores_RUT')
    cedula_representante = models.FileField(null=True,blank=True,upload_to='Proveedores_CCRepresentante')
    certificacion_comercial = models.FileField(null=True,blank=True,upload_to='Proveedores_CertificacionComercial')
    certificacion_bancaria = models.FileField(null=True,blank=True,upload_to='Proveedores_CertificacionBancaria')
    sg_sst = models.FileField(null=True,blank=True,upload_to='Proveedores_SGSST')
    iso_9001 = models.FileField(null=True,blank=True,upload_to='Proveedores_ISO9001')
    iso_14001 = models.FileField(null=True,blank=True,upload_to='Proveedores_ISO14001')
    ohsas_180001 = models.FileField(null=True,blank=True,upload_to='Proveedores_OHSAS18001')

    def __str__(self):
        return self.nombre




class Cotizaciones(models.Model):
    id = models.AutoField(primary_key=True)
    proveedor = models.TextField()
    valorantes_iva = models.IntegerField()
    documento = models.FileField(upload_to='Cotizaciones')


class SolicitudesC(models.Model):


    id = models.AutoField(primary_key=True)
    codigo = models.TextField(default = "OCM",null=True,blank=True)
    solicita = models.ForeignKey(HojasdeVida, on_delete=models.CASCADE, null=True,related_name='solicitaid')
    autoriza = models.ForeignKey(HojasdeVida, on_delete=models.CASCADE, null=True,related_name='autorizasolicitud')
    centro_costo =  models.ForeignKey(CentroCosto, on_delete=models.SET_NULL, null=True)
    descripcion = models.TextField(null = True)
    proveedor_1 = models.TextField(null = True)
    proveedor_2 = models.TextField(null = True)
    proveedor_3 = models.TextField(null = True)
    cotizacion_1 = models.FileField(null = True,upload_to='Cotizaciones')
    cotizacion_2 = models.FileField(null = True,upload_to='Cotizaciones')
    cotizacion_3 = models.FileField(null = True,upload_to='Cotizaciones')
    estado = models.TextField(null=True,blank=True)
    fecha = models.DateField(null=True,blank=True)
    cuadro_comparativo = models.FileField(upload_to='Cotizaciones/CuadrosComparativosa')
    justificacion = models.TextField()
    observaciones_autorizacion = models.TextField(null=True,blank=True)
    requerimiento_asociado = models.ForeignKey(Requerimiento,on_delete=models.CASCADE, null = True,blank = True)
    proveedor_seleccionado = models.TextField(null = True,blank = True)

    def __str__(self):
        return self.codigo

class ProductosServicios(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField()
    cantidad = models.IntegerField()
    unidades = models.TextField()
    valor_unitario = models.IntegerField(null = True, blank = True)
    iva = models.IntegerField(null = True, blank = True)
    valor_iva = models.IntegerField(null = True, blank = True)
    valor_total = models.IntegerField(null = True, blank = True)
    solicitud_relacionada = models.IntegerField(blank = True,null = True)
    requerimiento_relacionado = models.IntegerField(blank = True,null = True)
    reembolsable = models.BooleanField()
    calibracion = models.BooleanField()

class ProductosRequerimiento(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField()
    cantidad = models.IntegerField()
    unidades = models.TextField()
    valor_unitario = models.IntegerField(null = True, blank = True)
    iva = models.IntegerField(null = True, blank = True)
    valor_iva = models.IntegerField(null = True, blank = True)
    valor_total = models.IntegerField(null = True, blank = True)
    requerimiento_relacionado = models.IntegerField(blank = True,null = True)
    calibracion = models.BooleanField()
    reembolsable = models.BooleanField()
class OrdenCompra(models.Model):
    id = models.AutoField(primary_key=True)
    codigo =  models.TextField(null = True)
    proveedor = models.TextField(null = True)
    centro_costo = models.ForeignKey(CentroCosto, on_delete=models.SET_NULL, null=True)
    estado = models.TextField(null = True,blank = True)
    cotizacion = models.FileField(null = True,upload_to='Cotizacion_OrdenCompra')
    fecha = models.DateField()
    porcentaje_retefuente = models.IntegerField()
    porcentaje_admin = models.IntegerField()
    porcentaje_imprevistos = models.IntegerField()
    porcentaje_utilidad = models.IntegerField()
    porcentaje_iva_util = models.IntegerField()
    subtotal = models.IntegerField()
    retefuente = models.IntegerField()
    admin = models.IntegerField()
    imprevistos = models.IntegerField()
    utilidad = models.IntegerField()
    iva_util = models.IntegerField()
    total_iva = models.IntegerField()
    total = models.IntegerField()
    recibe = models.ForeignKey(HojasdeVida, on_delete=models.SET_NULL, null = True,related_name='recibeorden')
    observaciones = models.TextField()
    solicitud_relacionada = models.ForeignKey(SolicitudesC,on_delete=models.SET_NULL, null = True, blank = True)



class Correspondencia(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.TextField()
    folios = models.TextField()
    anexos = models.TextField()
    asunto = models.TextField()
    lugar = models.TextField()
    fecha_radicado = models.DateField(default = date.today)
    descripcion = models.TextField()
    nombre = models.TextField()
    correo = models.TextField()
    metodo_envio = models.TextField()
    adjunto = models.FileField()
