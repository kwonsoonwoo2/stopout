from django.db import models


class School(models.Model):
    school_name = models.CharField(max_length=200)

    def __str__(self):
        return self.school_name


class Student(models.Model):
    school = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
    )
    student_name = models.CharField(max_length=200)
    friends = models.ManyToManyField(
        'self',
        through='Friend',
        symmetrical=False,
    )

    def __str__(self):
        return self.student_name

class Friend(models.Model):
    school = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
    )
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
    )