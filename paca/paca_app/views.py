from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from .forms import MessageForm
from .models import Message

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
