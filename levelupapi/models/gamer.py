from django.db import models
from django.contrib.auth import get_user_model
from .event import Event


User = get_user_model()


class Gamer(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=50)
    sign_up_events = models.ManyToManyField('levelupapi.Event', related_name='attendees')
