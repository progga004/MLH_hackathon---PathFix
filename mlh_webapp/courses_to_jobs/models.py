from django.db import models

class CoursesTable(models.Model):
    course = models.CharField(max_length=200)
    jobs = models.CharField(max_length=200)
    