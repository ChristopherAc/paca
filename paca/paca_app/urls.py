from django.conf import settings
from django.conf.urls.static import static
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
    # Hämmta alla användare som är bokade på ett pass.
    path('check_booked', views.check_booked, name="check_booked"),
    #ajax för att kolla användartyp
    path('check_user', views.check_user, name='check_user'),
    # Ajax för att kolla om det finns platser kvar i ett pass
    path('check_spots', views.check_spots, name='check_spots'),
    # ajax för att ta bort passen
    path('delete_pass', views.delete_pass, name='delete_pass'),
    # url för att avboka anställd från pass
    path('remove_from_job/<int:job_id>/<int:user_id>', views.remove_from_job, name='remove_from_job'),
    #ändra lösenord i inställningar
    path('password', views.password, name="password"),
    #Profil sidan
    path('profile/', views.profile, name='profile')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
