from datetime import datetime
from django.contrib.auth.models import User
from django.db import models


class officemodel(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, unique=True, db_index=True)
    DateofJoining = models.DateField(default=datetime.now)
    Salary = models.DecimalField(max_digits=10, decimal_places=2)
    Photo = models.ImageField(upload_to='profile pictures', blank=True, null=True)
    Working = models.BooleanField(default=False, choices=[(True, 'Yes'), (False, 'No')])
    Address = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name
