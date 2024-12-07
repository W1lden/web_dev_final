from django.shortcuts import render, get_object_or_404
from django.views import View
from rest_framework import viewsets
from .models import Course, User
from .serializers import CourseSerializer, UserSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CourseListView(View):
    def get(self, request):
        courses = Course.objects.all()
        return render(request, 'courses/course_list.html', {'courses': courses})

class CourseDetailView(View):
    def get(self, request, course_id):
        course = get_object_or_404(Course, pk=course_id)
        return render(request, 'courses/course_detail.html', {'course': course})
