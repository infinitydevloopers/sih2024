from django.db import models

# Create your models here.
from django.db import models
import random

class User(models.Model):
    ROLE_CHOICES = [
        (0, 'Researcher'),
        (1, 'Entrepreneur'),
        (2, 'Company'),
        (3, 'Accelerator'),
    ]

    id = models.CharField(primary_key=True, max_length=12, editable=False, unique=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    role = models.IntegerField(choices=ROLE_CHOICES)
    phone_no = models.CharField(max_length=15)
    updated_at = models.DateTimeField(auto_now=True)
    last_logged_in_at = models.DateTimeField(null=True, blank=True)
    address = models.TextField()
    citizenship = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if not self.id:
            role_prefix = str(self.role) + "_"
            random_number = str(random.randint(1000000, 99999999))
            self.id = role_prefix + random_number

        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
