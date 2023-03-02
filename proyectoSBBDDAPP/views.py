from django.shortcuts import render, HttpResponse
from proyectoSBBDDAPP.models import tecnico
from proyectoSBBDD.forms import formulario_reporte
from proyectoSBBDD.forms import formulario_contacto

def home(request):
    return render(request, 'home.html')

def generate_report(request):
    if request.method=='POST': #Qué se hará al usar el metodo post
        miFormulario = formulario_reporte(request.POST) #para que en el formulario venga la informacion que introdujo el usuario en POST
        if miFormulario.is_valid():
            infForm = miFormulario.cleaned_data
            #AQUÍ HACER LO Q SE TENGA Q HACER CON EL FORM
            return render(request, 'gracias.html')
    else:
        miFormulario=formulario_reporte()
        
        #Construir documento html con los datos dentro de miFormulario
    return render(request, 'generate_report.html', {'form': miFormulario}) #le decimos que va a renderizar generate_report.html usando un formulario guardado en miFormulario

def report_status(request):
    return render(request, 'report_status.html')

def about_us(request):
    return render(request, 'about_us.html')

def contact(request):
    if request.method=='POST': #Qué se hará al usar el metodo post
        miFormulario = formulario_contacto(request.POST) #para que en el formulario venga la informacion que introdujo el usuario en POST
        if miFormulario.is_valid():
            infForm = miFormulario.cleaned_data
            #AQUÍ HACER LO Q SE TENGA Q HACER CON EL FORM
            return render(request, 'gracias.html')
    else:
        miFormulario=formulario_contacto()
    return render(request, 'contact.html', {'form': miFormulario})

def faq(request):
    

    return render(request, 'faq.html')