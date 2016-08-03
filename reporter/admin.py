from django.contrib import admin

# Register your models here.
from .models import Galletas, Proveedor, Sabor

admin.site.register([Galletas, Proveedor, Sabor])