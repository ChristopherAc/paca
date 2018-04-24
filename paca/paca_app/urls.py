from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # inställningar
    path('settings/', views.settings, name='settings'),
    # Meddelande
    path('message', views.message, name='message')
]
