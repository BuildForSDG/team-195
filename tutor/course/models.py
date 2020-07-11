'''
    Model classes to create database tables namely Course, Grade and Chapter.
'''
from django.core.validators import RegexValidator
from django.db import models
from student.models import Students, Grade
from tutor.users.models import Tutors, User


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


class Posts(models.Model):
    '''
    A model to store forum messages
    '''
    alphanumeric_characters = RegexValidator(
        r'^[\w\W]+$', 'Only alphanumeric characters are allowed.'
    )

    post = models.CharField(
        max_length=500, validators=[alphanumeric_characters]
    )
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s %s" % (
            self.post, self.course_id, self.user_id
            )


class Comments(models.Model):
    '''
        A model to store forum's post's comments
    '''
    alphanumeric_characters = RegexValidator(
        r'^[\w\W]+$', 'Only alphanumeric characters are allowed.'
    )

    comment = models.CharField(
        max_length=500, validators=[alphanumeric_characters]
    )
    post_id = models.ForeignKey(Posts, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s %s" % (
            self.comment, self.post_id, self.user_id
            )
