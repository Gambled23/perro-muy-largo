from django import forms


opcionesFormReporte =(
    ("1", "Falta de agua"),
    ("2", "Contaminacion de agua"),
    ("3", "Poca cantidad de agua"),
)


class formulario_reporte(forms.Form):
    num_usuario = forms.IntegerField()
    movtivo_reporte = forms.ChoiceField(choices= opcionesFormReporte)

class formulario_contacto(forms.Form):
    email = forms.EmailField()
    asunto = forms.CharField()
    descripcion = forms.CharField(widget=forms.TextInput(attrs={'size':80}))

class formulario_estado_reporte(forms.Form):
    folio_reporte = forms.IntegerField()

class formulario_registrar_usuario(forms.Form):
    #Para crear domicilio
    municipio = forms.CharField(max_length=50) 
    colonia = forms.CharField(max_length=50) 
    calle = forms.CharField(max_length=50) 
    numero = forms.CharField(max_length=5)
    #Para crear usuario
    nombre = forms.CharField(max_length=50) 
    telefono = forms.Field()
   
    