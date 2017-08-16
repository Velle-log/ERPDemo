from django.db import models
from django.contrib.auth.models import User
from user_profile.models import ExtraInfo
from django.dispatch import receiver
from django.db.models.signals import post_save
from user_profile.models import Department
# Create your models here.

LEAVE_CHOICE = (

    ('casual', 'casual'),
    ('vacation', 'vacation'),
    ('commuted', 'commuted'),
    ('special casual', 'special casual'),
    ('restricted', 'restricted'),
    ('station leave', 'station leave'),

)

PROCESSING_BY_CHOICES = (
    ('rep user', 'rep user'),
    ('hod', 'Head Of Department'),
    ('director', 'Director')

)

APPLICATION_STATUSES = (

    ('accepted', 'Accepted'),
    ('rejected', 'Rejected'),
    ('processing', 'Being Processed')

)

class Leave(models.Model):
    applicant = models.ForeignKey(User, related_name='applied_for', on_delete=models.CASCADE)
    replacing_user = models.ForeignKey(User, related_name='replaced_for', on_delete=models.CASCADE)
    type_of_leave = models.CharField(max_length=20, choices=LEAVE_CHOICE)
    applied_time = models.DateTimeField(auto_now=True)
    start_date = models.DateField()
    end_date = models.DateField()
    purpose = models.CharField(max_length=500, blank=False)
    leave_address = models.CharField(max_length=100, blank=True)
    processing_status = models.CharField(max_length=20, default='rep user', choices=PROCESSING_BY_CHOICES)
    application_status = models.CharField(max_length=20, default='processing', choices=APPLICATION_STATUSES)

    def __str__(self):
        return '{} - {}'.format(self.applicant.username, self.type_of_leave)

    def save(self, *args, **kwargs):
        if(self.applicant != self.replacing_user):
            if(self.start_date <= self.end_date):
                super(Leave, self).save(*args, **kwargs)
            else:
                raise Exception("Start Date should be less than(or equal to) the End Date")
        else:
            raise Exception("User and Replacing User must be different")

class ApplicationRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="requested_applications")
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="application_request")
    leave = models.ForeignKey(Leave, on_delete=models.CASCADE, related_name='pending_requests')

    def save(self, *args, **kwargs):
        if(self.user != self.recipient):
            super(ApplicationRequest, self).save(*args, **kwargs)
        else:
            raise Exception("User and Replacing User must be different")

    def __str__(self):
        return '{}: {}'.format(self.user.username, self.leave.type_of_leave)

class RemainingLeaves(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='remaining_leaves')
    casual = models.IntegerField(default=30)
    vacation = models.IntegerField(default=60)
    commuted = models.IntegerField(default=10)
    special_casual = models.IntegerField(default=15)
    restricted = models.IntegerField(default=2)

    def __str__(self):
        return '{} has {} casual leaves left'.format(self.user.username, self.casual)

@receiver(post_save, sender=ExtraInfo)
def create_remaining_leaves(sender, instance, created, **kwargs):
    if created and instance.user_type != 'student':
        RemainingLeaves.objects.create(user=instance.user)
