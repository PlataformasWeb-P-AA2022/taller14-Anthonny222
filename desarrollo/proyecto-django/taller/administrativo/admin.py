from django.contrib import admin

from administrativo.models import Propietario, Departamento


class PropietarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'edad', 'nacionalidad')
    search_fields = ('nombre', 'edad')

admin.site.register(Propietario, PropietarioAdmin)


class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('costo', 'cuartos', 'banio', 'valor')
    search_fields = ('Propietario',)

admin.site.register(Departamento, DepartamentoAdmin)
