
from .settings import *

# Specificerar att databasen ska vara lokal och minnsebaserad under testning.
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory",
    }
}
