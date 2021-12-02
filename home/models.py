from django.db import models
from django import forms

# Create your models here.
class Task(models.Model):
    taskTitle =models.CharField(max_length=30)
    taskdesc = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    randomno=models.DecimalField(decimal_places=10, max_digits=15, default=35.256488115)

    def __str__(self):
        return self.taskTitle+" Added on "+str(self.time)+" RN "+str(self.randomno)