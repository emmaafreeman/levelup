from django.db import models
from .game import Game


class Event(models.Model):
    """Level up event model"""

    organizer = models.ForeignKey('levelupapi.Gamer', on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=50, null=True)
    game = models.ForeignKey(Game, on_delete=models.SET_NULL, null=True)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)

    @property
    def joined(self):
        """ Join a new event """
        return self.__joined

    @joined.setter
    def joined(self, value):
        self.__joined = value
