from django.db import models
from django.urls import reverse

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    school = models.CharField(max_length=20)
    class Meta:
        verbose_name = ("Student")
        verbose_name_plural = ("Students")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Student_detail", kwargs={"pk": self.pk})

class Family(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    father_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=20)
    brother = models.CharField(max_length=20)
    sister = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Family"
        unique_together = ['father_name', 'brother']
        ordering = ['id']

    def __str__(self):
        return self.father_name


class Todo(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    completed= models.BooleanField(default=False)

    def __str__(self):
        return self.title