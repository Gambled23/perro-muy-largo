from django.shortcuts import render, HttpResponse
from proyectoSBBDDAPP.models import tecnico
from proyectoSBBDD.forms import formulario_reporte, formulario_contacto, formulario_estado_reporte, formulario_registrar_usuario
from proyectoSBBDDAPP.models import reporte, usuario, tecnico, domicilio, registros

def home(request):
    context  = {
        'test' : 'xd'
    }
    return render(request, 'home.html', context)

def generate_report(request):
    if request.method=='POST': #Qué se hará al usar el metodo post
        formularioCrearReporte = formulario_reporte(request.POST) #para que en el formulario venga la informacion que introdujo el usuario en POST
        if formularioCrearReporte.is_valid():
            infForm = formularioCrearReporte.cleaned_data
            motivo_reporte = infForm['movtivo_reporte']
            cod_cliente = infForm['num_usuario']
            #Guardar reporte en BD
            tecnicoBD = tecnico.objects.all()
            usuarioBD = usuario.objects.get(codigo_cliente=cod_cliente)
            rep = reporte(motivo_reporte=motivo_reporte, codigo_cliente=usuarioBD, codigo_tecnico=tecnicoBD[0]) #ostia puta q hice aqui q crack
                #cod_cliente-1 funca pq los datos se guardan en serial auto
                #jaja trolleado no funciona
            rep.save()
            folio_reporte = reporte.objects.latest('folio')
            context = {
                'motivo_reporte' : motivo_reporte,
                'folio_reporte' : folio_reporte.folio,
            }
            return render(request, 'generated_report.html', context)
    else:
        formularioCrearReporte=formulario_reporte()
        
        #Construir documento html con los datos dentro de formularioCrearReporte
    return render(request, 'generate_report.html', {'form': formularioCrearReporte}) #le decimos que va a renderizar generate_report.html usando un formulario guardado en formularioCrearReporte

def report_status(request):
    if request.method=='POST': #Qué se hará al usar el metodo post
        formularioConsultarReporte = formulario_estado_reporte(request.POST) #para que en el formulario venga la informacion que introdujo el usuario en POST
        if formularioConsultarReporte.is_valid():
            infForm = formularioConsultarReporte.cleaned_data
            #Guardar consulta en tabla registros
            reg = registros(folio=infForm['folio_reporte'])
            reg.save()

            #Buscar consulta en BD
            folio_reporte = infForm['folio_reporte']
            reporteConsultado = reporte.objects.get(folio=folio_reporte)
            context = {
                'reporte' : reporteConsultado,
            }
            return render(request, 'report_found.html', context)
    else:
        formularioConsultarReporte=formulario_estado_reporte()
        
        #Construir documento html con los datos dentro de formularioCrearReporte
    return render(request, 'report_status.html', {'form': formularioConsultarReporte})

def about_us(request):
    return render(request, 'about_us.html')

def contact(request):
    if request.method=='POST': #Qué se hará al usar el metodo post
        formularioCrearReporte = formulario_contacto(request.POST) #para que en el formulario venga la informacion que introdujo el usuario en POST
        if formularioCrearReporte.is_valid():
            infForm = formularioCrearReporte.cleaned_data
            #AQUÍ HACER LO Q SE TENGA Q HACER CON EL FORM
            return render(request, 'gracias.html')
    else:
        formularioCrearReporte=formulario_contacto()
    return render(request, 'contact.html', {'form': formularioCrearReporte})

def faq(request):
    

    return render(request, 'faq.html')

def test(request):

    return render(request, 'test.html')

def register_user(request):
    if request.method=='POST': 
        formularioRegistrarUsuario = formulario_registrar_usuario(request.POST)
        if formularioRegistrarUsuario.is_valid():
            infForm = formularioRegistrarUsuario.cleaned_data
            #Crear domicilio
            dom = domicilio(calle=infForm['calle'], colonia=infForm['colonia'], numero=infForm['numero'], municipio=infForm['municipio'])
            dom.save()

            #Crear usuario
            #Obtener ultimo domicilio creado
            ultimoDomicilio = domicilio.objects.latest('codigo_domicilio')

            usr = usuario(nombre=infForm['nombre'], telefono=infForm['telefono'], codigo_domicilio=ultimoDomicilio)
            usr.save()
            ultimoUsuario = usuario.objects.latest('codigo_cliente')
            codCliente = ultimoUsuario.codigo_cliente
            userCTX = usuario.objects.get(codigo_cliente=codCliente)
            context = {
                'usuario' : userCTX,
            }
            return render(request, 'user_registered.html', context)
    else:
        formularioRegistrarUsuario=formulario_registrar_usuario()
    return render(request, 'register_user.html', {'form': formularioRegistrarUsuario})