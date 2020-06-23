#ghostpost model
from django.db import models
from django.utils import timezone


# Create your models here.
class RoastsAndBoasts(models.Model):
    ROAST = 'Roast'
    BOAST = 'Boast'
    ROASTORBOAST = (
        (ROAST, 'Roast'),
        (BOAST, 'Boast')
    )
    roastorboast = models.CharField(max_length=5,choices=ROASTORBOAST,default=ROAST)
    content = models.CharField(max_length=280)
    upVotes = models.IntegerField(default=0)
    downVotes = models.IntegerField(default=0)
    createdAt = models.DateTimeField(default=timezone.now)
    score = models.IntegerField(default=0)
    def __str__(self):
        if self.roastorboast == 'Roast':
            return "Roast"
        if self.roastorboast == 'Boast':
            return "Boast"

# Boolean to tell whether it's a boast or a roast
# CharField to put the content of the post in
# IntegerField for up votes
# IntegerField for down votes
# DateTimeField for submission time