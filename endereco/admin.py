from django.contrib import admin
from endereco.models import Endereco

class EnderecoAdmin(admin.ModelAdmin):
    list_display = ['cidade', 'logradouro', 'bairro']
    list_filter = ['cidade']


admin.site.register(Endereco, EnderecoAdmin)

# Register your models here.
