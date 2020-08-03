from django.contrib import admin
from django.urls import include,path

urlpatterns = [
    path('', include('ApiPokemon.urls')),
    path('', include('GetPokemon.urls')),
    path('admin/', admin.site.urls),
]
