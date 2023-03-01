from django.urls import path
from . import views

urlpatterns = [
    path('', views.depoimento,name='depoimento'),
]