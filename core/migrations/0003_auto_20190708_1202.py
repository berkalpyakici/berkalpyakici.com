# Generated by Django 2.2.3 on 2019-07-08 17:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190708_1156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='datetime',
        ),
        migrations.AddField(
            model_name='project',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='experience',
            name='employer_logo',
            field=models.ImageField(default='uploaded_images/default.jpg', upload_to='uploaded_images/'),
        ),
    ]
