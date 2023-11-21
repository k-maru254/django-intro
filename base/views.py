from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Subject, Student, Teacher
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .serializers import StudentSerializer, TeachersSerializer, SubjectSerializer


# Create your views here.


def Home(request):
    api_routes = [
        "/api",
        "/api/students",
        "/api/Teachers",
        "/api/subjects"
    ]
    return Response(api_routes)


class HandleTeachers(APIView):

    def get(self, request, format=None):
        teachers_queryset = Teacher.objects.all()
        serialized_teachers_data = TeachersSerializer(
            teachers_queryset, many=True)
        return Response(serialized_teachers_data.data)

    def post(self, request, format=None):
        posted_teacher_data = request.data
        serialized_posted_teacher = TeachersSerializer(
            data=posted_teacher_data)
        if serialized_posted_teacher.is_valid():
            serialized_posted_teacher.save()
            print(serialized_posted_teacher.data)
            return Response(serialized_posted_teacher.data, status=status.HTTP_201_CREATED)
        return Response(serialized_posted_teacher.errors, status=status.HTTP_400_BAD_REQUEST)


class HandleTeacher(APIView):

    def get_teacher(self, pk):
        try:
            return Teacher.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        teacher_data = self.get_teacher(pk)
        serialized_teacher_data = TeachersSerializer(teacher_data)
        return Response(serialized_teacher_data.data)

    def put(self, request, pk, format=None):
        teacher_data = self.get_teacher(pk)
        teacher_new_data = request.data
        serialized_teacher = TeachersSerializer(
            teacher_data, data=teacher_new_data)
        if serialized_teacher.is_valid():
            serialized_teacher.save()
            return Response(serialized_teacher, status=status.HTTP_202_ACCEPTED)
        return Response(serialized_teacher.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, formrmat=None):
        teacher_data = self.get_teacher(pk)
        teacher_data.delete()
        return Response(status=status.HTTP_200_OK)


@api_view(["GET", "POST"])
def students(req, format=None):

    if req.method == "GET":
        all_students = Student.objects.all()
        serialized_students = StudentSerializer(all_students, many=True)
        return Response(serialized_students.data)

    elif req.method == "POST":
        posted_data = req.data
        print(posted_data)
        serialized_posted_data = StudentSerializer(data=posted_data)
        if serialized_posted_data.is_valid():
            serialized_posted_data.save()
            print(serialized_posted_data.data)
            return Response(status=status.HTTP_201_CREATED)
    else:
        return HttpResponse("No requesr")


class HandleSubjects(APIView):

    def get(self, request, format=None):
        subjects_queryset = Subject.objects.all()
        serialized_subjects = SubjectSerializer(subjects_queryset, many=True)
        return Response(serialized_subjects.data)

    def post(self, request, format=None):
        posted_data = request.data
        print(posted_data)
        serialized_posted_data = SubjectSerializer(data=posted_data)
        if serialized_posted_data.is_valid():
            serialized_posted_data.save()
            return Response(serialized_posted_data.data, status=status.HTTP_201_CREATED)
        return Response(serialized_posted_data.errors, status=status.HTTP_400_BAD_REQUEST)


class HandleSubject(APIView):

    def get_subjects(self, pk):
        try:
            return Subject.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk, format=None):
        subject_data = self.get_subjects(pk)
        serealized_subject = SubjectSerializer(subject_data)
        print(serealized_subject)
        return Response(serealized_subject.data)

    def put(self, request, pk, format=None):
        subject_data = self.get_subjects(pk)
        posted_subject_data = request.data
        serialized_subject = SubjectSerializer(
            subject_data, data=posted_subject_data)
        if serialized_subject.is_valid():
            serialized_subject.save()
            return Response(serialized_subject.data, status=status.HTTP_201_CREATED)
        return Response(serialized_subject.error, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        subject_data = self.get_subjects(pk)
        subject_data.delete()
        return Response(status=status.HTTP_202_ACCEPTED)


@api_view(["GET", "PUT", "DELETE"])
def student(request, pk, format=None):
    try:
        student_object = Student.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    #  retrieve a single data from the database
    if request.method == "GET":
        serialized_student_data = StudentSerializer(student_object, many=False)
        return Response(serialized_student_data.data)

    # edit a field in the row in the database
    if request.method == "PUT":
        new_student_data = request.data
        serialized_new_student = StudentSerializer(
            student_object, new_student_data)

        if serialized_new_student.is_valid():
            serialized_new_student.save()
            return Response(serialized_new_student.data, status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    # Execute delete
    if request.method == "DELETE":
        student_object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def subjects(request):

    return HttpResponse("Subject API")


def CreateSubjects(request):

    # Listing all subjects in the school
    subjects = [
        {
            "name": "Mathematics",
            "code": 1001
        },
        {
            "name": "English",
            "code": 1002
        },
        {
            "name": "Kiswahili",
            "code": 1003
        },
        {
            "name": "Biology",
            "code": 1004
        },
        {
            "name": "Physics",
            "code": 1005
        },
        {
            "name": "Chemistry",
            "code": 1006
        },
        {
            "name": "History",
            "code": 1007
        }
    ]

    for subject in subjects:
        try:
            # adding all the subjests to the database
            Subject.objects.create(
                name=subject["name"], subject_code=subject["code"])
        except:
            return HttpResponse("Error occured while adding subjects to database")
    return HttpResponse("Subjects added successfully")
