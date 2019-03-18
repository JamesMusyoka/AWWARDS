from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from tinymce.models import HTMLField

class Project(models.Model):
    title = models.CharField(max_length=25)
    link = models.CharField(max_length=50, null=True)
    description = HTMLField()
    project_image = models.ImageField(upload_to='project/')
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['title']

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    @classmethod
    def search_by_title(cls):
        aww = cls.objects.filter(title__icontains=search_term)

    @classmethod
    def Project(cls):
        today = dt.date.today()
        aww = cls.objects.filter(title)
        return aww



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', default=True)
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    profile_pic = models.ImageField(upload_to='profile/', default=True)
    bio = models.CharField(max_length=200, default=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)

    def save_profile(self):
        self.save

class Rate(models.Model):
    rate = models.CharField(max_length=144)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, default=True)
    user = models.ForeignKey(User, default=True, on_delete=models.CASCADE)

    def save_rate(self):
        self.save()

    def delete_rate(self):
        self.delete()

class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()

