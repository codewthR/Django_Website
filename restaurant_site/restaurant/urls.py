from django.urls import path
from . import views
from django.http import HttpResponse

from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('menu/', views.menu, name='menu'),
    # path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
