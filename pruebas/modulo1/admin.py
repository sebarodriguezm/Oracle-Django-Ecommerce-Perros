from django.contrib import admin
from .models import *
# Register your models here.


class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ('nombre'),
    ordering = ['nombre'] 
    
class ProductoAdmin(admin.ModelAdmin):
    search_fields = ('nombre'),
    ordering = ['nombre']  
    autocomplete_fields = ['categoria'] 
    
class MarcaAdmin(admin.ModelAdmin):
    search_fields = ('nombre'),
    ordering = ['nombre']       

class RazaAdmin(admin.ModelAdmin):
    ordering = ['nombre']
    autocomplete_fields = ['categoria']
    

admin.site.register(Categoria, CategoriaAdmin)  
admin.site.register(Raza, RazaAdmin)   
admin.site.register(Cliente)   
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Marca, MarcaAdmin)
    
    