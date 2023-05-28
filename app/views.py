# -*- encoding: utf-8 -*-
from app.models import AsistenciaCapacitacion,DocumentosHojaVida,SubCategoriasCalificacion,CalificacionesProveedores,CalificacionProveedores,ImagenRequerimiento,ProductosRequerimiento,Temas,CentroCosto,ProductosServicios,Requerimiento,Bitacoras, Capacitaciones,HojasdeVida,Ausentismo,BitacorasRegistro,OrdenCompra,Proveedores,SolicitudesC,Contratos,PlanTrabajo,Productos,Correspondencia
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from django.http import HttpResponseRedirect
from .forms import EvaluacionInicialForm,RequerimientosViewForm,CapacitacionEditForm, AusentismoVerForm,AsistenciaFormSetEdit,AsistenciaFormSetHelper,HojaDocumentoForm,AsistenciaFormSet,AusentismoForm,SubcategoriaForm,InicialHelper,CalificacionesProveedoresForm,CalificacionesFormSet,CategoriaForm,SolicitudParcialForm,ProductosRequerimientoForm,ProductosRequerimientoFormSetHelper,RequerimientoFormSet,TemasForm,ProductosFormSetView,ProductosFormSetViewHelper,SolicitudViewForm,ProductosFormSetHelperOrden,CentroCostoForm,ProductosFormSetHelper,ProductosFormSet,RequerimientosForm,CotizacionesForm,BitacoraForm,CapacitacionForm,HojasdeVidaForm,RegistroBitacoraForm, OrdenForm, ProveedoresForm,SolicitudForm,ContratoForm,PlanTrabajoForm,ProductosForm,CorrespondenciaForm
from django.contrib.auth.models import User
from datetime import date,timedelta,datetime
from django.db.models import Q

@login_required(login_url='/login/')
def index(request):

    return render(request, "index.html")

@login_required(login_url='/login/')
def handler404(request, exception, template_name="404.html"):
    response = render_to_response(template_name)
    response.status_code = 404
    return response

@login_required(login_url='/login/')
def getBitacoras(request):


    obj = Bitacoras.objects.all()

    context = {"object":obj}

    return render(request, "tablaBitacoras.html", context)
@login_required(login_url='/login/')
def getRequerimiento(request):


    obj = Requerimiento.objects.all()
    from_date = datetime.now().date()
    for p in obj:
        if ((p.plazo - from_date).days) > 9:
             p.plazo_etapa = 0
        elif 0 <= ((p.plazo - from_date).days) <= 8:
             p.plazo_etapa = 1
        elif 0 > ((p.plazo - from_date).days):
            p.plazo_etapa = 2
    context = {"object":obj,"from_date":from_date}

    return render(request, "tablaRequerimientos.html", context)
@login_required(login_url='/login/')
def getCentroCosto(request):


    obj = CentroCosto.objects.all()

    context = {"object":obj}

    return render(request, "tablaCentroCosto.html", context)
@login_required(login_url='/login/')
def getAusentismo(request):

    usuario = HojasdeVida.objects.get(user = request.user)
    rol = usuario.rol
    print(rol)
    obj = Ausentismo.objects.filter(Q(solicitante = usuario) | Q(solicitado = usuario))
    obj_1 = Ausentismo.objects.all()
    if usuario.rol == "Gerencial":
        context = {"object_1":obj_1,"object":obj,'usuario':usuario,'rol':rol}
        return render(request, "tablaAusentismoGerencial.html", context)

    context = {"object":obj,'usuario':usuario,'rol':rol}
    return render(request, "tablaAusentismo.html", context)
@login_required(login_url='/login/')
def getTemasCapacitacion(request):


    obj = Temas.objects.all()

    context = {"object":obj}

    return render(request, "tablaTemas.html", context)

@login_required(login_url='/login/')
def getCapacitaciones(request):

    obj = Capacitaciones.objects.all()

    context = {"object":obj}

    return render(request, "tablaCapacitaciones.html", context)
@login_required(login_url='/login/')
def getHojaVida(request):


    obj = HojasdeVida.objects.all()

    context = {"object":obj}

    return render(request, "tablaHojaVida.html", context)
@login_required(login_url='/login/')
def getCorrespondencia(request):


    obj = Correspondencia.objects.all()

    context = {"object":obj}

    return render(request, "tablaCorrespondencia.html", context)
@login_required(login_url='/login/')
def getContratos(request):


    obj = Contratos.objects.all()

    context = {"object":obj}

    return render(request, "tablaContratos.html", context)
@login_required(login_url='/login/')
def getOrdenCompra(request):


    obj = OrdenCompra.objects.all()

    context = {"object":obj}

    return render(request, "tablaOrdenCompra.html", context)
@login_required(login_url='/login/')
def getProveedores(request):


    obj = Proveedores.objects.all()

    context = {"object":obj}

    return render(request, "tablaProveedores.html", context)

@login_required(login_url='/login/')
def getSolicitudes(request):


    obj = SolicitudesC.objects.all()
    usuario = HojasdeVida.objects.get(user = request.user)
    context = {"object":obj,"usuario":usuario}

    return render(request, "tablaSolicitudes.html", context)
@login_required(login_url='/login/')
def getProductos(request):


    obj = Productos.objects.all()

    context = {"object":obj}

    return render(request, "tablaProductos.html", context)
@login_required(login_url='/login/')
def getCategorias(request):


    obj = CalificacionProveedores.objects.all()

    context = {"object":obj}

    return render(request, "tablaCalificacion.html", context)
@login_required(login_url='/login/')
def getSubcategorias(request,id_elemento):


    obj =  SubCategoriasCalificacion.objects.filter(categoria_principal=id_elemento)

    context = {"object":obj}

    return render(request, "tablaSubcategorias.html", context)
@login_required(login_url='/login/')
def eliminarBitacora(request,id_elemento):
    elemento = Bitacoras.objects.get(categoria=id_elemento)
    elemento.delete()
    return redirect('/bitacoras')
@login_required(login_url='/login/')
def eliminarAusentismo(request,id_elemento):
    elemento = Ausentismo.objects.get(id=id_elemento)
    elemento.delete()
    return redirect('/ausentismo')
@login_required(login_url='/login/')
def eliminarCategoria(request,id_elemento):
    elemento = CalificacionProveedores.objects.get(id=id_elemento)
    elemento.delete()
    return redirect('/categorias')
@login_required(login_url='/login/')
def eliminarSubcategoria(request,id_elemento):
    elemento = SubCategoriasCalificacion.objects.get(id = id_elemento)
    elemento.delete()
    return redirect('/categorias')

@login_required(login_url='/login/')
def eliminarCapacitacion(request,id_elemento):
    elemento = Capacitaciones.objects.get(pk=id_elemento)
    elemento.delete()
    return redirect('/capacitaciones')
@login_required(login_url='/login/')
def eliminarHojaVida(request,id_elemento):
    elemento = HojasdeVida.objects.get(pk=id_elemento)
    usuario = elemento.user
    usuario.delete()
    elemento.delete()

    return redirect('/hojas-vida')
@login_required(login_url='/login/')
def eliminarContrato(request,id_elemento):
    elemento = Contratos.objects.get(pk=id_elemento)
    elemento.delete()

    return redirect('/contratos')
@login_required(login_url='/login/')
def eliminarProducto(request,id_elemento):
    elemento = Productos.objects.get(pk=id_elemento)
    elemento.delete()

    return redirect('/productos')
@login_required(login_url='/login/')
def eliminarProveedor(request,id_elemento):
    elemento = Proveedores.objects.get(pk=id_elemento)
    elemento.delete()

    return redirect('/proveedores')
@login_required(login_url='/login/')
def addBitacora(request):
    if request.method == 'POST':
      form = BitacoraForm(request.POST)
      print(request.POST)
      form.save()
      return redirect('bitacoras')
    else:
      form = BitacoraForm()
    return render(request, "addBitacora.html", {'form': form})
@login_required(login_url='/login/')

def evaluacionInicial(request, id_elemento):
    form = EvaluacionInicialForm(request.POST)

    if request.method == 'POST':
        form = EvaluacionInicialForm(request.POST)
        form.save()
        proveedor = Proveedores.objects.get(id = id_elemento)
        proveedor.ultima_reevaluacion = date.today()
        proveedor.clasificacion =  (form.cleaned_data['documentos_legales'] * 0.14) + (form.cleaned_data['forma_pago'] * 0.14) + (form.cleaned_data['precio'] * 0.16) \
         + (form.cleaned_data['gestion_cotizaciones'] * 0.14) + (form.cleaned_data['certificaciones_calidad'] * 0.14) + (form.cleaned_data['implementacion_sgsst'] * 0.14) + (form.cleaned_data['documentos_ambientales'] * 0.14)
        proveedor.save()

        return redirect('/proveedores')
    else:

      form = EvaluacionInicialForm()
    return render(request, "addEvaluacionInicial.html", {'form': form})
@login_required(login_url='/login/')
def addProveedores(request):
    form = ProveedoresForm(request.POST)
    if request.method == 'POST' and form.is_valid():
      form.save()
      print(request.POST)
      return redirect('/proveedores')
    else:
      print (form.errors)
      form = ProveedoresForm()
    return render(request, "addProveedores.html", {'form': form})
@login_required(login_url='/login/')
def addAusentismo(request):
    usuario = HojasdeVida.objects.get(user = request.user)
    form = AusentismoForm(request.POST,request.FILES,initial={'solicitante': usuario.nombre + " " +  usuario.apellidos, 'fecha': date.today})
    if request.method == 'POST' and form.is_valid():
      form.save()
      print(request.POST)
      return redirect('/ausentismo')
    else:
      print (form.errors)
      form = AusentismoForm(initial={'solicitante': usuario.nombre + " " +  usuario.apellidos,'fecha': date.today,'duracion_unidad':'Dias','hora_inicio': '00:00','hora_final':'00:00'})
    return render(request, "addAusentismo.html", {'form': form})
@login_required(login_url='/login/')
def addCategoria(request):
    form = CategoriaForm(request.POST)
    if request.method == 'POST' and form.is_valid():
      form.save()

      return redirect('/categorias')
    else:

      form = CategoriaForm()
    return render(request, "addCalificacion.html", {'form': form})
@login_required(login_url='/login/')
def addSubcategoria(request):
    form = SubcategoriaForm(request.POST)
    if request.method == 'POST' and form.is_valid():
      form.save()
      print(form.errors)

      return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    else:
      form = SubcategoriaForm()
    return render(request, "addSubcategoria.html", {'form': form})

@login_required(login_url='/login/')
def addProducto(request):
    form = ProductosForm(request.POST)
    if request.method == 'POST' and form.is_valid():
      form.save()
      return redirect('/productos')
    else:
      form = ProductosForm()
    return render(request, "addProductos.html", {'form': form})
@login_required(login_url='/login/')
def addTema(request):
    form = TemasForm(request.POST)
    if request.method == 'POST' and form.is_valid():
      form.save()
      return redirect('/temasCapacitacion')
    else:
      form = TemasForm()
    return render(request, "addTema.html", {'form': form})
@login_required(login_url='/login/')
def addCentroCosto(request):
    form = CentroCostoForm(request.POST)
    if request.method == 'POST' and form.is_valid():
      form.save()
      return redirect('/requerimientos')
    else:
      form = CentroCostoForm()
    return render(request, "addCentroCosto.html", {'form': form})
@login_required(login_url='/login/')
def addRequerimiento(request):
    helper = ProductosFormSetHelper()
    form = RequerimientosForm(request.POST,request.FILES)
    formset = ProductosFormSet(request.POST,queryset=ProductosServicios.objects.none())
    if request.method == 'POST' and formset.is_valid():

      form.save()
      requerimiento = Requerimiento.objects.last()
      requerimiento.etapa = "1"
      requerimiento.save()
      imagenes = request.FILES.getlist('imagenes')
      for imagen in imagenes:
          foto = ImagenRequerimiento.objects.create(imagen = imagen, requerimiento_relacionado =requerimiento.id )

      for form in formset:

          child = form.save(commit = False)
          child.requerimiento_relacionado = requerimiento.id
          child.save()
      return redirect('/requerimientos')
    else:

      formset = ProductosFormSet(queryset=ProductosServicios.objects.none())
      form = RequerimientosForm(initial = {'fecha': date.today,'plazo':datetime.now()+timedelta(days=30)})
    return render(request, "addRequerimiento.html", {'form': form,'formset': formset,'helper': helper})
@login_required(login_url='/login/')
def addSolicitud(request):
    helper = ProductosFormSetHelper()
    form = SolicitudForm(request.POST,request.FILES)
    formset = ProductosFormSet(request.POST,queryset=ProductosServicios.objects.none())
    if request.method == 'POST' and formset.is_valid():
      form.save()
      solicitud = SolicitudesC.objects.last()
      for form in formset:

          child = form.save(commit = False)
          child.solicitud_relacionada = solicitud.id
          child.save()



      solicitud.codigo = "OCM" + str(solicitud.id)
      solicitud.estado = "Creada"
      solicitud.fecha = datetime.today()

      solicitud.save()
      return redirect('/solicitud')
    else:

      formset = ProductosFormSet(queryset=ProductosServicios.objects.none())
      form = SolicitudForm()
    return render(request, "addSolicitud.html",{'form': form,'formset': formset,'helper': helper})
@login_required(login_url='/login/')
def editarSolicitud(request,id):
    solicitud = SolicitudesC.objects.get(id = id)
    fecha = solicitud.fecha
    estado = solicitud.estado
    helper = ProductosFormSetHelper()
    form = SolicitudForm(request.POST,request.FILES,instance = solicitud)
    formset = ProductosFormSet(request.POST,queryset=ProductosServicios.objects.filter(solicitud_relacionada = id))

    if request.method == 'POST' and formset.is_valid():
      form.save()
      for form in formset:

          child = form.save(commit = False)
          child.solicitud_relacionada = id
          child.save()
      solicitud.fecha = fecha
      solicitud.estado = estado
      solicitud.estado = "Creada"
      solicitud.save()
      return redirect('/solicitud')
    else:

      formset = ProductosFormSet(queryset=ProductosServicios.objects.filter(solicitud_relacionada = id))
      form = SolicitudForm(instance = solicitud)
    return render(request, "addSolicitud.html",{'form': form,'formset': formset,'helper': helper})

@login_required(login_url='/login/')
def viewSolicitud(request,id):
    solicitud = SolicitudesC.objects.get(id = id)
    helper = ProductosFormSetViewHelper()
    form = SolicitudViewForm(instance = solicitud)
    formset = ProductosFormSetView(queryset=ProductosServicios.objects.filter(solicitud_relacionada=id))

    return render(request, "viewSolicitud.html",{'form': form,'formset': formset,'helper': helper})

def viewRequerimiento(request,id):
    requerimiento = Requerimiento.objects.get(id = id)
    helper = ProductosFormSetViewHelper()
    form = RequerimientosViewForm(instance = requerimiento)
    formset = ProductosFormSetView(queryset=ProductosServicios.objects.filter(requerimiento_relacionado=id))

    return render(request, "viewRequerimiento.html",{'form': form,'formset': formset,'helper': helper})
@login_required(login_url='/login/')
def generarSolicitud(request,id):
    helper = ProductosFormSetHelper()
    obj = Requerimiento.objects.get(id = id)
    form = SolicitudForm(request.POST,request.FILES,initial={'solicita': obj.solicita, 'autoriza': obj.encargado,'proveedor_1': obj.sugerencia_proveedor1,'proveedor_2': obj.sugerencia_proveedor2,'proveedor_3': obj.sugerencia_proveedor3})
    formset = ProductosFormSet(request.POST,queryset=ProductosServicios.objects.filter(requerimiento_relacionado = id))
    if request.method == 'POST' and formset.is_valid():
      form.save()
      solicitud = SolicitudesC.objects.last()
      for form in formset:
          child = form.save(commit = False)
          child.solicitud_relacionada = solicitud.id
          child.requerimiento_relacionado = obj.id
          child.save()

      solicitud.codigo = "OCM" + str(solicitud.id)
      solicitud.estado = "Creada"
      solicitud.fecha = datetime.today()
      solicitud.requerimiento_asociado = obj
      solicitud.save()
      obj.etapa = 2
      obj.save()
      return redirect('/solicitud')
    else:
      formset = ProductosFormSet(queryset=ProductosServicios.objects.filter(requerimiento_relacionado = id))
      form = SolicitudForm(initial={'solicita': obj.solicita, 'autoriza': obj.encargado,'proveedor_1': obj.sugerencia_proveedor1,'proveedor_2': obj.sugerencia_proveedor2,'proveedor_3': obj.sugerencia_proveedor3})

    return render(request, "addSolicitud.html",{'form': form,'formset': formset,'helper': helper})
@login_required(login_url='/login/')
def generarOrden(request,id):
    helper = ProductosFormSetHelperOrden()
    obj = SolicitudesC.objects.get(id = id)
    if obj.proveedor_seleccionado == obj.proveedor_1:
        cotizacion = obj.cotizacion_1
    elif obj.proveedor_seleccionado == obj.proveedor_2:
        cotizacion = obj.cotizacion_2
    else:
        cotizacion = obj.cotizacion_3
    form = OrdenForm(request.POST,request.FILES,initial={'recibe': obj.solicita,'proveedor': obj.proveedor_seleccionado,'cotizacion':cotizacion,'centro_costo':obj.centro_costo})
    formset = ProductosFormSet(request.POST,queryset=ProductosServicios.objects.filter(solicitud_relacionada = id))
    if request.method == 'POST' and formset.is_valid():
      parent = form.save(commit = False)
      parent.solicitud_relacionada = obj
      parent.estado = "Creada"
      parent.save()
      orden = OrdenCompra.objects.last()
      orden.codigo = "OC" + str(orden.id)
      orden.save()
      obj.estado = "Generada"
      obj.save()
      for form in formset:
          child = form.save(commit = False)
          child.solicitud_relacionada = obj.id
          child.save()

      requerimiento = obj.requerimiento_asociado
      requerimiento.etapa = 4
      requerimiento.save()
      return redirect('/ordenes')
    else:

        form = OrdenForm(initial={'recibe': obj.solicita,'proveedor': obj.proveedor_seleccionado,'cotizacion':cotizacion,'centro_costo':obj.centro_costo})
        formset = ProductosFormSet(queryset=ProductosServicios.objects.filter(solicitud_relacionada = id))

    return render(request, "addOrden.html",{'form': form,'formset': formset,'helper': helper})
@login_required(login_url='/login/')
def addOrden(request):
    if request.method == 'POST':
      form = OrdenForm(request.POST)
      print(request.POST)
      form.save()
      return redirect('/ordenes')
    else:
      form = OrdenForm()
    return render(request, "addOrden.html", {'form': form})
@login_required(login_url='/login/')
def addCorrespondencia(request):
    if request.method == 'POST':
      form = CorrespondenciaForm(request.POST,request.FILES)
      form.save()
      print(request.POST)
      return redirect('/correspondencia')
    else:
      form = CorrespondenciaForm()
      print(form.errors)

    return render(request, "addCorrespondencia.html", {'form': form})

@login_required(login_url='/login/')
def addContrato(request):
    if request.method == 'POST':
      form = ContratoForm(request.POST)
      form.save()
      return redirect('/contratos')
    else:
      form = ContratoForm()
    return render(request, "addContrato.html", {'form': form})
@login_required(login_url='/login/')
def addDocumentoHojaVida(request,id_elemento):
    if request.method == 'POST':
      form = HojaDocumentoForm(request.POST,request.FILES)

      temp = form.save(commit = False)
      temp.hoja_relacionada = id_elemento
      temp.save()
      return redirect('/documentosHoja'+ "/" + id_elemento)
    else:
      form = HojaDocumentoForm()
    return render(request, "addDocHoja.html", {'form': form})

@login_required(login_url='/login/')
def addTTHojaVida(request,id_elemento):
    if request.method == 'POST':
      form = HojaDocumentoForm(request.POST,request.FILES)

      temp = form.save(commit = False)
      temp.hoja_relacionada = id_elemento
      temp.categoria = "TTHH"
      temp.save()
      return redirect('/documentosTTHH'+ "/" + id_elemento)
    else:
      form = HojaDocumentoForm()
    return render(request, "addDocHoja.html", {'form': form})

def addSegSocial(request,id_elemento):
    if request.method == 'POST':
      form = HojaDocumentoForm(request.POST,request.FILES)

      temp = form.save(commit = False)
      temp.hoja_relacionada = id_elemento
      temp.categoria = "SegSocial"
      temp.save()
      return redirect('/documentosSegSocial'+ "/" + id_elemento)
    else:
      form = HojaDocumentoForm()
    return render(request, "addDocHoja.html", {'form': form})

def addSegSalud(request,id_elemento):
    if request.method == 'POST':
      form = HojaDocumentoForm(request.POST,request.FILES)

      temp = form.save(commit = False)
      temp.hoja_relacionada = id_elemento
      temp.categoria = "SegSalud"
      temp.save()
      return redirect('/documentosSegSalud'+ "/" + id_elemento)
    else:
      form = HojaDocumentoForm()
    return render(request, "addDocHoja.html", {'form': form})

def addNomina(request,id_elemento):
    if request.method == 'POST':
      form = HojaDocumentoForm(request.POST,request.FILES)

      temp = form.save(commit = False)
      temp.hoja_relacionada = id_elemento
      temp.categoria = "Nomina"
      temp.save()
      return redirect('/documentosNomina'+ "/" + id_elemento)
    else:
      form = HojaDocumentoForm()
    return render(request, "addDocHoja.html", {'form': form})

def addHojaVidaDoc(request,id_elemento):
    if request.method == 'POST':
      form = HojaDocumentoForm(request.POST,request.FILES)

      temp = form.save(commit = False)
      temp.hoja_relacionada = id_elemento
      temp.categoria = "HojaVida"
      temp.save()
      return redirect('/documentosHojaVida'+ "/" + id_elemento)
    else:
      form = HojaDocumentoForm()
    return render(request, "addDocHoja.html", {'form': form})

@login_required(login_url='/login/')
def addCapacitacion(request):
    HojasVida = HojasdeVida.objects.all()
    formset = AsistenciaFormSet(queryset = AsistenciaCapacitacion.objects.none())
    juntas = zip(HojasVida,formset)
    if request.method == 'POST':
      helper = AsistenciaFormSetHelper()
      formset = AsistenciaFormSet(request.POST)
      form = CapacitacionForm(request.POST,request.FILES)
      print(request.POST)
      form.save()
      ultima_capacitacion = Capacitaciones.objects.last().id
      for a,b in zip(HojasVida,formset):
            print(b.errors)
            child = b.save(commit = False)
            child.persona = a.nombre + " " + a.apellidos
            child.capacitacion_relacionada = ultima_capacitacion

            child.save()

      return redirect('capacitaciones')
    else:
      helper = AsistenciaFormSetHelper()
      formset = AsistenciaFormSet(queryset = AsistenciaCapacitacion.objects.none())
      form = CapacitacionForm()
    return render(request, "addCapacitacion.html", {'form': form,'formset': formset,'HojasVida': HojasVida,"helper":helper,'juntas':juntas})
@login_required(login_url='/login/')
def editarCapacitacion(request,id_elemento):
    HojasVida = HojasdeVida.objects.all()
    capacitacion = Capacitaciones.objects.get(id=id_elemento)
    helper = AsistenciaFormSetHelper()
    form = CapacitacionEditForm(request.POST,request.FILES,instance = capacitacion)
    formset = AsistenciaFormSetEdit(request.POST,queryset = AsistenciaCapacitacion.objects.filter(capacitacion_relacionada = id_elemento))

    if request.method == 'POST':

        form.save()
        for form in formset:
            child = form.save(commit = False)
            child.capacitacion_relacionada = id_elemento
            child.save()
        return redirect('capacitaciones')
    else:
      helper = AsistenciaFormSetHelper()
      formset = AsistenciaFormSetEdit(queryset = AsistenciaCapacitacion.objects.filter(capacitacion_relacionada = id_elemento))
      form = CapacitacionEditForm(instance = capacitacion)

    return render(request, "editarCapacitacion.html", {'form': form,'formset': formset,"helper":helper,'HojasVida':HojasVida})
@login_required(login_url='/login/')
def addHojaVida(request):
    form = HojasdeVidaForm(request.POST,request.FILES)
    if request.method == 'POST' and form.is_valid():
      print(form.errors)
      cleaned_data = form.cleaned_data
      usuario = cleaned_data.get('nombre_usuario')
      password = cleaned_data.get('password')
      user = User.objects.create_user(usuario, '', password)
      form.save()
      HojaV = HojasdeVida.objects.order_by('-pk')[0]
      UsuarioLink = User.objects.get(username=usuario)
      HojaV.user = UsuarioLink
      HojaV.save()
      return redirect('hojas-vida')
    else:
      print(form.errors)
      form = HojasdeVidaForm()
    return render(request, "addHojaVida.html", {'form': form})
@login_required(login_url='/login/')
def getDocumentosHojaVida(request,id_elemento):
    obj = DocumentosHojaVida.objects.filter(hoja_relacionada = id_elemento)

    nombre_apellido = HojasdeVida.objects.get(id=id_elemento).nombre + " " +  HojasdeVida.objects.get(id=id_elemento).apellidos
    context = {"object":obj,"nombre":nombre_apellido,"id":id_elemento}

    return render(request, "tablaDocumentosHoja.html", context)

@login_required(login_url='/login/')
def getSegSalud(request,id_elemento):
    obj = DocumentosHojaVida.objects.filter(hoja_relacionada = id_elemento,categoria = "SegSalud")

    nombre_apellido = HojasdeVida.objects.get(id=id_elemento).nombre + " " +  HojasdeVida.objects.get(id=id_elemento).apellidos
    context = {"object":obj,"nombre":nombre_apellido,"id":id_elemento}

    return render(request, "tablaSalud.html", context)

@login_required(login_url='/login/')
def getNomina(request,id_elemento):
    obj = DocumentosHojaVida.objects.filter(hoja_relacionada = id_elemento,categoria = "Nomina")

    nombre_apellido = HojasdeVida.objects.get(id=id_elemento).nombre + " " +  HojasdeVida.objects.get(id=id_elemento).apellidos
    context = {"object":obj,"nombre":nombre_apellido,"id":id_elemento}

    return render(request, "tablaNomina.html", context)

@login_required(login_url='/login/')
def getTTHH(request,id_elemento):
    obj = DocumentosHojaVida.objects.filter(hoja_relacionada = id_elemento,categoria = "TTHH")

    nombre_apellido = HojasdeVida.objects.get(id=id_elemento).nombre + " " +  HojasdeVida.objects.get(id=id_elemento).apellidos
    context = {"object":obj,"nombre":nombre_apellido,"id":id_elemento}

    return render(request, "tablaTTHH.html", context)

@login_required(login_url='/login/')
def getHojaVidaDoc(request,id_elemento):
    obj = DocumentosHojaVida.objects.filter(hoja_relacionada = id_elemento,categoria = "HojaVida")

    nombre_apellido = HojasdeVida.objects.get(id=id_elemento).nombre + " " +  HojasdeVida.objects.get(id=id_elemento).apellidos
    context = {"object":obj,"nombre":nombre_apellido,"id":id_elemento}

    return render(request, "tablaDocumentosHojaVida.html", context)

@login_required(login_url='/login/')
def getSegSocial(request,id_elemento):
    obj = DocumentosHojaVida.objects.filter(hoja_relacionada = id_elemento,categoria = "SegSocial")

    nombre_apellido = HojasdeVida.objects.get(id=id_elemento).nombre + " " +  HojasdeVida.objects.get(id=id_elemento).apellidos
    context = {"object":obj,"nombre":nombre_apellido,"id":id_elemento}

    return render(request, "tablaSegSocial.html", context)

@login_required(login_url='/login/')
def enviarOrden(request,id):
      orden = OrdenCompra.objects.get(id=id)
      orden.estado = "Pendiente por Recibir"
      orden.save()
      return redirect('/ordenes')
@login_required(login_url='/login/')
def evaluarOrden(request,id):
      orden = OrdenCompra.objects.get(id=id)
      orden.estado = "Cerrada"
      r = OrdenCompra.solicitud_relacionada
      m = r.requerimiento_asociado
      m.etapa = "5"
      m.save()
      orden.save()
      return redirect('/ordenes')
@login_required(login_url='/login/')
def recibirOrden(request,id):
      orden = OrdenCompra.objects.get(id=id)
      orden.estado = "Pendiente por Evaluar"
      orden.save()
      return redirect('/ordenes')
@login_required(login_url='/login/')
def registroBitacora(request,id_elemento):


    obj = BitacorasRegistro.objects.filter(bitacora_relacionada=id_elemento)
    context = {"object":obj,"id":id_elemento}

    return render(request, "tablaRegistroBitacora.html", context)
@login_required(login_url='/login/')
def addRegistroBitacora(request,id_elemento):
    if request.method == 'POST':
      form = RegistroBitacoraForm(request.POST)
      form.save()
      Registro = BitacorasRegistro.objects.order_by('-pk')[0]
      Registro.bitacora_relacionada = id_elemento
      Registro.usuario = request.user.get_username()
      Registro.save()
      return redirect('/registroBitacora/' + id_elemento)
    else:
      form = RegistroBitacoraForm(request.POST)
    return render(request, "addBitacoraRegistro.html", {'form': form})
@login_required(login_url='/login/')
def addPlanTrabajo(request,id_elemento):
    if request.method == 'POST':
      form.save()
      Registro = PlanTrabajo.objects.order_by('-pk')[0]
      Registro.contrato_relacionado = id_elemento
      Registro.save()
      return redirect('/planTrabajo/' + id_elemento)
    else:
      form = PlanTrabajoForm(request.POST)
    return render(request, "addPlanTrabajo.html", {'form': form})

@login_required(login_url='/login/')
def editarProveedor(request,id_elemento):
    proveedor = Proveedores.objects.get(id = id_elemento)
    form = ProveedoresForm(instance=proveedor)
    if request.method == 'POST':
        form = ProveedoresForm(request.POST,instance=proveedor)
        if form.is_valid():
            form.save()
            return redirect('/proveedores')
    return render(request, "addProveedores.html", {'form': form})
@login_required(login_url='/login/')
def verAusentismo(request,id_elemento):
    ausentismo = Ausentismo.objects.get(id = id_elemento)
    print(ausentismo.solicitado.all().first())
    form = AusentismoVerForm(instance=ausentismo, initial = {"solicitado":ausentismo.solicitado.all().first()})
    if request.method == 'POST':
        form = AusentismoVerForm(request.POST,instance=ausentismo)

    return render(request, "verAusentismo.html", {'form': form})
@login_required(login_url='/login/')
def editarContrato(request,id_elemento):
    contrato = Contratos.objects.get(id = id_elemento)
    form = ContratoForm(instance=contrato)
    if request.method == 'POST':
        form = ContratoForm(request.POST,instance=contrato)
        if form.is_valid():
            form.save()
            return redirect('/contratos')
    return render(request, "addContrato.html", {'form': form})
@login_required(login_url='/login/')
def editarSubcategoria(request,id_elemento):
    subcategoria = SubCategoriasCalificacion.objects.get(id = id_elemento)
    form = SubcategoriaForm(instance=subcategoria)
    if request.method == 'POST':
        form = SubcategoriaForm(request.POST,instance=subcategoria)
        if form.is_valid():
            form.save()
            return redirect('/categorias')
    return render(request, "addSubcategoria.html", {'form': form})
@login_required(login_url='/login/')
def editarCategoria(request,id_elemento):
    categoria = CalificacionProveedores.objects.get(id = id_elemento)
    form = CategoriaForm(instance=categoria)
    if request.method == 'POST':
        form = CategoriaForm(request.POST,instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('/categorias')
    return render(request, "addCalificacion.html", {'form': form})
@login_required(login_url='/login/')
def editarHojaVida(request,id_elemento):
    hoja = HojasdeVida.objects.get(id = id_elemento)
    form = HojasdeVidaForm(instance=hoja)
    if request.method == 'POST':
        form = HojasdeVidaForm(request.POST,request.FILES,instance=hoja)
        if form.is_valid():
            form.save()
            return redirect('/hojas-vida')
    return render(request, "addHojaVida.html", {'form': form})
@login_required(login_url='/login/')
def editarProducto(request,id_elemento):
    producto = Productos.objects.get(id = id_elemento)
    form = ProductosForm(instance=producto)
    if request.method == 'POST':
        form = ProductosForm(request.POST,instance=producto)
        if form.is_valid():
            form.save()
            return redirect('/productos')
    return render(request, "addProductos.html", {'form': form})
@login_required(login_url='/login/')
def verCorrespondencia(request,id_elemento):
    correspondencia = Correspondencia.objects.get(id = id_elemento)
    form = CorrespondenciaForm(instance=correspondencia)
    if request.method == 'POST':
        form = CorrespondenciaForm(request.POST,instance=correspondencia)
        if form.is_valid():
            form.save()
            return redirect('/correspondencia')
    return render(request, "addCorrespondencia.html", {'form': form})
@login_required(login_url='/login/')
def planTrabajo(request,id_elemento):


    obj = PlanTrabajo.objects.filter(contrato_relacionado=id_elemento)
    nombre = Contratos.objects.get(id = id_elemento).nombre
    context = {"object":obj,"nombre":nombre,"id":id_elemento}

    return render(request, "tablaPlanTrabajo.html", context)


@login_required(login_url='/login/')
def aprobarSolicitud(request,id_elemento):
    solicitud = SolicitudesC.objects.get(codigo = id_elemento)
    d = solicitud.requerimiento_asociado
    d.etapa = "3"
    d.save()
    form = SolicitudParcialForm(request.POST,instance=solicitud)
    #solicitud.estado = "Aprobado"
    #solicitud.save()

    if request.method == 'POST':
        form = SolicitudParcialForm(request.POST,instance=solicitud)
        print(form.errors)
        if form.is_valid():
            print(form.errors)
            form.save()
            solicitud.estado = "Aprobado"
            solicitud.save()
            return redirect('/solicitud')

    return render(request, "seleccionProveedor.html",{'codigo':id_elemento,'form':form,'proveedor1': solicitud.proveedor_1,'proveedor2': solicitud.proveedor_2,'proveedor3': solicitud.proveedor_3})
@login_required(login_url='/login/')
def aprobarAusentismo(request,id_elemento):
    ausentismo = Ausentismo.objects.get(id = id_elemento)
    ausentismo.estado = "Aprobado"
    ausentismo.save()

    return redirect('/ausentismo')
@login_required(login_url='/login/')
def autorizarAusentismo(request,id_elemento):
    ausentismo = Ausentismo.objects.get(id = id_elemento)
    ausentismo.estado = "Autorizado"
    ausentismo.save()

    return redirect('/ausentismo')
@login_required(login_url='/login/')
def aprobarSolicitudBackup(request,id_elemento):
    solicitud = SolicitudesC.objects.get(codigo = id_elemento)
    solicitud.estado = "Aprobado"
    solicitud.save()

    return redirect('/solicitud')
