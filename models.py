from django.db import models

class Student(models.Model):
    roll_no = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    photo = models.FileField(upload_to='students/', null=True, blank=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name

