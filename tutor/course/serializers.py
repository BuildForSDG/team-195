'''
    A serializer to serialize data from Course and Chapter models
    and parse json to the view.
'''


from rest_framework import serializers
from .models import Course, Chapter


class CourseSerializer(serializers.ModelSerializer):
	'''
		A class to serialize data from Course model
	'''
	class Meta:
		model = Course
		fields = ['id','course_name', 'grade','description',
					'created', 'created_by']
		extra_kwargs = {
			"course_name": {
				"error_messages": {
					"blank": "Please provide the course name"
                }
            },
            "grade": {
				"error_messages": {
					"blank": "Please provide grade for the course"
                }
            },"description": {
				"error_messages": {
					"blank": "Please provide course description"
                }
            },

            }


class ChapterSerializer(serializers.ModelSerializer):
	'''
		A class to serialize data from Chapter model
	'''
	class Meta:
		model = Chapter
		fields = ('id','chapter_name', 'content', 'course')
		extra_kwargs = {
			"chapter_name": {
				"error_messages": {
					"blank": "Please provide the Chapter name"
                }
            }
        }


