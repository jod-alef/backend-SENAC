from django.contrib import admin
from imoveis.models import Imovel, Inquilino, Aluguel

# Register your models here.
admin.site.register(Imovel)
admin.site.register(Inquilino)
admin.site.register(Aluguel)