from django import forms
from .models import Task, UserDetails

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed', 'completion_time']


class User_Details_Form(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = [ 'task', 'name', 'city', 'phone', 'picture']

def __str__(self):
    return self.title 