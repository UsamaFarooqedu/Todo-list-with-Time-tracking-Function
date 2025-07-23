from django.contrib import admin
from .models import Task,UserDetails
from .forms import  User_Details_Form

# Register your models here.

admin.site.register(Task)


class UserDetailsAdmin(admin.ModelAdmin):
    form = User_Details_Form
admin.site.register(UserDetails, UserDetailsAdmin)

