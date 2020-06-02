'''
    A serializer to serialize data from Course, Grade and Chapter models
    and parse json to the view.
'''


from rest_framework import serializers
from .models import Course, Chapter, Grade


class GradeSerializer(serializers.ModelSerializer):
    '''
    A class to serialize data from Grade model
    '''
    id = serializers.ReadOnlyField()

    class Meta:
        model = Grade
        fields = ['id', 'grade_name']
        extra_kwargs = {
            "grade_name": {
                "error_messages": {
                    "blank": "Please provide the grade name!"
                }
            }
        }

    def create(self, validated_data):
        '''
        Create the Grade instance
        '''
        grade = Grade.objects.create(grade_name=validated_data['grade_name'])
        return grade

    def update(self, instance, validated_data):
        '''
        Update the Grade instance
        '''
        instance.grade_name = validated_data['grade_name']
        instance.save()
        return instance


class CourseSerializer(serializers.ModelSerializer):
    '''
    A class to serialize data from Course model
    '''
    id = serializers.ReadOnlyField()
    created = serializers.ReadOnlyField()

    class Meta:
        model = Course
        fields = ['id', 'course_name', 'grade', 'description',
                  'created', 'created_by']
        extra_kwargs = {
            "course_name": {
                "error_messages": {
                    "blank": "Please provide the course name!"
                }
            },
            "grade": {
                "error_messages": {
                    "blank": "Please provide grade for the course!"
                }
            }, "description": {
                "error_messages": {
                    "blank": "Please provide course description!"
                }
            },

        }

    def create(self, validated_data):
        '''
        Create the Course instance
        '''
        course = Course.objects.create(course_name=validated_data['course_name'],
                                       grade=validated_data['grade'],
                                       description=validated_data['description'],
                                       created_by=validated_data['created_by'])
        return course

    def update(self, instance, validated_data):
        '''
        Update the Course instance
        '''
        instance.course_name = validated_data['course_name']
        instance.grade = validated_data['grade']
        instance.description = validated_data['description']
        instance.save()
        return instance


class ChapterSerializer(serializers.ModelSerializer):
    '''
    A class to serialize data from Chapter model
    '''
    id = serializers.ReadOnlyField()

    class Meta:
        model = Chapter
        fields = ('id', 'chapter_name', 'content', 'course')
        extra_kwargs = {
            "chapter_name": {
                "error_messages": {
                    "blank": "Please provide the Chapter name!"
                }
            },
            "content": {
                "error_messages": {
                    "blank": "Content cannot be blank!"
                }
            }
        }

    def create(self, validated_data):
        '''
        Create the Chapter instance
        '''
        chapter = Chapter.objects.create(chapter_name=validated_data['chapter_name'],
                                         content=validated_data['content'],
                                         course=validated_data['course'])
        return chapter

    def update(self, instance, validated_data):
        '''
        Update the Chapter instance
        '''
        instance.chapter_name = validated_data['chapter_name']
        instance.content = validated_data['content']
        instance.course = validated_data['course']
        instance.save()
        return instance
