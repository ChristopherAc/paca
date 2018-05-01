from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from .forms import MessageForm
from .models import Message
from .forms import UserForm
from .models import User
from .models import Manager

@login_required
def index(request):
    ''' Första sidan, login sida om användaren inte är inloggad.
        Är användaren inloggad så visas kalendern. '''
    if request.user.has_logged_in == False:
        return redirect('changepassword/')
#        request.user.has_logged_in = True

    return render(request,'index.html')

@login_required
def settings(request):
    return render(request, 'settings.html')

@login_required
def message(request):
    # Skapar en Modelform
    form = MessageForm()
    if request.method == 'POST':
        # Hämta skickad formdata
        form = MessageForm(request.POST)
        if form.is_valid():
            # Spara efte validering, commitas ej, då kan vi ändra modellen.
            new_message = form.save(commit=False)
            new_message.sent_from = request.user
            new_message.save()

    messages = Message.objects.filter(sent_to=request.user)
    något_annat = Message.objects.filter(sent_from=request.user)
    return render(request,'message.html',{'form':form,'messages':messages,'något_annat':något_annat})

@login_required
def change_password(request):
    form = PasswordChangeForm(request.user, request.POST)
    if form.is_valid():
        user = form.save()
        request.user.has_logged_in = True
        request.user.save()
        return redirect('/')
    return render(request, 'change_password.html', {'form':form})

# view för att lägga till användare
@login_required
def add_user(request):
    # Skapar en Userform (forms.py Userform)
    form = UserForm()

    # Om förfrågan är en POST
    if request.method == 'POST':

        # Hämta POST datan från formen
        form = UserForm(request.POST)

        # Om Formen är validerad och godkänd.
        if form.is_valid():

            # Spara som ett objekt utan att kommita i databasen
            new_user = form.save(commit=False)

            # generera ett nytt lösenord från djangos inbyggda funktion make_random_password().
            password = User.objects.make_random_password()
            # spara det genererade lösenodet genom djangos set_password()
            new_user.set_password(password)
            # Spara anvndaren
            new_user.save()

            if request.POST.get('ismanager') == 'ismanager':
                manager = Manager(user = new_user)
                manager.save()





            # Skapa ett meddelande från inloggad användare till sig själv,
            # I detta meddelande finns det nya lösenordet för den nya användaren.
            password_message = Message(
                sent_from=request.user,
                sent_to=request.user,
                text="Lösenord för {} {} : {}".format(
                    new_user.first_name,
                    new_user.last_name,
                    password
                ))
            password_message.save()

        # Om inte det skickade formuläret är godkänt så skickar vi tillbaks det,
        # Med felmeddelande.
        else:
            form = request.method(request.POST)

    return render(request, 'add_user.html',{'form':form})

def forgot_password(request):
    if request.method == 'POST':
        try:
            get_email = request.POST.get('Email')
            User.objects.get(email=get_email)
        except User.DoesNotExist:
            get_email = None
    return render(request, 'forgot_password.html')
