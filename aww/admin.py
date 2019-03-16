from django.contrib import admin
from .models import Project, Profile, Rate

class ProjectAdmin(admin.ModelAdmin):
    filter_horizontal =('rate')

admin.site.register(Project)
admin.site.register(Profile)
admin.site.register(Rate)

