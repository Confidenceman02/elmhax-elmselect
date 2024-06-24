from django.db import models
from django.db.models.fields import CharField


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)
    duration = models.IntegerField()
    rating = models.FloatField()

    def __str__(self) -> str:
        return self.name


class Extra(models.Model):
    name = CharField(max_length=100)

    def __str__(self):
        return self.name


class Promotion(models.Model):
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    extras = models.ManyToManyField(Extra)
