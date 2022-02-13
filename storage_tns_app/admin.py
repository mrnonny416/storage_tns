from django.contrib import admin
from . import models

admin.site.register(models.user)
admin.site.register(models.material)
admin.site.register(models.equipment)
admin.site.register(models.history)

# Register your models here.
