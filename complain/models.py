from django.db import models
from django.utils.timezone import datetime
from django.contrib.auth.models import User

# Create your models here.
class Complain(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    complaintitle = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    pn = models.CharField(max_length=100)
    gender = models.CharField(max_length=100, choices=(
        ('m', 'Male'),
        ('f', 'Female')
    ))
    complain = models.TextField()
    # image = models.ImageField(upload_to='images/', blank=True)
    treated = models.CharField(max_length=50, choices=(
        ('Yes', 'Yes'),
        ('No', 'No')
    ), null=True, default='No')
    date_added = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']
    