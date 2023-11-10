from django.contrib import admin
from core import models
from users.models import User


admin.site.register(models.Inquerito)
admin.site.register(models.IdentificacaoAggFamiliar)
admin.site.register(models.CaracteristicasAggFamiliar)
admin.site.register(User)
