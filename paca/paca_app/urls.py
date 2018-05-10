from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # inställningar
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    # Meddelande
    path('message', views.message, name='message'),
    # Ändra lösenord ( första inloggningen )
    path('changepassword/', views.change_password, name='changepassword'),
    # lägg till en arbetsgivare
    path('add_user/', views.add_user, name='add_user'),
    #Glömt lösenord
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    #Ajax för fullCalendar
    path('get_jobs', views.get_jobs, name='get_jobs'),
    #Tillfällig URL för arbetspass
    path('jobs', views.jobs, name="jobs"),
    #tillfällig URL för att ta bort pass
    path('jobs/delete/<int:id>', views.jobs_delete, name="jobs_delete"),
    #tillfällig URL för att boka pass
    path('jobs/book/<int:id>', views.jobs_book, name="jobs_book")
]
