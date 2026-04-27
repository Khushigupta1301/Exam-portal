
from django.db import models

class ExamForm(models.Model):
    full_name = models.CharField(max_length=100)
    course = models.CharField(max_length=50)
    year = models.IntegerField()
    address = models.TextField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.full_name
