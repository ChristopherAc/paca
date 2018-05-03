from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import JsonResponse
from django.contrib import messages
from .forms import MessageForm
from .models import Message
from .forms import UserForm
from .models import User
from .models import Manager
from .models import Job
from .forms import JobForm

@login_required
def ajax_calendar(request):
    if request.is_ajax():
        print("lol")

@login_required
def index(request):
    ''' Första sidan, login sida om användaren inte är inloggad.
        Är användaren inloggad så visas kalendern. '''
    if request.user.has_logged_in == False:
        return redirect('changepassword/')
    return render(request,'index.html')

@login_required
def settings(request):
    return render(request, 'settings.html')

@login_required
def jobs(request):
    try:
        manager = Manager.objects.get(user=request.user)
    except:
        manager= False

    if manager:
        type = "manager"
        jobForm = JobForm(request.POST or None)
        if request.method == 'POST':
            if jobForm.is_valid():
                jobFo = jobForm.save()
                new_job.manager.add(manager)
                new_job.save()

        jobs = Job.objects.filter(manager=manager)
        return render(request, 'jobs.html',{'jobForm':jobForm,'jobs':jobs, 'type':type})

    else:
        type = "worker"
        users_manager = Manager.objects.get(manages=request.user)
        jobs = Job.objects.filter(manager=users_manager).exclude(worker=request.user)
        bookings = Job.objects.filter(manager=users_manager).filter(worker=request.user)
        return render(request, 'jobs.html',{'jobs':jobs, 'type':type,'bookings':bookings})

@login_required
def jobs_delete(request,id):
    try:
        manager = Manager.objects.get(user=request.user)
    except:
        return redirect('/jobs')

    target = Job.objects.get(id=id)
    target.delete()
    return redirect('/jobs')

@login_required
def jobs_book(request, id):
    user=request.user
    job = Job.objects.get(id=id)
    job.worker.add(user)
    job.save()
    return redirect('/jobs')

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
    try:
        Manager.objects.get(user=request.user)
    except:
        return redirect('/')
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
            # Spara användaren
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
            get_user = User.objects.get(email=get_email)

            new_password = User.objects.make_random_password()
            get_user.set_password(new_password)
            get_user.save()

            get_managers = Manager.objects.filter(manages=get_user)
            for manager in get_managers:
                print(manager)

            for manager in get_managers:
                password_message = Message(
                    sent_from=get_user,
                    sent_to=manager.user,
                    text="{} {} Har bett om ett nytt lösenord. Nytt lösenord är {}".format(
                        get_user.first_name,
                        get_user.last_name,
                        new_password
                    ))
                password_message.save()

            get_user.has_logged_in == False
            get_user.save()
            messages.add_message(request, messages.SUCCESS, 'Ett nytt lösenord har skickats till din arbetsgivare.')
            return render(request, 'forgot_password.html')

        except User.DoesNotExist:
            get_email = None
            messages.add_message(request, messages.WARNING, 'Det finns ingen användare med angiven email!')
            return render(request, 'forgot_password.html')
    return render(request, 'forgot_password.html')
