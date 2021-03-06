# paca
  OBS. ett nytt bibliotek används. se steg 3 under instruktioner.

  Observera att sidan visar en  kalender. kalendern går dock inte att använda för att boka pass(ännu).

  Granskning:
    De filer som bör granskas är:
      paca_app/views.py
      paca_app/urls.py
      paca_app/models.py
      paca_app/tests.py
      paca_app/admin.py
      paca_app/templates
        add_user.html
        base.html
        change_password.html
        forgot_password.html
        index.html
        jobs.html
        message.html
        settings.html
      paca_app/teplates/registration/login.html

      Filer för whiteboxtestning
      paca/paca/test_settings.py
      paca/spaca_app/tests
        test_models.py
        test_views.py

  Resterande filer är autogenererade av antingen Django eller Fullcalendar
  Använd istället länken "Arbetspass" i headern för att nå dessa funktioner.

  Läs igenom denna filen noga. Det finns faktorer på varje dator som avgör om du måste skriva python3, python innan varje kommando. Har du en "Enviroment variable" i din dator som pekar på python.exe så behöver du inte skriva något innan dina pythonkommandon. Därför rekomenderas du att läsa och prova de olika alternativen som finns i dokumentet.

## Instruktioner
Python 3
1. installera python3 (kryssa i att du vill att pip installeras med python.)

Django==2.0.4
2. i terminalen, installera django med pip.
  'python install django'
  eller
  'python3 install django'
  eller
  'pip install django'

3. Installera bibliotek som behövs för att applikationen ska fungera perfekt.

  Uppmärksamma att ni kan behöva använda olika sätt för att installera. exempelvis pip3 install, python3 install osv.
  använd google.
  pip install django-widget-tweaks
  pip install v pillow==5.0
  pip install pytest
  pip install pytest-django
  pip install pytest-cov
  pip install mixer

4. navigera till den mappen i projektet där filen "manage.py" ligger.

5. skriv nu i terminalen:
  python manage.py runserverer
  eller
  python3 manage.py runserver
  eller
  manage.py runserver

6. Om allt fungerar så ska du få en text som bekräftar att server är startad. Om inte så kontrollera tidigare steg

7. Öppna din favoritwebläsare, skriv  http://127.0.0.1:8000/ i adressfältet.

8. Du kan nu logga in på vår sida. Nedan i detta dokument finns det användare du kan använda dig av. Det är helt okej att skapa egna användare.

## instruktioner för att testa applikationen med unittester
1. Navigera till /paca/paca (i terminalen )

2. Skriv py.test

## Användare
användarnamn: stoff@paca.se
lösenord:     qwer1234
notering:     Är en arbetsledare/Manager i systemet.

användarnamn: Anders@paca.se
lösenord:     qwer1234
notering:     Är en arbetsledare/Manager i systemet.

användarnamn: erik@paca.se
lösenord:     qwer1234
notering:     Anställd/worker i systemet. har stoff@paca.se som arbetsledare.

användarnamn: simon@paca.se
lösenord:     qwer1234
notering:     Anställd/worker i systemet. har stoff@paca.se som arbetsledare.

användarnamn: per@paca.se
lösenord:     qwer1234
notering:     Anställd/worker i systemet. har stoff@paca.se som arbetsledare.
              Denna användaren har aldrig varit inloggad tidigare. Därför kommer en ändring av lösenord ske vid första inloggningen.

användarnamn: anna@paca.se
lösenord:     qwer1234
notering:     Anställd/worker i systemet. har anders@paca.se som arbetsledare.

användarnamn: karin@paca.se
lösenord:     qwer1234
notering:     Anställd/worker i systemet. har anders@paca.se som arbetsledare.

användarnamn: lisa@paca.se
lösenord:     qwer1234
notering:     Anställd/worker i systemet. har anders@paca.se som arbetsledare.
              Denna användaren har aldrig varit inloggad tidigare. Därför kommer en ändring av lösenord ske vid första inloggningen.

användarnamn: admin@paca.se
lösenord:     qwer1234
notering:     Användaren är en superuser, Innebär att du kan logga in på
              "http://127.0.0.1:8000/admin/" och hantera objekt i databasen.
              Detta är inte en del av systemet utan används för vår del mest i utvecklings och testningssyfte. Det går bra att prova på om man är nyfiken dock!.
