from django.shortcuts import render

def index(request):
    ''' Första sidan, login sida om användaren inte är inloggad.
        Är användaren inloggad så visas kalendern. '''
        
    return render(request,'index.html')
