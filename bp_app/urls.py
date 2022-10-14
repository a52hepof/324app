"""bp_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, re_path
from Actividades import views as actividadesViews
from accessAplication import views as accessAplicationViews


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', accessAplicationViews.home, name='home'),
    path('signup', accessAplicationViews.signupPage, name='signup'),
    path('logout', accessAplicationViews.signout, name='logout'),
    path('signin', accessAplicationViews.signin, name='signin'),
    path('Actividades/crear', actividadesViews.crearActividad, name='crearActividades'),
    path('Actividades/creada/<str:idActividad>', actividadesViews.actividadCreada, name='actividadcreada'),
    path('Actividades/listado', actividadesViews.actividadListado, name='actividades'),
    path('Actividades/detalle/<int:idActividad>', actividadesViews.actividadDetalle, name='actividadDetalle'),
    path('Actividades/realizar/<int:idActividad>', actividadesViews.actividadRealizar, name='actividadRealizar'),
    path('Actividades/eliminar/<int:idActividad>', actividadesViews.actividadEliminar, name='actividadEliminar'),
    
]


if settings.DEBUG:
    urlpatterns  += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns  += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)