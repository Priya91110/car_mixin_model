from django.contrib import admin
from .models import carModel
# Register your models here.
class CarAdmin(admin.ModelAdmin):
    list_display = ['carname','price']
    
admin.site.register(carModel,CarAdmin)