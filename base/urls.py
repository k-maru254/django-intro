from django.urls import path
from .views import Home, students, HandleTeachers, HandleTeacher, HandleSubjects, HandleSubject, student, CreateSubjects
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("", Home, name="home"),
    path("students/", students, name="students"),
    path("students/<str:pk>", student, name="student"),
    path("teachers/", HandleTeachers.as_view(), name="teachers"),
    path("teachers/<str:pk>", HandleTeacher.as_view(), name="teacher"),
    path("subjects/", HandleSubjects.as_view(), name="subjects"),
    path("subjects/<str:pk>", HandleSubject.as_view(), name="subject"),
    path("create-subject/", CreateSubjects, name="create_subject"),
]
urlpatterns = format_suffix_patterns(urlpatterns)
