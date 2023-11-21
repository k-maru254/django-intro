from rest_framework import serializers
from .models import Student, Subject, Teacher


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class TeachersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = "__all__"


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"
