from django.forms import ModelForm
from .models import Message

# Form för Messages
class MessageForm(ModelForm):
    class Meta:
        model = Message
        # Vi vill inte att användaren ska ange sent_from
        # Används denna formen så måste allså denna datan läggas in manuellt.
        fields = ['sent_to','text']
