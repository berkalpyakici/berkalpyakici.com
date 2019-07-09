from django.db import models
from django.utils import timezone

class Setting(models.Model):
    """
    Model for social buttons.
    """
    site_name = models.CharField(max_length=100, null=True, blank=True)
    favicon = models.ImageField(upload_to='uploaded_images/', default='uploaded_images/favicon.ico')

    class Meta:
         verbose_name = "Website General Setting"

    def __str__(self):
        """
        Returns a human-readable string for the instance.
        """
        return self.site_name + ' ['+str(self.id)+']'

class Social(models.Model):
    """
    Model for social buttons.
    """
    text = models.CharField(max_length=100, null=True, blank=True)
    url = models.CharField(max_length=100, null=True, blank=True)
    icon = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
         verbose_name = "Social Icon"

    def __str__(self):
        """
        Returns a human-readable string for the instance.
        """
        return self.text

class Project(models.Model):
    """
    Model for project listing.
    """
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=400, null=True, blank=True)
    date = models.DateField(default=timezone.now)
    link1_url = models.CharField(max_length=100, null=True, blank=True)
    link1_icon = models.CharField(max_length=100, null=True, blank=True)
    link2_url = models.CharField(max_length=100, null=True, blank=True)
    link2_icon = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
         verbose_name = "Project"

    def __str__(self):
        """
        Returns a human-readable string for the instance.
        """
        return self.title

class Experience(models.Model):
    """
    Model for experience listing.
    """
    position = models.CharField(max_length=100, null=True, blank=True)
    employer_name = models.CharField(max_length=100, null=True, blank=True)
    employer_logo = models.ImageField(upload_to='uploaded_images/', default='uploaded_images/default.jpg')
    description = models.CharField(max_length=400, null=True, blank=True)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)

    class Meta:
         verbose_name = "Work Experience"

    def __str__(self):
        """
        Returns a human-readable string for the instance.
        """
        return self.position + ' at ' + self.employer_name