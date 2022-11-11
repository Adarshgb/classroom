from django.contrib import admin

# Register your models here.
from onlineapp import models

admin.site.register(models.log)
admin.site.register(models.teacherdata)
admin.site.register(models.studentdata)
admin.site.register(models.studentleave)
admin.site.register(models.noteupload)

