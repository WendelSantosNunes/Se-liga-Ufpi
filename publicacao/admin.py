from django.contrib import admin

from .models import Publicacao

# Register your models here.


class PublicacaoAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


admin.site.register(Publicacao, PublicacaoAdmin)
