from django.db import models
from django.db.models import Sum
from django.utils import timezone
from visitor.models import PR_Request


class Event(models.Model):
    name = models.CharField(max_length=50)  
    date = models.DateField(default=timezone.now)
    time = models.TimeField(default=timezone.now)
    maxcap = models.IntegerField(default=1)
    image = models.ImageField(upload_to='event' ,default='event/banner.png')

    def realAttendee(self):
        return PR_Request.objects.filter(event=self , isApproved=1).aggregate(Sum('numberOfGuests'))['numberOfGuests__sum'] or 0

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date']


class EventReport():
    pass