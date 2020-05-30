'''
    Model classes to create database tables namely Course and Chapter.
'''

from django.db import models
from student.models import Students

class Course(models.Model):
    '''
    A model to store courses records
    '''
    course_name = models.CharField(max_length=50)
    grade = models.IntegerField()
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    created_by = models.ForeignKey('users.User', on_delete=models.CASCADE)
    student_subscribed = models.ManyToManyField(Students)

    class Meta:
        """
            Meta class odering courses by date created they were created.
        """
        ordering = ('-created',)

    def __str__(self):
        return '{}'.format(self.course_name)


class Chapter(models.Model):
    '''
    A model to store chapters records
    '''
    chapter_name = models.CharField(max_length=50)
    content = models.FileField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    
    def __str__(self):
        return "%s %s" % (self.course, self.chapter_name)
