
from django.utils import timezone
from rest_framework import serializers

from .models import Social, Project, Experience


class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social

        # Fields to provide to API endpoint
        fields = ('id', 'text', 'url', 'icon',)

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project

        # Fields to provide to API endpoint
        fields = ('id', 'title', 'description', 'date', 'link1_url', 'link1_icon', 'link2_url', 'link2_icon')

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience

        # Fields to provide to API endpoint
        fields = ('id', 'position', 'employer_name', 'employer_logo', 'description', 'start_date', 'end_date')