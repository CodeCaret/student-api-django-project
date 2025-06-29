from django.db import models

class StudentDetail(models.Model):
    name = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    course = models.TextField()

    def __str__(self):
        return self.name