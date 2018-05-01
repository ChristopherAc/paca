from django.test import TestCase
from .models import User

# Create your tests here.
class TestRedirectToLogin(TestCase):

    def test_redirect_home_to_login(self):
        response = self.client.get('')
        self.assertRedirects(response, '/accounts/login/?next=/')

class TestNoRedirectLogin(TestCase):
    def setUp(self):
        user_manager = User.objects.create(email='testuser133333@gmail.com',password='qwer1234')
        user_manager.save()
        login = self.client.login(email='testuser@gmail.com',password='qwer1234')

    def test_template_home(self):
        print(User.objects.create(email='testuser@gmail.com',password='qwer1234'))
        response = self.client.get('')
        self.assertTemplateUsed(response,'index.html')
