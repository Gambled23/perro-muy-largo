from django.contrib import admin

from proyectoSBBDDAPP.models import domicilio, usuario, tecnico, reporte

# Register your models here.

class domicilioAdmin(admin.ModelAdmin):
    list_display=('codigo_domicilio','calle','colonia','numero','municipio')
    search_fields=['codigo_domicilio']
    list_filter=('colonia',)

class usuarioAdmin(admin.ModelAdmin):
    list_display=('codigo_domicilio','nombre','codigo_cliente','telefono')
    search_fields=['codigo_cliente']

class tecnicoAdmin(admin.ModelAdmin):
    list_display=('codigo_tecnico','nombre')

class reporteAdmin(admin.ModelAdmin):
    list_display=('folio','estado_reporte','codigo_cliente','codigo_tecnico')
    search_fields=['codigo_tecnico']
    list_filter=('estado_reporte', 'codigo_tecnico',)

admin.site.register(domicilio, domicilioAdmin)
admin.site.register(usuario, usuarioAdmin)
admin.site.register(reporte, reporteAdmin)
admin.site.register(tecnico, tecnicoAdmin)
