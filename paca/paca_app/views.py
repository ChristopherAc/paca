from django.shortcuts import render, HttpResponse

def index(request):
    ''' Första sidan, login sida om användaren inte är inloggad.
        Är användaren inloggad så visas kalendern. '''

    return render(request,'index.html')
