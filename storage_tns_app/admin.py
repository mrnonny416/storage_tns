from django.contrib import admin
from . import models

admin.site.site_header = "TNS Storage Admin"
admin.site.site_title = "ยินดีต้อนรับเข้าสู่ระบบจัดการของ Admin"
admin.site.index_title = "TNS Storage Manage Admin"

admin.site.register(models.user)
admin.site.register(models.material)
admin.site.register(models.storage)
admin.site.register(models.equipment)
admin.site.register(models.history)

# Register your models here.
