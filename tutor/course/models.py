'''
    Model classes to create database tables namely Course, Grade and Chapter.
'''
from django.db import models
from student.models import Students, Grade
from tutor.users.models import Tutors


class Course(models.Model):
    '''
    A model to store courses records
    '''
    course_name = models.CharField(max_length=50)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    tutor = models.ForeignKey(
        Tutors, on_delete=models.CASCADE
    )
    student = models.ManyToManyField(Students)

    class Meta:
        """
            Meta class odering courses by date created they were created.
        """
        ordering = ('-created',)

    def __str__(self):
        return "%s %s %s" % (self.course_name, " Grade ", self.grade)


class Chapter(models.Model):
    '''
    A model to store chapters records
    '''
    chapter_name = models.CharField(max_length=50)
    content = models.FileField(blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.course, self.chapter_name)
