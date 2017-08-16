from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

CHOICES = (
    ('faculty', 'faculty'),
    ('staff', 'staff'),
    ('student', 'student'),
)

class Department(models.Model):
    department_name = models.CharField(default='None', unique=True, max_length=50)

    def __str__(self):
        return self.department_name

class ExtraInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='details')
    department = models.ForeignKey(Department, null=True, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=20, choices=CHOICES)
    pf_number = models.IntegerField(null=True)

    def __str__(self):
        return '{}: {}'.format(self.user.username, self.user_type)

@receiver(post_save, sender=User)
def add_extra_data(sender, instance, created, **kwargs):
    if created:
        ExtraInfo.objects.create(user=instance)

class Designation(models.Model):

    designation = models.CharField(max_length=20, unique=True, null=False, blank=False)
    user_type = models.CharField(choices=CHOICES, max_length=10, blank=False)

    def __str__(self):
        return '{}: {}'.format(self.designation, self.user_type)

class Designated(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='designation')
    designation = models.OneToOneField(Designation, on_delete=models.CASCADE)

    def __str__(self):
        return '{}: {}'.format(self.user.username, self.designation.designation)
