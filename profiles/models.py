from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.core.exceptions import ValidationError
from picklefield.fields import PickledObjectField
from jsonfield import JSONField


class UserProfile(models.Model):
    """
    A user profile
    """
    GENDER_CHOICES = (
        ('', 'Please select gender... *'),
        ('M', 'Male'),
        ('F', 'Female'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=40, null=False, blank=False, default='')
    email = models.EmailField(max_length=254, null=False, blank=False)
    town_or_city = models.CharField(max_length=40, null=False, blank=False, default='')
    country = CountryField(blank_label="Country *", max_length=40, null=False, blank=False)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=False, blank=False, default='Please select gender... *')
    weight = models.DecimalField(max_digits=4, decimal_places=1, null=False, blank=False)
    birthdate = models.DateField(null=False, blank=False, default="2000-01-01")
    image = models.ImageField(null=True, blank=True, upload_to='media/')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')

    def __str__(self):
        return self.full_name


class HeroLevels(models.Model):
    """Save calculated fitness levels for user"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    level_data = JSONField()
    general_level = models.DecimalField(max_digits=2, decimal_places=0, default=50)

    def __str__(self):
        return self.user.username


class MailNotificationSettings(models.Model):
    """Settings for mail notifications for individual users"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    notify = models.BooleanField(blank=True, default=True)

    def __str__(self):
        return self.user.username