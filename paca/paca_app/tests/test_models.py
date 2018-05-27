import pytest
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db

class TestUser:
    def test_model(self):
        obj = mixer.blend('paca_app.User')
        assert obj.pk == 1, "Borde skapa en User instans"

    def test_str_(self):
        obj = mixer.blend('paca_app.User')
        assert obj.__str__() == "{} {}".format(obj.first_name, obj.last_name)

class TestManager:
    def test_model(self):
        obj = mixer.blend('paca_app.Manager')
        assert obj.pk == 1, "Borde skapa en Manager instans"

    def test_str_(self):
        obj = mixer.blend('paca_app.Manager')
        assert obj.__str__() == "{} {}".format(obj.user.first_name, obj.user.last_name)

class TestMessage:
    def test_model(self):
        obj = mixer.blend('paca_app.Message')
        assert obj.pk == 1, 'Borde skapa en Message instans'

    def test_str_(self):
        obj = mixer.blend('paca_app.Message')
        assert obj.__str__() == " from: {} to {} on: {}".format(obj.sent_from, obj.sent_to, obj.sent_time)

class TestJob:
    def test_model(self):
        obj = mixer.blend('paca_app.Job')
        assert obj.pk == 1, "Borde skapa en message isntans"

    def test_spots_left_while_spots_left(self):
        user1 = mixer.blend('paca_app.User')
        job = mixer.blend('paca_app.Job',spots=2, worker=user1)
        assert job.spots_left() == 'free', "spots:2 user:1 borde returnera 'free'"

    def test_spots_left_while_spots_filled(self):
        user1 = mixer.blend('paca_app.User')
        user2 = mixer.blend('paca_app.User')
        job = mixer.blend('paca_app.Job',spots=1, worker=[user1,user2])
        assert job.spots_left() == 'full', "spots:1 user:2 borde returnera 'free'"

    def test_spots_left_while_spots_equal(self):
        user1 = mixer.blend('paca_app.user')
        job = mixer.blend('paca_app.Job', spots=1, worker=user1)
        assert job.spots_left() == 'full', "spots:1 user:1 borde returnera 'full'"

    def test_str_(self):
        obj = mixer.blend('paca_app.Job')
        assert obj.__str__() == "{}".format(obj.title)
