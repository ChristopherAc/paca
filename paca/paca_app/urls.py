from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # inställningar
    path('/edit_profile', views.edit_profile, name='edit_profile'),
    # Nytt meddelande
    path('new_message/', views.new_message, name='new_message'),
    # Skickade meddelande
    path('sent_messages/', views.sent_messages, name='sent_messages'),
    # Mottagna meddelande
    path('recieved_messages/', views.recieved_messages, name='recieved_messages'),
    #Antal olästa meddelande
    path('unread_messages', views.count_unread_messages, name='unread_messages'),
    # Ändra lösenord ( första inloggningen )
    path('changepassword', views.change_password, name='changepassword'),
    # lägg till en arbetsgivare
    path('add_user/', views.add_user, name='add_user'),
    #Glömt lösenord
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    #Ajax för fullCalendar
    path('get_jobs', views.get_jobs, name='get_jobs'),
    #Ajax för save_jobs
    path('save_jobs', views.save_jobs, name='save_jobs'),
    #ajax för att boka in användare på pass
    path('book_user', views.book_user, name="book_user"),
    #ajax för att kolla användartyp
    path('check_user', views.check_user, name='check_user'),
    # Ajax för att kolla om det finns platser kvar i ett pass
    path('check_spots', views.check_spots, name='check_spots'),
    # ajax för att ta bort passen
    path('delete_pass', views.delete_pass, name='delete_pass'),
    #Tillfällig URL för arbetspass
    path('jobs', views.jobs, name="jobs"),
    #tillfällig URL för att ta bort pass
    path('jobs/delete/<int:id>', views.jobs_delete, name="jobs_delete"),
    #tillfällig URL för att boka pass
    path('jobs/book/<int:id>', views.jobs_book, name="jobs_book"),
    #ändra lösenord i inställningar
    path('password', views.password, name="password"),
    #Profil sidan
    path('profile/', views.profile, name='profile')
]
