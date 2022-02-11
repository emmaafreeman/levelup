from django.db import models


class Type(models.Model):
    """Level up type model"""

    type = models.CharField(max_length=50)