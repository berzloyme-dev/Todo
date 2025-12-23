from django.db import models
from django.forms import IntegerField


class Student(models.Model):
    ism = models.CharField(max_length=50)
    yosh = models.IntegerField()
    kurs = models.IntegerField()

    def __str__(self):
        return self.ism

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Studentlar'

class Reja(models.Model):
    sarlavha = models.TextField()
    batafsil = models.TextField(blank=True )
    sana = models.DateField()
    bajarildi = models.BooleanField(default=True)
    Student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.sarlavha
    class Meta:
        verbose_name = 'Reja'
        verbose_name_plural = 'Rejalar'

