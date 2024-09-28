from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Tarea.urls')),  # Asegúrate de incluir las URLs de tu aplicación
]
