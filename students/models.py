from django.db import models

# Create your models here.
class StudentInfo(models.Model):
    roll_no = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=100)
    stud_class = models.CharField(max_length=10)
    school = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
    address = models.CharField(max_length=200)

class StudentAcademics(models.Model):
    roll_no = models.ForeignKey(StudentInfo, on_delete = models.CASCADE)
    maths = models.CharField(max_length=3)
    physics = models.CharField(max_length=3)
    chemistry = models.CharField(max_length=3)
    biology = models.CharField(max_length=3)
    english = models.CharField(max_length=3) 

