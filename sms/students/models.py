from django.db import models

# Create your models here.
class Student(models.Model):
    user=models.OneToOneField('auth.User', on_delete=models.CASCADE,null=False)
    enrollment_number=models.CharField(max_length=20, unique=True,null=False)
    course=models.CharField(max_length=100,null=False)
    semester=models.IntegerField(default=1,null=False)
    contact_number=models.CharField(max_length=15,null=False)
    address=models.TextField(null=False)
    date_of_birth=models.DateField(null=False)

class Course(models.Model):
    course_name=models.CharField(max_length=100,null=False)
    course_code=models.CharField(max_length=10, unique=True,null=False)
    duration_years=models.IntegerField(null=False)
    description=models.TextField(null=True, blank=True)

class Attendance(models.Model):
    student_id=models.ForeignKey(Student, on_delete=models.CASCADE,null=False)
    date=models.DateField(null=False)
    status=models.CharField(max_length=10, choices=[('Present', 'Present'), ('Absent', 'Absent')], null=False)

class Subject(models.Model):
    subject_name=models.CharField(max_length=100,null=False)
    subject_code=models.CharField(max_length=10, unique=True,null=False)
    course=models.ForeignKey(Course, on_delete=models.CASCADE,null=False)
    semester=models.IntegerField(null=False)

class Marks(models.Model):
    student_id=models.ForeignKey(Student, on_delete=models.CASCADE,null=False)
    subject_id=models.ForeignKey(Subject, on_delete=models.CASCADE,null=False)
    marks_obtained=models.FloatField(null=False)
    total_marks=models.FloatField(null=False)
    exam_type=models.CharField(max_length=50,null=False, choices=[('Internal', 'Internal'), ('External', 'External')])