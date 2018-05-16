import pytest
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db

# class TestMessage:
#     def test_model(self):
#         obj = mixer.blend('paca_app.Message')
#         assert obj.pk == 1, 'Borde skapa en Message instans'
