from django.db import models
from .gametype import Type


class Game(models.Model):
    """Level up game model"""

    title = models.CharField(max_length=50, null=True)
    maker = models.CharField(max_length=50, null=True)
    gamer = models.ForeignKey('levelupapi.Gamer', on_delete=models.SET_NULL, null=True)
    game_type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True)
    number_of_players = models.IntegerField(null=True)
    skill_level = models.IntegerField(null=True)