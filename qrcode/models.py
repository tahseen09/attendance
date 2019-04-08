from django.db import models

# Create your models here.
class students(models.Model):
    roll = models.CharField(max_length = 100, null = True, blank = True, unique = True)
    name = models.CharField(max_length = 100, null = True, blank = True)
    subject = models.CharField(max_length = 100, null = True, blank = True)
    semester = models.CharField(max_length = 100, null = True, blank = True)