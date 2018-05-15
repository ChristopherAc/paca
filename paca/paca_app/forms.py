from django.forms import ModelForm
from django.contrib.auth.forms import UserChangeForm
from django import forms
from .models import Message
from .models import User
from .models import Job


# Form för Messages
class MessageForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = Message
        # Vi vill inte att användaren ska ange sent_from
        # Används denna formen så måste allså denna datan läggas in manuellt.
        fields = ['sent_to','text']

# Skapar ett formulär baserad på vår User modell
# Använder endast email, first_name och last_name som input fields
# Lösenord måste manuellt läggas till i databaseobjektet om detta formulär används för
# för att skapa användare
class UserForm(ModelForm):
    class Meta:
        model = User

        fields = ['email', 'first_name', 'last_name', 'phone']

class JobForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(JobForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = Job

        exclude = ['manager', 'worker']

# Skapar ett formulär i inställningar med fälten email,
class EditProfileForm(UserChangeForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User

        fields = ['email', 'first_name', 'last_name', 'phone', 'password']
        exclude = []
    #def clean_password(self):
        #valid = self.User.check_password(self.cleaned_data['password'])
        #if not valid:
            #raise forms.ValidationError("Password Incorrect")
        #return valid
