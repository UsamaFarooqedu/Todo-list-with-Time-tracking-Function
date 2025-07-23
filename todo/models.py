from django.db import models
from django.urls import reverse
from django.utils import timezone


# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True)
    completion_time = models.DateTimeField(null=True, blank=True)  

    def __str__(self):
        return self.title

    def get_edit_url(self):
        return reverse('edit_task', args=[self.id])

    def get_delete_url(self):
        return reverse('delete_task', args=[self.id])


class UserDetails(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE) 
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='profile_pics', default='default.jpg')
    created_at = models.DateTimeField(auto_now_add=True)



