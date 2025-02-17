from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Student(models.Model):
    student_id = models.CharField(max_length=100, primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)  # Store hashed passwords

    def save(self, *args, **kwargs):
        # Hash password before saving if it's not already hashed
        if not self.password.startswith("pbkdf2_sha256$"):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def verify_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.name
