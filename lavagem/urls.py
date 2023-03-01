from django.urls import path
from . import views

urlpatterns = [
    path('', views.lavagem, name='lavagem'),
    path('agendados/', views.agendados, name='agendados'),
]