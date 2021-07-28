from django.contrib import admin

from pessoas.models import Telefone, Pessoa

admin.site.register(Telefone)
admin.site.register(Pessoa)

