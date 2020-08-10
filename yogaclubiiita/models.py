from django.db import models

DAY_OF_THE_WEEK = (
    (0 , '---Select day---'),
    (1 , 'Monday'),
    (2 , 'Tuesday'),
    (3 , 'Wednesday'),
    (4 , 'Thursday'),
    (5 , 'Friday'),
    (6 , 'Saturday'), 
    (7 , 'Sunday'),
)

class Contact(models.Model):
    Name = models.CharField(max_length=200)
    Mail = models.EmailField()
    Subject = models.CharField(max_length=200)
    Message = models.TextField()
    created_at =models.DateTimeField(auto_now_add=True)
    

    class Meta:
        ordering = ['created_at']

class Schedule(models.Model):
    Day = models.IntegerField(choices=DAY_OF_THE_WEEK,  default=0)
    StartTime = models.TimeField()
    EndTime = models.TimeField()

class StudioAddress(models.Model):
    Address = models.CharField(max_length=200)
    ContactNumber = models.CharField(max_length=20)
    Website = models.CharField(max_length=20)


