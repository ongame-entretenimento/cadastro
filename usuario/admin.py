from django.contrib import admin
from usuario.models import Usuario, UsuarioPendente, Cidade, Estado

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'email', 'sexo', 'data_nascimento', 'data_cadastro',)
    list_display_links = ('usuario', 'email', 'sexo', 'data_nascimento', 'data_cadastro',)
    list_filter = ('confirmado', 'sexo', )
    search_fields = ('usuario', 'email',)

class UsuarioPendenteAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'email', 'sexo', 'data_nascimento', 'data_cadastro',)
    list_display_links = ('usuario', 'email', 'sexo', 'data_nascimento', 'data_cadastro',)
    list_filter = ('confirmado', 'sexo', )
    search_fields = ('usuario', 'email',)

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(UsuarioPendente, UsuarioPendenteAdmin)
admin.site.register(Cidade)
admin.site.register(Estado)
