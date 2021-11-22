from django.db import models
from django.contrib.auth.models import User


class Home(models.Model):
    """
    Model created to store the gender choices.
    """
    username = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="home",
        default="1"
    )
    order_number = models.IntegerField()
    
    class Meta:
        ordering = ["order_number"]

    def __str__(self):
        return '%s' % (self.title)
