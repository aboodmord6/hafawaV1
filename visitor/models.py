from django.db import models
from django.utils import timezone

# Create your models here.

class PR_profile(models.Model):
    user = models.ForeignKey('Main.MyUser', on_delete=models.CASCADE)
    homephone = models.CharField(max_length=20 , blank=True, default = "" ) 
    cp = models.CharField(max_length=5)
    nationalty = models.CharField(max_length=255)
    personalPhoto = models.ImageField(upload_to='personalPhoto', default = 'personalPhoto/icon.png')
    createDate = models.DateTimeField(default=timezone.now)
    class Meta:
        ordering = ["-createDate"]
    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

class PR_Request(models.Model):
    requester = models.ForeignKey('Main.MyUser', on_delete=models.CASCADE) 
    numberOfGuests = models.IntegerField(default=0)
    hotelName = models.CharField(max_length=200 , null=True)
    hotelLocation = models.CharField(max_length=255 , null=True) 
    nationaltyOfvisitors = models.CharField(max_length=255)
    event = models.ForeignKey('event.Event', on_delete=models.CASCADE)  
    #Admin
    isApproved = models.IntegerField(default='-1')
    notes = models.TextField(default = "لايوجد ملاحظات")
    createDate = models.DateTimeField(default=timezone.now) 
    
    class Meta:
        ordering = ['-createDate']

    def __str__(self):
        return self.requester.first_name + ' ' + self.requester.last_name