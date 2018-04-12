from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    ''' Första sidan, login sida om användaren inte är inloggad.
        Är användaren inloggad så visas kalendern. '''

    return render(request,'index.html')

@login_required
def settings(request):
    return HttpResponse('välkommen till inställningar!')
