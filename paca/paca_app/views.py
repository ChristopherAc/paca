from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import PasswordChangeForm
from django.http import JsonResponse
from django.contrib import messages
from .forms import EditProfileForm
from .forms import MessageForm
from .models import Message
from .forms import UserForm
from .models import User
from .models import Manager
from .models import Job
from .forms import JobForm
import json
import datetime

@csrf_exempt
def check_spots(request):
    data = request.POST
    if Job.objects.filter(id=data['id']).filter(worker=request.user).exists():
        return JsonResponse({'data':'booked'})
    job = Job.objects.get(id=data['id'])
    return JsonResponse({'data':job.spots_left()})

@csrf_exempt
def delete_pass(request):
    data = request.POST
    job = Job.objects.get(id=data['id'])
    job.delete()
    return JsonResponse({'data':'ok'})

@csrf_exempt
@login_required
def profile(request):
    # Profil sida för användaren
    if request.user.has_logged_in == False:
        return redirect('changepassword/')
    return render(request,'profile.html')

@csrf_exempt
@login_required
def book_user(request):
    # hämta passet med ajax datan.
    data = request.POST
    job = Job.objects.get(id=data['id'])

    # Kolla om användaren redan är bokad på passet.
    this_job_with_this_user = Job.objects.filter(id=data['id']).filter(worker=request.user).exists()
    if this_job_with_this_user:
        return JsonResponse({'response':'Du är redan inbokad på detta passet'})
    print(this_job_with_this_user)
    # Fånga upp tidsspektrumet för att kolla 11-timmars reglen.
    limit_1 = job.start + datetime.timedelta(hours=-11)
    limit_2 = job.end + datetime.timedelta(hours=11)
    intrusive_jobs1 = Job.objects.filter(end__range=[limit_1, limit_2]).exclude(id=job.id).filter(worker=request.user).exists()
    intrusive_jobs2 = Job.objects.filter(start__range=[limit_1, limit_2]).exclude(id=job.id).filter(worker=request.user).exists()

    if intrusive_jobs1 and intrusive_jobs2:
        return JsonResponse({'response':' Detta pass är i konflikt med ett pass du redan är inbokad på','id':data['id']})

    # Kolla om det finns platser kvar på passet.
    if job.spots_left() == True:
        job.worker.add(request.user)
        job.save()
        print("Det finns platser och du är nu inbokad.")
        return JsonResponse({'response':"Du är nu bokad på detta passet."})
    else:
        print("Det finns INGA platser kvar.")
        return JsonResponse({'response':"Inga platser kvar."})

def get_jobs(request):
    # Alla arbetspass hämtas och returneras
    try:
        manager = Manager.objects.get(user=request.user)
    except:
        manager = None
    if manager:
        jobstest = Job.objects.filter(manager=manager)
        jobs = Job.objects.filter(manager=manager).values()

    else:
        manager = Manager.objects.get(manages=request.user)
        jobs = Job.objects.filter(manager=manager).values()

    list_jobs = list(jobs)
    return JsonResponse(list_jobs,safe=False)

def check_user(request):
    try:
        manager = Manager.objects.get(user=request.user)
    except:
        manager = None
    if manager:
        data = "m"
    else:
        data = "a"
    return JsonResponse({'data':data})

@login_required
@csrf_exempt
def save_jobs(request):
    try:
        manager = Manager.objects.get(user=request.user)
    except:
        manager = None
    data = request.POST
    print(data)
    new_job = Job(title=data['title'],spots=int(data['spots']),start=data['start'],end=data['end'])
    new_job.save()
    new_job.manager.add(manager)
    new_job.save()

    return JsonResponse({'start':new_job.start, 'end':new_job.end, 'title':new_job.title})
@login_required
def index(request):
    # Första sidan, login sida om användaren inte är inloggad.
    #Är användaren inloggad så visas kalendern (index.html)
    if request.user.has_logged_in == False:
        return redirect('changepassword/')
    return render(request,'index.html')


@login_required
def edit_profile(request):
    if request.method == 'POST' or request.FILES:
        form = EditProfileForm(request.POST, request.FILES, instance=request.user)

        if form.is_valid():
            form.save(commit=False)


            form.save()
            alert_msg = "Dina inställningar har nu sparats!"
            return render(request, 'edit_profile.html',{'alert_msg':alert_msg, 'form':form})
        else:
            alert_msg=None
    form = EditProfileForm(request.POST or None, instance=request.user)
    args = {'form': form}
    return render(request, 'edit_profile.html', args)

@login_required
def password(request):

    form = PasswordChangeForm(request.user, request.POST or None)
    if form.is_valid():
        user = form.save()
        request.user.has_logged_in = True
        request.user.save()
        return redirect('/')
    return render(request, 'password.html', {'form':form})


@login_required
def jobs(request):
    # Tillfällig view fram tills kalendern är färdig.

    # Kontrollera om den inloggade användaren är en arbetsgivare
    try:
        manager = Manager.objects.get(user=request.user)
    except:
        manager= False

    # Om användaren är en arbetsgivare. Så ska ett formulär för att lägga till arbetspass finnas.
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

    # Om användaren inte är en arbetsgivare så skall endast passen synas.
    else:
        type = "worker"
        users_manager = Manager.objects.get(manages=request.user)
        jobs = Job.objects.filter(manager=users_manager).exclude(worker=request.user)
        bookings = Job.objects.filter(manager=users_manager).filter(worker=request.user)
        return render(request, 'jobs.html',{'jobs':jobs, 'type':type,'bookings':bookings})

@login_required
def jobs_delete(request,id):
    # Endast en arbetsgivares ska kunna ta bort pass.
    try:
        manager = Manager.objects.get(user=request.user)
    except:
        return redirect('/jobs')

    target = Job.objects.get(id=id)
    target.delete()
    return redirect('/jobs')

@login_required
def jobs_book(request, id):
    # Arbetare bokar upp sig på jobb
    user=request.user
    job = Job.objects.get(id=id)
    job.worker.add(user)
    job.save()
    return redirect('/jobs')

@login_required
def new_message(request):
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
            form = MessageForm()
            messages.success(request, "Ditt meddelande har skickats!")
    return render(request,'new_message.html', {'form':form})

@login_required
def sent_messages(request):
    """ Sparar alla meddelande som är skickade från den inloggande användaren """
    message_sent = Message.objects.filter(sent_from=request.user)
    return render(request, 'sent_messages.html', {'message_sent':message_sent})

@login_required
def recieved_messages(request):
    """ Sparar alla meddelande som är mottagna av den inloggande användaren """
    message_recieved = Message.objects.filter(sent_to=request.user)
    return render(request, 'recieved_messages.html', {'message_recieved':message_recieved})


@login_required
def count_unread_messages(request):
    """ Räknar och sparar antal meddelande som är skickade till inloggade användare och inte lästa """
    unread_msg = Message.objects.filter(sent_to=request.user).filter(is_read=False).count()
    data = {
        "unread_msg":unread_msg,
    }
    return JsonResponse(data)

@login_required
def change_password(request):
    form = PasswordChangeForm(request.user, request.POST or None)
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

    # managers = Manager.user.all()
    users = User.objects.filter(manager=None)
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

            # Kontrollera om checkobxen är ifylld för "arbetsgivare"
            if request.POST.get('ismanager') == 'ismanager':
                # om checkboxen är ifylld så sparas användaren som en Arbetsgivare.
                manager = Manager(user = new_user)

                manager.save()

                manages = request.POST.getlist('manages')
                for user in manages:
                    user = User.objects.get(pk=user)
                    manager.manages.add(user)
                    manager.save()

            else:
                this_manager = Manager.objects.get(user=request.user)
                this_manager.manages.add(new_user)
                this_manager.save()

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

            success_msg = "Grattis! Din användare är nu skapad. Lösenordet finner bland dina <a href='/message'>meddelande</a>"

            form = UserForm(None)
            # Om inte det skickade formuläret är godkänt så skickar vi tillbaks det,
            # Med felmeddelande.
            return render(request, 'add_user.html',{'form':form, 'success_msg':success_msg, 'users':users})
        else:
            form = UserForm(request.POST)

    success_msg = None
    return render(request, 'add_user.html',{'form':form, 'success_msg':success_msg, 'users':users})

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
