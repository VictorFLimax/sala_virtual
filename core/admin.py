from django.contrib import admin

from core import models


# Register your models here.
@admin.register(models.Anexo)
class AnexoAdmin(admin.ModelAdmin):
    list_display = ('id','nome', 'tipo', 'caminho_anexo', 'servidor','created_at', 'modified_at', 'active')
    search_fields = ('id','nome', 'tipo', 'caminho_anexo', 'servidor','created_at', 'modified_at', 'active')


