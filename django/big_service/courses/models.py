  
from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=255)
    credit = models.IntegerField()
    grade = models.CharField(max_length=20)
    description = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.title} {self.credit}"

# After describing a Model, we must run a command to create the table in SQLite database.
# py manage.py makemigrations courses
