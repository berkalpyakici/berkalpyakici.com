from django.contrib import admin

from .models import Setting, Social, Project, Experience

admin.site.register(Setting)
admin.site.register(Social)
admin.site.register(Project)
admin.site.register(Experience)