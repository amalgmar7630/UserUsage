from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    @property
    def name(self):
        if not self.get_full_name():
            return self.email
        return self.get_full_name()

    def __str__(self):
        return self.name
