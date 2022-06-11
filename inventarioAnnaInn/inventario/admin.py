from django.contrib import admin

# Register your models here.
from .models import Cocina, Insumos, Blancos

admin.site.register(Cocina)
admin.site.register(Insumos)
admin.site.register(Blancos)