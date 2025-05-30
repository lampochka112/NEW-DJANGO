
from django.contrib import adminfrom django.contrib import admin
from django.urls import path
from converter import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('converter/', views.converter, name='converter'),
    path('contacts/', views.contacts, name='contacts'),
]
