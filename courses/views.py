from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Course

class CourseListView(View):
    def get(self, request):
        courses = Course.objects.all()
        return render(request, 'courses/course_list.html', {'courses': courses})

class CourseDetailView(View):
    def get(self, request, course_id):
        course = get_object_or_404(Course, pk=course_id)
        return render(request, 'courses/course_detail.html', {'course': course})
