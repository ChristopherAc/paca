from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    '''
        https://www.fomfus.com/articles/how-to-use-email-as-username-for-django-authentication-removing-the-username
    '''
    """Specificerar modeManager för User klassen"""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """skapar och sparar användaren """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """skapar och sparar en användare med email och lösenord"""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Skapar och sparar en superuser med email och lösenord"""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class User(AbstractUser):
    """Model för användare."""

    has_logged_in = models.BooleanField(default=False)
    phone = models.CharField(max_length=12)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    # Nedan är för att förändra grundklassen som är inbyggd i Django
    username = None
    email = models.EmailField(_('email address'), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        #returnera alltid ett user objekt som förnamn efternamn
        return "{} {}".format(self.first_name, self.last_name)

class Manager(models.Model):
    # Arbetsgivare, kopplad till en användare
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    manages = models.ManyToManyField(User, blank=True, related_name='manages')

    def __str__(self):
        # returnera alltid en arbetsgivare som förnamn - efternamn (i relation till användaren)
        return "{} {}".format(self.user.first_name, self.user.last_name)

class Message(models.Model):
    # Meddelande model.
    is_read = models.BooleanField(default=False)
    text = models.TextField(max_length=200)
    sent_from = models.ForeignKey('User', on_delete=models.CASCADE, related_name='sent_from')
    sent_to = models.ForeignKey('User', on_delete=models.CASCADE, related_name='sent_to')
    sent_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # returnera alltid ett meddelande som "From: user to User on: date"
        return " from: {} to {} on: {}".format(self.sent_from, self.sent_to, self.sent_time)

class Job(models.Model):
    # Model för arbetspass.
    title = models.CharField(max_length=30)
    spots = models.IntegerField()
    manager = models.ManyToManyField('Manager', blank=True, related_name='manager')
    start = models.DateTimeField()
    end = models.DateTimeField()
    worker = models.ManyToManyField(User, blank=True, related_name='worker')

    def spots_left(self):
        # En funktion som returnerar sant om det finns platser kvar i arbetspasset.
        spots = self.spots
        workers = self.worker.count()
        if workers < spots:
            return True
        else:
            return False

    def __str__(self):
        # returnera alltid namnet på arbetspasset.
        return "{}".format(self.title)
