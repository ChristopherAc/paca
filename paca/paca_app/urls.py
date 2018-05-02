from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # inställningar
    path('settings/', views.settings, name='settings'),
    # Meddelande
    path('message', views.message, name='message'),
    # Ändra lösenord ( första inloggningen )
    path('changepassword/', views.change_password, name='changepassword'),
    # lägg till en arbetsgivare
    path('add_user/', views.add_user, name='add_user'),
    #Glömt lösenord
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    #Ajax för fullCalendar
    path('/ajax_calendar', views.ajax_calendar, name='ajax_calendar')
]
