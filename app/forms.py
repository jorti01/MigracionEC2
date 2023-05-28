from django import forms
from .models import EvaluacionesSeleccion,DocumentosHojaVida,AsistenciaCapacitacion,Ausentismo,SubCategoriasCalificacion,CalificacionesProveedores,CalificacionProveedores,ImagenRequerimiento,ProductosRequerimiento,Temas,CentroCosto,Cotizaciones,Bitacoras,Capacitaciones,HojasdeVida,BitacorasRegistro,OrdenCompra,Proveedores,SolicitudesC,Contratos,PlanTrabajo,Productos,Correspondencia,ProductosServicios,Requerimiento
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper,Layout
from crispy_forms.layout import Layout, Submit, Row, Column, ButtonHolder, HTML,Div
from django_select2 import forms as s2forms
from django.forms import TextInput
from django.forms import modelformset_factory
from string import Template
from django.utils.safestring import mark_safe
from django.forms import ImageField, SelectMultiple,formset_factory, ModelChoiceField,HiddenInput
from django.conf import settings
from crispy_forms.layout import Field





class CustomImageField(Field):
    template = 'image_thumbnail.html'

class ImagenForm(forms.ModelForm):

    class Meta:
        model = ImagenRequerimiento
        fields = ('imagen',)

class PictureWidget(forms.widgets.Widget):
    def render(self, name, value, attrs=None, **kwargs):
        html =  Template("""<img src="$link"/>""")
        return mark_safe(html.substitute(link=value))

class UserProfileForm(forms.ModelForm):
    photo = ImageField(widget=PictureWidget)

class DateInput(forms.DateInput):
    input_type = 'date'

class BitacoraForm(forms.ModelForm):

    class Meta:
        model = Bitacoras
        fields = ('tema', 'estado', 'fecha', 'usuario',)
        widgets = {
            'fecha': DateInput(attrs={'type': 'date'})
        }

class RegistroBitacoraForm(forms.ModelForm):

    class Meta:
        model = BitacorasRegistro
        fields = ('entrada', 'fecha')
        widgets = {
            'fecha': DateInput(attrs={'type': 'date'})
        }

class CategoriaForm(forms.ModelForm):
    categoria = forms.CharField()
    class Meta:
        model = CalificacionProveedores
        fields = '__all__'

class AusentismoForm(forms.ModelForm):
    codigo_enfermedad = forms.CharField(required=False)
    solicitante = forms.CharField()
    duracion_cantidad = forms.CharField(required=False)
    hora_inicio = forms.TimeField(required=False )
    hora_final = forms.TimeField(required=False)
    motivo = forms.ChoiceField(choices= (("Accidente de Trabajo","Accidente de Trabajo"),("Enfermedad Laboral","Enfermedad Laboral"),("Enfermedad Común","Enfermedad Común"),("Licencia de Maternidad","Licencia de Maternidad"),("Ley Maria","Ley Maria"),("Cita Medica","Cita Medica"),("Ejercicio Sufragio","Ejercicio Sufragio"),("Dias Compensatorios","Dias Compensatorios"),("Calamidad","Calamidad"),("Personal","Personal"),("Otro","Otro")))
    duracion_unidad = forms.ChoiceField(choices= (("Horas","Horas"),("Dias","Dias")))
    class Meta:
        model = Ausentismo
        fields = ('motivo','adjunto','solicitante', 'solicitado', 'fecha','duracion_cantidad','duracion_unidad','detalle','hora_inicio','hora_final','codigo_enfermedad')
        widgets = {
                    'fecha': DateInput(attrs={'type': 'date'},format="%m/%d/%Y"),

                }
    def __init__(self, *args, **kwargs):
        super(AusentismoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Guardar', css_class='btn-primary'))
        self.helper.layout = Layout(

                              Row(Column('solicitante',css_class='form-group col-md-6 mb-0'),
                              Column('solicitado', css_class='form-group col-md-6 mb-0',multiple="multiple"),),


                              Row(Column('adjunto',css_class='form-group col-md-4 mb-0'),
                              Column('fecha', css_class='form-group col-md-4 mb-0',multiple="multiple"),
                              Column('motivo', css_class='form-group col-md-4 mb-0',multiple="multiple")
                              ),


                              Row(Column('duracion_cantidad',css_class='form-group col-md-6 mb-0'),
                              Column('duracion_unidad', css_class='form-group col-md-6 mb-0',multiple="multiple"),),


                              Row(Column('codigo_enfermedad',css_class='form-group col-md-4 mb-0'),
                              Column('hora_inicio',css_class='form-group col-md-4 mb-0'),
                              Column('hora_final',css_class='form-group col-md-4 mb-0'),
                              ),

                              Row(Column('detalle',css_class='form-group col-md-12 mb-0'),
                              )
                              )

        #self.fields['solicitante'].disabled = True

class AusentismoVerForm(forms.ModelForm):
    codigo_enfermedad = forms.CharField(required=False)
    solicitante = forms.CharField()
    solicitado = forms.CharField()
    fecha = forms.DateField(
        widget=forms.widgets.DateInput(format="%m/%d/%Y"))
    duracion_cantidad = forms.CharField(required=False)
    hora_inicio = forms.TimeField(required=False )
    hora_final = forms.TimeField(required=False)
    motivo = forms.ChoiceField(choices= (("Accidente de Trabajo","Accidente de Trabajo"),("Enfermedad Laboral","Enfermedad Laboral"),("Enfermedad Común","Enfermedad Común"),("Licencia de Maternidad","Licencia de Maternidad"),("Ley Maria","Ley Maria"),("Cita Medica","Cita Medica"),("Ejercicio Sufragio","Ejercicio Sufragio"),("Dias Compensatorios","Dias Compensatorios"),("Calamidad","Calamidad"),("Personal","Personal"),("Otro","Otro")))
    duracion_unidad = forms.ChoiceField(choices= (("Horas","Horas"),("Dias","Dias")))
    class Meta:
        model = Ausentismo
        fields = ('motivo','adjunto','solicitante', 'solicitado', 'fecha','duracion_cantidad','duracion_unidad','detalle','hora_inicio','hora_final','codigo_enfermedad')

    def __init__(self, *args, **kwargs):
        super(AusentismoVerForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(

                              Row(Column('solicitante',css_class='form-group col-md-6 mb-0'),
                              Column('solicitado', css_class='form-group col-md-6 mb-0',multiple="multiple"),),


                              Row(Column('adjunto',css_class='form-group col-md-4 mb-0'),
                              Column('fecha', css_class='form-group col-md-4 mb-0',multiple="multiple"),
                              Column('motivo', css_class='form-group col-md-4 mb-0',multiple="multiple")
                              ),


                              Row(Column('duracion_cantidad',css_class='form-group col-md-6 mb-0'),
                              Column('duracion_unidad', css_class='form-group col-md-6 mb-0',multiple="multiple"),),


                              Row(Column('codigo_enfermedad',css_class='form-group col-md-4 mb-0'),
                              Column('hora_inicio',css_class='form-group col-md-4 mb-0'),
                              Column('hora_final',css_class='form-group col-md-4 mb-0'),
                              ),

                              Row(Column('detalle',css_class='form-group col-md-12 mb-0'),
                              )
                              )

        self.fields['solicitante'].disabled = True

class SubcategoriaForm(forms.ModelForm):
    nombre = forms.CharField()
    class Meta:
        model = SubCategoriasCalificacion
        fields = '__all__'
class CapacitacionForm(forms.ModelForm):
    adjunto = forms.FileField(required= False)
    fecha = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS )
    responsable = forms.CharField()
    duracion = forms.CharField()
    tipo = forms.ChoiceField(choices= (("Practico","Practico"),("Teórica","Teórica"),("Teórica/Practica","Teórica/Practica"),("Virtual","Virtual")))
    evaluacion = forms.ChoiceField(choices= (("Escrita","Escrita"),("Oral","Oral"),("Practica","Practica"),("N/A","N/A")))
    sede = forms.CharField()
    estado = forms.ChoiceField(choices= (("Programada","Programada"),("Reprogramada","Reprogramada"),("Ejecutada","Ejecutada"),("Cancelada","Cancelada")))
    class Meta:
        model = Capacitaciones
        fields = '__all__'
        widgets = {
            'fecha': DateInput(attrs={'type': 'date'})
        }
    def __init__(self, *args, **kwargs):
        super(CapacitacionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(

                              Row(Column('tema',css_class='form-group col-md-6 mb-0'),
                              Column('fecha',css_class='form-group col-md-6 mb-0'),


                              ),
                              Row(Column('responsable',css_class='form-group col-md-4 mb-0'),
                              Column('duracion',css_class='form-group col-md-4 mb-0'),
                              Column('tipo',css_class='form-group col-md-4 mb-0'),


                              ),
                              Row(Column('evaluacion',css_class='form-group col-md-4 mb-0'),
                              Column('sede',css_class='form-group col-md-4 mb-0'),
                              Column('estado',css_class='form-group col-md-4 mb-0'),
                              ),
                              Row(Column('adjunto',css_class='form-group col-md-4 mb-0'),
                              ),
                              Row(Column('tema_texto',css_class='form-group col-md-6 mb-0'),
                              Column('objetivo',css_class='form-group col-md-6 mb-0'),
                              ),
                              Row(
                              Column('evaluacion_texto',css_class='form-group col-md-12 mb-0'),
                              ),

                                )

class CapacitacionEditForm(forms.ModelForm):
    adjunto = forms.FileField(required= False)
    fecha = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS )
    responsable = forms.CharField()
    duracion = forms.CharField()
    tipo = forms.ChoiceField(choices= (("Practico","Practico"),("Teórica","Teórica"),("Teórica/Practica","Teórica/Practica"),("Virtual","Virtual")))
    evaluacion = forms.ChoiceField(choices= (("Escrita","Escrita"),("Oral","Oral"),("Practica","Practica"),("N/A","N/A")))
    sede = forms.CharField()
    estado = forms.ChoiceField(choices= (("Programada","Programada"),("Reprogramada","Reprogramada"),("Ejecutada","Ejecutada"),("Cancelada","Cancelada")))
    class Meta:
        model = Capacitaciones
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CapacitacionEditForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(

                              Row(Column('tema',css_class='form-group col-md-6 mb-0'),
                              Column('fecha',css_class='form-group col-md-6 mb-0'),


                              ),
                              Row(Column('responsable',css_class='form-group col-md-4 mb-0'),
                              Column('duracion',css_class='form-group col-md-4 mb-0'),
                              Column('tipo',css_class='form-group col-md-4 mb-0'),


                              ),
                              Row(Column('evaluacion',css_class='form-group col-md-4 mb-0'),
                              Column('sede',css_class='form-group col-md-4 mb-0'),
                              Column('estado',css_class='form-group col-md-4 mb-0'),
                              ),
                              Row(Column('adjunto',css_class='form-group col-md-4 mb-0'),
                              ),
                              Row(Column('tema_texto',css_class='form-group col-md-6 mb-0'),
                              Column('objetivo',css_class='form-group col-md-6 mb-0'),
                              ),
                              Row(
                              Column('evaluacion_texto',css_class='form-group col-md-12 mb-0'),
                              ),

                                )

class HojasdeVidaForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    nombre = forms.CharField()
    apellidos = forms.CharField()
    foto = forms.ImageField()
    documento = forms.CharField()
    correo = forms.CharField()
    sexo = forms.CharField()
    lugar_nacimiento = forms.CharField()
    tipo_documento = forms.ChoiceField(choices= (("Cedula Ciudadania","Cedula Ciudadania"),("Cedula de Extranjeria","Cedula de Extranjeria"),("Pasaporte","Pasaporte")))
    direccion_residencia = forms.CharField()
    ciudad = forms.CharField()
    departamento = forms.CharField()
    cargo = forms.CharField()
    tipo_contrato = forms.ChoiceField(choices= (("Termino Indefinido ","Termino Indefinido"),("Termino Fijo","Termino Fijo"),("Obra/Labor","Obra/Labor")))
    salario = forms.CharField()
    sede = forms.CharField()
    nombre_usuario = forms.CharField()
    password = forms.CharField(required = False)
    rol =  forms.ChoiceField(choices= (("Gerencial","Gerencial"),("Administrador","Administrador"),("Lider/Coordinador","Lider/Coordinador"),("Asistente TTHH","Asistente TTHH"),("Asistente Admon","Asistente Admon"),("Tecnico","Tecnico"),("Ayudante","Ayudante"),("Auxiliar","Auxiliar"),("Obrero/Recorredor","Obrero/Recorredor")))
    estado = forms.ChoiceField(choices = (("Activo","Activo"),("Inactivo","Inactivo")))
    class Meta:

        model = HojasdeVida
        fields ='__all__'
        widgets = {
            'fecha_nacimiento': DateInput(attrs={'type': 'date'},format=('%Y-%m-%d')),
            'fecha_ingreso': DateInput(attrs={'type': 'date'},format=('%Y-%m-%d')),
                }
    def __init__(self, *args, **kwargs):
        super(HojasdeVidaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Guardar', css_class='btn-primary'))
        self.helper.layout = Layout(

                              Row(Column(css_class='form-group col-md-4 mb-0'),
                              Column(CustomImageField('foto'), css_class='form-group col-md-4 mb-0 '),
                              ),
                              Row(Column('nombre',css_class='form-group col-md-4 mb-0'),
                              Column('apellidos',css_class='form-group col-md-4 mb-0'),
                              Column('tipo_documento',css_class='form-group col-md-4 mb-0'),
                              ),
                              Row(
                              Column('documento',css_class='form-group col-md-4 mb-0'),
                              Column('correo',css_class='form-group col-md-4 mb-0'),
                              Column('telefono',css_class='form-group col-md-4 mb-0'),

                              ),

                              Row(Column('sexo',css_class='form-group col-md-4 mb-0'),
                              Column('lugar_nacimiento',css_class='form-group col-md-4 mb-0'),
                              Column('fecha_nacimiento',css_class='form-group col-md-4 mb-0'),
                              ),
                              Row(Column('direccion_residencia',css_class='form-group col-md-4 mb-0'),
                              Column('ciudad',css_class='form-group col-md-4 mb-0'),
                              Column('departamento',css_class='form-group col-md-4 mb-0'),
                              ),
                              HTML("""
                              </div>
    <div class="card card-primary">
<div class="card-header">
<h3 class="card-title">Ingreso</h3>
</div>
                              """),
                              Row(Column('cargo',css_class='form-group col-md-4 mb-0'),
                              Column('fecha_ingreso',css_class='form-group col-md-4 mb-0'),
                              Column('tipo_contrato',css_class='form-group col-md-4 mb-0'),
                              ),
                              Row(Column('salario',css_class='form-group col-md-4 mb-0'),
                              Column('numero_cuenta',css_class='form-group col-md-4 mb-0'),
                              Column('sede',css_class='form-group col-md-4 mb-0'),
                              ),
                              HTML("""
                              """),
                                HTML("""
                                </div>
      <div class="card card-primary">
  <div class="card-header">
  <h3 class="card-title">Ingreso a VIA</h3>
  </div>
                                """),
                                Row(Column('nombre_usuario',css_class='form-group col-md-4 mb-0'),
                                Column('password',css_class='form-group col-md-4 mb-0'),
                                Column('rol',css_class='form-group col-md-4 mb-0'),
                                ),
                                Row(Column(css_class='form-group col-md-4 mb-0'),
                                Column('estado',css_class='form-group col-md-4 mb-0'),
                                Column(css_class='form-group col-md-4 mb-0'),
                                ),
                                HTML("""</div>
                                """)

        )




class OrdenForm(forms.ModelForm):
    proveedor = forms.CharField()
    codigo = forms.CharField(required=False)
    estado = forms.CharField(required=False)
    class Meta:
        model = OrdenCompra
        fields ='__all__'
        widgets = {
                'fecha': DateInput(attrs={'type': 'date'}),
                }
    def __init__(self, *args, **kwargs):
        super(OrdenForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Guardar', css_class='btn-primary'))
        self.helper.layout = Layout(
                              Row(Column(css_class='form-group col-md-2 mb-0'),
                              Column(css_class='form-group col-md-2 mb-0'),
                              Column(css_class='form-group col-md-4 mb-0'),
                              Column('subtotal', css_class='form-group col-md-2 mb-0'),
                              ),
                             Row(Column( css_class='form-group col-md-2 mb-0'),
                             Column('porcentaje_retefuente', css_class='form-group col-md-2 mb-0'),
                             Column( css_class='form-group col-md-4 mb-0'),
                             Column('retefuente', css_class='form-group col-md-2 mb-0'),
                             ),
                             Row(Column( css_class='form-group col-md-2 mb-0'),
                             Column('porcentaje_admin', css_class='form-group col-md-2 mb-0'),
                             Column(css_class='form-group col-md-4 mb-0'),
                             Column('admin', css_class='form-group col-md-2 mb-0'),
                             ),
                             Row(Column(css_class='form-group col-md-2 mb-0'),
                             Column('porcentaje_imprevistos', css_class='form-group col-md-2 mb-0'),
                             Column( css_class='form-group col-md-4 mb-0'),
                             Column('imprevistos', css_class='form-group col-md-2 mb-0'),
                             ),
                              Row(Column(css_class='form-group col-md-2 mb-0'),
                              Column('porcentaje_utilidad', css_class='form-group col-md-2 mb-0'),
                              Column(css_class='form-group col-md-4 mb-0'),
                              Column('utilidad', css_class='form-group col-md-2 mb-0'),
                              ),
                              Row(Column( css_class='form-group col-md-2 mb-0'),
                              Column('porcentaje_iva_util', css_class='form-group col-md-2 mb-0'),
                              Column(css_class='form-group col-md-4 mb-0'),
                              Column('iva_util', css_class='form-group col-md-2 mb-0'),
                              ),
                              Row(Column(css_class='form-group col-md-2 mb-0'),
                              Column(css_class='form-group col-md-2 mb-0'),
                              Column(css_class='form-group col-md-4 mb-0'),
                              Column('total_iva', css_class='form-group col-md-2 mb-0'),
                              ),
                              Row(Column(css_class='form-group col-md-2 mb-0'),
                              Column(css_class='form-group col-md-2 mb-0'),
                              Column(css_class='form-group col-md-4 mb-0'),
                              Column('total', css_class='form-group col-md-2 mb-0'),
                              ),
                              HTML("""                      <div class="card card-primary">
                  <div class="card-header">
                  <h3 class="card-title">Responsables</h3>
                  </div>




                         """),
                          Row(Column('recibe', css_class='form-group col-md-6 mb-0'),
                          ),
                          HTML("""
                                       </div>
                          """),
                          'observaciones',
        )


class ProveedoresForm(forms.ModelForm):
    nombre = forms.CharField()
    identificacion = forms.CharField()
    evaluacion = forms.CharField()
    ultima_reevaluacion = forms.CharField()
    clasificacion = forms.CharField()
    ciudad = forms.CharField()
    email = forms.CharField()
    tipo_empresa = forms.ChoiceField(choices= (("Persona Natural","Persona Natural"),("Persona Juridica","Persona Juridica")))
    tipo_identificacion = forms.ChoiceField(choices= (("Cedula Ciudadania","Cedula Ciudadania"),("NIT","NIT"),("RUT","RUT"),("Cedula de Extranjeria","Cedula de Extranjeria"),("Pasaporte","Pasaporte")))
    nombre_contacto = forms.CharField()
    evaluacion = forms.CharField(required=False)
    ultima_reevaluacion = forms.CharField(required=False)
    clasificacion = forms.CharField(required=False)
    email_contacto = forms.CharField()
    direccion = forms.CharField()
    productos_ofrecidos =  forms.ModelMultipleChoiceField(
        queryset=Productos.objects.all())

    class Meta:
        model = Proveedores
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(ProveedoresForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Guardar', css_class='btn-primary'))
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
                     HTML("""

                <!-- left column -->

                <!-- general form elements -->
                <div class="card card-primary">
                  <div class="card-header">
                    <h3 class="card-title">Datos Empresa</h3>
                  </div>
                  <!-- /.card-header -->
                  <!-- form start -->

                    <div class="card-body">


                     """),
                     Row(Column('nombre', css_class='form-group col-md-4 mb-0'),
                     Column('tipo_empresa', css_class='form-group col-md-4 mb-0'),
                     Column('tipo_identificacion', css_class='form-group col-md-4 mb-0'),),

                     Row(Column('identificacion', css_class='form-group col-md-4 mb-0'),
                     Column('ciudad', css_class='form-group col-md-4 mb-0'),
                     Column('direccion', css_class='form-group col-md-4 mb-0'),),

                     Row(Column('telefono', css_class='form-group col-md-4 mb-0'),
                     Column('email', css_class='form-group col-md-4 mb-0'),
                     Column('productos_ofrecidos', css_class='form-group col-md-4 mb-0',multiple="multiple"),),

                     HTML("""  </div>

                                <!-- /.card -->






                                </div>

                                <!-- general form elements -->
                                <div class="card card-primary">
                                <div class="card-header">
                                <h3 class="card-title">Persona Contacto</h3>
                                </div>
                                <!-- /.card-header -->
                                <!-- form start -->

                                <div class="card-body">
                                """),
                                Row(Column('nombre_contacto', css_class='form-group col-md-4 mb-0'),
                                    Column('telefono_contacto', css_class='form-group col-md-4 mb-0'),
                                    Column('email_contacto', css_class='form-group col-md-4 mb-0'),),
                                HTML("""
                                          </div>
                                                    </div>
                                        <div class="card card-primary">
                                        <div class="card-header">
                                        <h3 class="card-title">Documentos Basicos</h3>
                                        </div>
                                        <!-- /.card-header -->
                                        <!-- form start -->

                                        <div class="card-body">"""),
                            Row(Column('camara_comercio', css_class='form-group col-md-4 mb-0'),
                                Column('rut', css_class='form-group col-md-4 mb-0'),
                                Column('cedula_representante', css_class='form-group col-md-4 mb-0'),),
                            Row(Column('certificacion_comercial', css_class='form-group col-md-4 mb-0'),
                                Column('certificacion_bancaria', css_class='form-group col-md-4 mb-0'),
                                Column('sg_sst', css_class='form-group col-md-4 mb-0'),),
                            Row(Column('iso_9001', css_class='form-group col-md-4 mb-0'),
                                Column('iso_14001', css_class='form-group col-md-4 mb-0'),
                                Column('ohsas_180001', css_class='form-group col-md-4 mb-0'),),

                                )




class SolicitudViewForm(forms.ModelForm):
    codigo = forms.CharField(required=False)
    estado = forms.CharField(required=False)



    class Meta:
        model = SolicitudesC
        fields = '__all__'
        widgets = {
                'fecha': DateInput(attrs={'type': 'date'}),
                }

    def __init__(self, *args, **kwargs):
        super(SolicitudViewForm, self).__init__(*args, **kwargs)
        for nam, field in self.fields.items():
            field.disabled = True
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
                     HTML("""
                    <div class="card card-primary">
          <div class="card-header">
            <h3 class="card-title">Datos Solicitud</h3>
          </div>
          <!-- /.card-header -->
          <!-- form start -->

            <div class="card-body">
                """),
            'centro_costo',
            Row(
                Column('solicita', css_class='form-group col-md-6 mb-0'),
                Column('autoriza', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'descripcion',

                    HTML("""

                   <div class="card card-primary">
               <div class="card-header">
               <h3 class="card-title">Selección de Proveedor</h3>
               </div>
               <!-- /.card-header -->
               <!-- form start -->

               <div class="card-body">
               """),
                'cuadro_comparativo',
                'justificacion',
            HTML("""
      </div>
       </div>"""
            ))

class SolicitudParcialForm(forms.ModelForm):
    proveedor_seleccionado = forms.CharField(required = False)

    class Meta:
        model = SolicitudesC
        fields = ('proveedor_seleccionado',)


class HojaDocumentoForm(forms.ModelForm):
    descripcion = forms.CharField()
    class Meta:
        model = DocumentosHojaVida
        fields = ('descripcion','documento')
    def __init__(self, *args, **kwargs):
        super(HojaDocumentoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Guardar', css_class='btn-primary'))
        self.helper.form_method = 'POST'


class SolicitudForm(forms.ModelForm):
    codigo = forms.CharField(required=False)
    estado = forms.CharField(required=False)
    proveedor_1 = forms.CharField()
    proveedor_2 = forms.CharField()
    proveedor_3 = forms.CharField()
    proveedor_seleccionado = forms.CharField(required = False)

    class Meta:
        model = SolicitudesC
        fields = '__all__'
        widgets = {
                'fecha': DateInput(attrs={'type': 'date'}),
                }

    def __init__(self, *args, **kwargs):
        super(SolicitudForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
                     HTML("""
                    <div class="card card-primary">
          <div class="card-header">
            <h3 class="card-title">Datos Solicitud</h3>
          </div>
          <!-- /.card-header -->
          <!-- form start -->

            <div class="card-body">
                """),
            'centro_costo',
            Row(
                Column('solicita', css_class='form-group col-md-6 mb-0'),
                Column('autoriza', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'descripcion',

                    HTML("""

                   <div class="card card-primary">
               <div class="card-header">
               <h3 class="card-title">Selección de Proveedor</h3>
               </div>
               <!-- /.card-header -->
               <!-- form start -->

               <div class="card-body">
               """),
               Row(
                   Column('proveedor_1', css_class='form-group col-md-4 mb-0'),
                   Column('proveedor_2', css_class='form-group col-md-4 mb-0'),
                   Column('proveedor_3', css_class='form-group col-md-4 mb-0'),
                   css_class='form-row'
               ),
               Row(
                   Column('cotizacion_1', css_class='form-group col-md-4 mb-0'),
                   Column('cotizacion_2', css_class='form-group col-md-4 mb-0'),
                   Column('cotizacion_3', css_class='form-group col-md-4 mb-0'),
                   css_class='form-row'
               ),
                'cuadro_comparativo',
                'justificacion',
            HTML("""
      </div>
       </div>"""
            ))

class PlanTrabajoForm(forms.ModelForm):
        actividad = forms.CharField()
        periodicidad = forms.CharField()
        observaciones = forms.CharField()
        class Meta:
            model = PlanTrabajo
            fields = ["actividad","periodicidad","observaciones"]


class ContratoForm(forms.ModelForm):
    nombre = forms.CharField()
    class Meta:
        model = Contratos
        fields = ["nombre","numero"]

class ProductosForm(forms.ModelForm):
    nombre = forms.CharField()
    descripcion = forms.CharField()
    class Meta:
        model = Productos
        fields = ["nombre","descripcion"]

class TemasForm(forms.ModelForm):
    nombre = forms.CharField()

    class Meta:
        model = Temas
        fields = "__all__"

class CentroCostoForm(forms.ModelForm):
    nombre = forms.CharField()

    class Meta:
        model = CentroCosto
        fields = ["nombre"]
class CotizacionesForm(forms.ModelForm):

    class Meta:
        model = Cotizaciones
        fields = "__all__"

class RequerimientosViewForm(forms.ModelForm):
    sugerencia_proveedor1 = forms.CharField()
    sugerencia_proveedor2 = forms.CharField()
    sugerencia_proveedor3 = forms.CharField()
    resumen = forms.CharField(widget=forms.TextInput(attrs={'class':'special', 'size': '80'}))
    class Meta:
        model = Requerimiento
        fields = "__all__"
        widgets = {
            'fecha': DateInput(attrs={'type': 'date'},format=('%Y-%m-%d')),
            'fecha_planeada': DateInput(attrs={'type': 'date'}),
            'plazo': DateInput(attrs={'type': 'date'},format=('%Y-%m-%d')),
            'fecha_oc': DateInput(attrs={'type': 'date'}),

        }
    def __init__(self, *args, **kwargs):
        super(RequerimientosViewForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.fields['sugerencia_proveedor1'].label = "Sug Proveedor 1"
        self.fields['sugerencia_proveedor2'].label = "Sug Proveedor 2"
        self.fields['sugerencia_proveedor3'].label = "Sug Proveedor 3"
        self.fields['requerimiento'].label = "Justificación del Requerimiento"
        for nam, field in self.fields.items():
            field.disabled = True
        self.helper.layout = Layout(
            Row(
                Column('fecha', css_class='form-group col-md-4 mb-0'),
                Column('fecha_planeada', css_class='form-group col-md-4 mb-0'),
                Column('plazo', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            'requerimiento',
            Row(
                Column('solicita', css_class='form-group col-md-6 mb-0'),
                Column('encargado', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'observaciones',
            )

class RequerimientosForm(forms.ModelForm):
    sugerencia_proveedor1 = forms.CharField()
    sugerencia_proveedor2 = forms.CharField()
    sugerencia_proveedor3 = forms.CharField()
    resumen = forms.CharField(widget=forms.TextInput(attrs={'class':'special', 'size': '80'}))
    class Meta:
        model = Requerimiento
        fields = "__all__"
        widgets = {
            'fecha': DateInput(attrs={'type': 'date'},format=('%Y-%m-%d')),
            'fecha_planeada': DateInput(attrs={'type': 'date'}),
            'plazo': DateInput(attrs={'type': 'date'},format=('%Y-%m-%d')),
            'fecha_oc': DateInput(attrs={'type': 'date'}),

        }
    def __init__(self, *args, **kwargs):
        super(RequerimientosForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.fields['sugerencia_proveedor1'].label = "Sug Proveedor 1"
        self.fields['sugerencia_proveedor2'].label = "Sug Proveedor 2"
        self.fields['sugerencia_proveedor3'].label = "Sug Proveedor 3"
        self.fields['requerimiento'].label = "Justificación del Requerimiento"
        self.fields['fecha'].disabled = True
        self.helper.layout = Layout(
            Row(
                Column('fecha', css_class='form-group col-md-4 mb-0'),
                Column('fecha_planeada', css_class='form-group col-md-4 mb-0'),
                Column('plazo', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            'requerimiento',
            Row(
                Column('solicita', css_class='form-group col-md-6 mb-0'),
                Column('encargado', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'observaciones',
            )



class CorrespondenciaForm(forms.ModelForm):

    nombre = forms.CharField()
    tipo = forms.ChoiceField(choices= (("Entrante","Entrante"),("Saliente","Saliente")))
    correo = forms.CharField()
    metodo_envio = forms.ChoiceField(choices= (("Correo","Correo"),("Otro medio","Otro medio")))
    folios = forms.CharField()
    anexos = forms.CharField()
    asunto = forms.CharField()
    lugar = forms.ChoiceField(choices= (("Superior","Superior"),("Lateral","Lateral")))

    class Meta:
        model = Correspondencia
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(CorrespondenciaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Guardar', css_class='btn-primary'))
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Row(
                Column('tipo', css_class='form-group col-md-4 mb-0'),
                Column('folios', css_class='form-group col-md-4 mb-0'),
                Column('anexos', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            'asunto',
            Row(
                Column('lugar', css_class='form-group col-md-4 mb-0'),
                Column('fecha_radicado', css_class='form-group col-md-4 mb-0'),
                Column('adjunto', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            'descripcion',
             HTML("""
            <div class="card card-primary">
  <div class="card-header">
    <h3 class="card-title">Datos Destinatario</h3>
  </div>
  <!-- /.card-header -->
  <!-- form start -->

    <div class="card-body">
        """),
        Row(
            Column('nombre', css_class='form-group col-md-4 mb-0'),
            Column('correo', css_class='form-group col-md-4 mb-0'),
            Column('metodo_envio', css_class='form-group col-md-4 mb-0'),
            css_class='form-row'
        ),
        )


class ProductosServiciosForm(forms.ModelForm):

    id = forms.IntegerField(required = False)
    nombre = forms.CharField()
    unidades = forms.CharField()

    class Meta:
        model = ProductosServicios
        fields = "__all__"
    def __init__(self, *args, **kwargs):
        super(ProductosServiciosForm, self).__init__(*args, **kwargs)
        self.fields['valor_unitario'].label = "Valor Unitario Estimado"
        self.fields['calibracion'].label = "Requiere calibración"
        self.fields['reembolsable'].label = "Es un reembolsable"
class InicialHelper(FormHelper):

    def __init__(self, *args, **kwargs):
        super(InicialHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_method = 'post'
        self.layout = Layout(
            Row(
                Column('categoria', css_class='form-group col-md-6 mb-0'),
                Column('sub_categoria', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            )
        self.form_tag = False

class CalificacionesProveedoresForm(forms.ModelForm):
    id = forms.IntegerField(required = False)
    sub_categoria = ModelChoiceField(queryset=SubCategoriasCalificacion.objects.all())
    proveedor_relacionado = forms.IntegerField(required = False)


    def __init__(self, *args, **kwargs):
        super(CalificacionesProveedoresForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Row(
                Column('categoria', css_class='form-group col-md-4 mb-0'),
                Column('sub_categoria', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            )
        self.form_tag = False
    class Meta:
        model = CalificacionesProveedores
        fields = "__all__"
        widgets = {
            'categoria': SelectMultiple(),
        }

class EvaluacionInicialForm(forms.ModelForm):

    class Meta:
        model = EvaluacionesSeleccion
        fields = "__all__"
        widgets = {
            'fecha': DateInput(attrs={'type': 'date'})
        }
    def __init__(self, *args, **kwargs):
        super(EvaluacionInicialForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_method = 'POST'
        self.fields['documentos_legales'].label = "Documentos Legales"
        self.fields['forma_pago'].label = "Forma de Pago"
        self.fields['precio'].label = "Precio"
        self.fields['gestion_cotizaciones'].label = "Gestion Cotizaciones"
        self.fields['certificaciones_calidad'].label = "Certificaciones de Calidad"
        self.fields['implementacion_sgsst'].label = "Implementacion del SG-SST"
        self.fields['documentos_ambientales'].label = "Documentos Ambientales"
        self.helper.layout = Layout(
            Row(
                Column('documentos_legales', css_class='form-group col-md-4 mb-0'),
                Column('forma_pago', css_class='form-group col-md-4 mb-0'),
                Column('precio', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('gestion_cotizaciones', css_class='form-group col-md-4 mb-0'),
                Column('certificaciones_calidad', css_class='form-group col-md-4 mb-0'),
                Column('implementacion_sgsst', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column( css_class='form-group col-md-4 mb-0'),
                Column('documentos_ambientales', css_class='form-group col-md-4 mb-0'),
                Column( css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),

            )

class ProductosViewServiciosForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductosViewServiciosForm, self).__init__(*args, **kwargs)
        for nam, field in self.fields.items():
            field.disabled = True
    id = forms.IntegerField(required = False)
    nombre = forms.CharField()
    unidades = forms.CharField()
    class Meta:
        model = ProductosServicios
        fields = "__all__"


CalificacionesFormSet = formset_factory(CalificacionesProveedoresForm, extra = CalificacionProveedores.objects.all().count())
ProductosFormSet = modelformset_factory(ProductosServicios, form = ProductosServiciosForm,extra=0)
ProductosFormSetView = modelformset_factory(ProductosServicios, form = ProductosViewServiciosForm,extra=0)
class ProductosFormSetHelper(FormHelper):

    def __init__(self, *args, **kwargs):
        super(ProductosFormSetHelper, self).__init__(*args, **kwargs)

        self.layout = Layout(
        Row(
        Column('nombre', css_class='form-group col-md-2 mb-0'),
        Column('cantidad', css_class='form-group col-md-2 mb-0'),
        Column('unidades', css_class='form-group col-md-2 mb-0'),
        Column('valor_unitario', css_class='form-group col-md-2 mb-0'),
        Column('calibracion', css_class='form-group col-md-2 mb-0'),
        Column('reembolsable', css_class='form-group col-md-2 mb-0'),)

        )
        self.form_tag = False

class ProductosFormSetViewHelper(FormHelper):

    def __init__(self, *args, **kwargs):
        super(ProductosFormSetViewHelper, self).__init__(*args, **kwargs)
        self.layout = Layout(
        Row(
        Column('nombre', css_class='form-group col-md-4 mb-0'),
        Column('cantidad', css_class='form-group col-md-4 mb-0'),
        Column('unidades', css_class='form-group col-md-4 mb-0'),)

        )
        self.form_tag = False
class ProductosFormSetHelperOrden(FormHelper):

    def __init__(self, *args, **kwargs):
        super(ProductosFormSetHelperOrden, self).__init__(*args, **kwargs)
        self.layout = Layout(
        Row(
        Column('nombre', css_class='form-group col-md-5 mb-0'),
        Column('cantidad', css_class='form-group col-md-1 mb-0'),
        Column('unidades', css_class='form-group col-md-1 mb-0'),
        Column('valor_unitario', css_class='form-group col-md-1 mb-0'),
        Column('iva', css_class='form-group col-md-1 mb-0'),
        Column('valor_iva', css_class='form-group col-md-1 mb-0'),
        Column('valor_total', css_class='form-group col-md-1 mb-0'),)
        )
        self.form_tag = False

class ProductosRequerimientoForm(forms.ModelForm):

    id = forms.IntegerField(required = False)
    nombre = forms.CharField()
    unidades = forms.CharField()

    class Meta:
        model = ProductosRequerimiento
        fields = "__all__"

RequerimientoFormSet = modelformset_factory(ProductosRequerimiento, form = ProductosRequerimientoForm,extra=0)

class ProductosRequerimientoFormSetHelper(FormHelper):

    def __init__(self, *args, **kwargs):
        super(ProductosRequerimientoFormSetHelper, self).__init__(*args, **kwargs)
        self.layout = Layout(
        Row(
        Column('nombre', css_class='form-group col-md-2 mb-0'),
        Column('cantidad', css_class='form-group col-md-2 mb-0'),
        Column('unidades', css_class='form-group col-md-2 mb-0'),
        Column('valor_unitario', css_class='form-group col-md-2 mb-0'),
        Column('reembolsable', css_class='form-group col-md-2 mb-0'),
        Column('calibracion', css_class='form-group col-md-2 mb-0')
        )

        )
        self.form_tag = False


class AsistenciaForm(forms.ModelForm):
    calificacion = forms.ChoiceField(choices=(
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (5, "5"),),required = False)

    class Meta:
        model = AsistenciaCapacitacion
        fields = "__all__"
        widgets = { 'persona': forms.TextInput(attrs={'size': 60})}


AsistenciaFormSet = modelformset_factory(AsistenciaCapacitacion, form = AsistenciaForm,extra=HojasdeVida.objects.all().count())
AsistenciaFormSetEdit = modelformset_factory(AsistenciaCapacitacion, form = AsistenciaForm,extra=0)
class AsistenciaFormSetHelper(FormHelper):

    def __init__(self, *args, **kwargs):
        super(AsistenciaFormSetHelper, self).__init__(*args, **kwargs)
        self.layout = Layout(
        Row(
        Column('asistencia'),
        ))
        self.form_tag = False
