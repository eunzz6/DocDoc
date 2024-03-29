from django.contrib import admin

# Register your models here.
from .models import Person, Submit

class PesonAdmin(admin.ModelAdmin):
    list_display = ['name','age','file2']
admin.site.register(Person, PesonAdmin)

class SubmitAdmin(admin.ModelAdmin):
    list_display = ['file']
admin.site.register(Submit, SubmitAdmin)