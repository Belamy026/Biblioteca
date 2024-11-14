from django.contrib import admin
from .models import Autor, Libro, Cliente, Prestamo, Multa

admin.site.register(Autor)
admin.site.register(Libro)
admin.site.register(Cliente)
admin.site.register(Prestamo)
admin.site.register(Multa)
