from django.contrib import admin
from django.urls import path

from flatpages import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hello/', views.hello, name='hello'),
    path('admin/', admin.site.urls),
]
