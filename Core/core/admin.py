from django.contrib import admin
from .models import Categorias, Pag1juegos,MundoAbierto,Rol,Lucha,Aventura
# Register your models here.
class juegoAdmin(admin.ModelAdmin):
  list_display=['NombreDelJuego','CompañiaCreadora','Plataforma','Descripcion']
  search_fields =['NombreDelJuego','CompañiaCreadora']
  list_filter=['Categorias']
  list_per_page=10


admin.site.register(Categorias)
admin.site.register(Pag1juegos,juegoAdmin)
admin.site.register(MundoAbierto,juegoAdmin)
admin.site.register(Rol,juegoAdmin)
admin.site.register(Lucha,juegoAdmin)
admin.site.register(Aventura,juegoAdmin)

