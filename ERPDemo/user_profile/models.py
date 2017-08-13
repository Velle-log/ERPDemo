from django.db import models
from django.contrib.auth.models import User

class Designation(models.Model):

    CHOICES = (
        ('faculty', 'faculty'),
        ('staff', 'staff'),
        ('student', 'student'),
    )

    designation = models.CharField(max_length=20, unique=True, null=False, blank=False)
    user_type = models.CharField(choices=CHOICES, max_length=10, blank=False)

    def __str__(self):
        return '{}: {}'.format(self.designation, self.user_type)

class Designated(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE)

    def __str__(self):
        return '{}: {}'.format(self.user.username, self.designation.designation)
