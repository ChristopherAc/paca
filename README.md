# paca

Krav
Django==2.0.4
Python 3

Observera att vissa kommandon kräver att man skriver 'python' eller 'python3' innan sitt kommando. Detta beror helt på din installation av python.

exempel:
  python3 manage.py runserver
  python manage.py runserver
  manage.py runserver

  ovan är 3 fungerande kommandon det är något ni får testa lite på egen hand vad som gäller för er installation.

##steg för att starta:

1 packa upp zip filen.

2 installera django på din dator.
  'pip install django'

3 Navigera till mappen där filen manage.py ligger (paca/paca). Gör detta genom kommandotolken (den ligger i paca/paca)

4.Skriv in kommandot 'manage.py migrate'.

5 skapa en användare: 'manage.py createsuperuser'

6 skriv in önskad e-mail och önskat lösenord när det efterfrågas.

7 när du har fått bekräftat att en ny användare har skapats skriv in 'manage.py runserver'.

8 gå till http://127.0.0.1:8000/

9 Du kan nu logga in och ut från vår hemsida med den uppgifter du angav!
