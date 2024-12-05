from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Course
from .serializers import CourseSerializer

class CourseListAPIView(APIView):
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

class CourseDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            course = Course.objects.get(pk=pk)
            serializer = CourseSerializer(course)
            return Response(serializer.data)
        except Course.DoesNotExist:
            return Response({'error': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)

