from django.test import RequestFactory
from django.contrib.auth.models import AnonymousUser
from mixer.backend.django import mixer
import pytest
from .. import views
pytestmark = pytest.mark.django_db

class TestIndex:
    def test_non_authenticated_user(self):
        req = RequestFactory().get('/')
        req.user = AnonymousUser()
        resp = views.index(req)
        assert 'login' in resp.url, "Borde redirecta till loginview"

    def test_authenticated_user(self):
        user = mixer.blend('paca_app.User', has_logged_in=True)
        req = RequestFactory().get('/')
        req.user = user
        resp = views.index(req)
        assert resp.status_code == 200, "Borde gå att nå index som inloggad användare."

    def test_authenticated_user_first_login(self):
        user = mixer.blend('paca_app.User', has_logged_in=False)
        req = RequestFactory().get('/')
        req.user = user
        resp = views.index(req)
        assert 'changepassword' in resp.url, "Borde redirecta användare till att ändra lösenord"
