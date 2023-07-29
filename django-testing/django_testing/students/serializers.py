from rest_framework import serializers
from django.conf import settings
from students.models import Course, Student
from rest_framework.exceptions import ValidationError


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ("id", "name", "students")

    def validate(self, data):
        if 'students' in [data]:
            count_students = len(data.get('students'))
            if count_students > settings.MAX_STUDENTS_PER_COURSE:
                raise ValidationError(
                    f'Невозможно добавить более {settings.MAX_STUDENTS_PER_COURSE} студентов на курс.')
        return data
