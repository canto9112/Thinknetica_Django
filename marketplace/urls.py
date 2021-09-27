from django.contrib import admin
from django.urls import path, include
from main.views import index
from django.contrib.flatpages import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', index, name='index'),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('about/', views.flatpage, {'url': '/about/'}, name='about'),
    path('contact/', views.flatpage, {'url': '/contact/'}, name='contact'),


]
