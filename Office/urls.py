"""Office URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.auth import urls
from Office import settings
from WebApp import views, token
from WebApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('create/', CreateEmp, name='create'),
    path('', ListEmp, name='home'),
    path('<int:id>/update/', UpdateEmp, name='UpdateEmp'),
    path('<int:id>/delete/', DeleteEmp, name='DeleteEmp'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('logout/', log_out, name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
