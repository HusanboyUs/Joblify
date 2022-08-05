from django.db import models
from django.contrib.auth.models import AbstractUser,User


class User(AbstractUser):
    location=models.CharField(max_length=50, blank=True, null=True, default='Warsaw')


class Jobs(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    company=models.CharField(max_length=55, blank=True, null=True)
    position=models.CharField(max_length=55, blank=True, null=True)
    job_location=models.CharField(max_length=55, blank=True, null=True)

    job_choice=(
        ('Full-time','Full-time'),
        ('Part-time','Part-time'),
        ('Remote','Remote'),
        ('Internship','Intersnhip'),
    )

    job_type=models.CharField(choices=job_choice, blank=True, max_length=55, null=True)

    choices=(
        ('Pending','Pending'),
        ('Declined','Declined'),
        ('Interview','Interview'),
    )

    status=models.CharField(choices=choices,blank=True, max_length=55, null=True)
    added=models.DateTimeField(auto_now_add=True, blank=True, null=True)


    def __str__(self):
        return self.company

    class Meta:
        ordering=('-added')
        verbose_name='Jobs'
        vebose_name_plural='Jobs'