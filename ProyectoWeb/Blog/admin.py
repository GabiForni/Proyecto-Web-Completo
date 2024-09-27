from django.contrib import admin
from .models import Categoria, Post

# Register your models here.


#creamos las clases correspondientes
#estas clases heredan de los modelos definidos por django
#pero se modifican agregando campos definidos por el usuario
class Categoria_admin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class Post_admin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

# registramos las clases en el panel de administracion del sitio
# el 2do parametro establece las configuraciones definidas por el usuario
# de lo contrario Django utiliza las configuraciones predeterminadas
admin.site.register(Categoria, Categoria_admin)
admin.site.register(Post, Post_admin)