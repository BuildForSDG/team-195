from django.db import models
'''
	A model to store course records
'''

class Chapter(models.Model):
    chapter_name = models.CharField(max_length=50)
    content = models.FileField()

    def __str__(self):
        return self.chapter_name



class Course(models.Model):
    course_name = models.CharField(max_length=50)
    grade = models.CharField(max_length=20)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    chapters = models.ManyToManyField(Chapter)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.course_name
