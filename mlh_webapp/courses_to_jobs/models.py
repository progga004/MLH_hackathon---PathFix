from django.db import models

class CoursesTable(models.Model):
    jobs = models.CharField(max_length=200, default='0000000')
    course = models.CharField(max_length=200, default='0000000')
    similarity = models.DecimalField(max_digits= 10, decimal_places = 3, default=0.0)
    jobskills = models.CharField(max_length=1000, default='0000000')
    courseskills = models.CharField(max_length=1000, default='0000000')
