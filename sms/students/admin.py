from django.contrib import admin
from .models import Student, Course, Attendance, Subject, Marks
# Register your models here.

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Attendance)
admin.site.register(Subject)
admin.site.register(Marks)