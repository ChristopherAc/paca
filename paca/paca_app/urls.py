from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # inställningar
    path('settings/', views.settings, name='settings'),
    # Meddelande
    path('message', views.message, name='message'),
    #
    path('changepassword/', views.change_password, name='changepassword')
]
