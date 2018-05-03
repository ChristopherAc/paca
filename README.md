# paca
  Observera att sidan visar en  kalender. kalendern går dock inte att använda för att boka pass(ännu).

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

3. navigera till den mappen i projektet där filen "manage.py" ligger.
4. skriv nu i terminalen:
  python manage.py runserverer
  eller
  python3 manage.py runserver
  eller
  manage.py runserver
5. Om allt fungerar så ska du få en text som bekräftar att server är startad. Om inte så kontrollera tidigare steg
6. Öppna din favoritwebläsare, skriv  http://127.0.0.1:8000/ i adressfältet.
7. Du kan nu logga in på vår sida. Nedan i detta dokument finns det användare du kan använda dig av. Det är helt okej att skapa egna användare.

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
