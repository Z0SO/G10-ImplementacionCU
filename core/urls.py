from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # incluimos la app de avm
    path('api/', include('avm.urls')),
    
    # incluimos tambien la app de autenticacion con JWT
    path('accounts/', include('accounts.urls')),

]
