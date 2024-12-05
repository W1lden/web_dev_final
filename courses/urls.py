from django.urls import path
from .views import CourseListAPIView, CourseDetailAPIView

urlpatterns = [
    path('api/courses/', CourseListAPIView.as_view(), name='course_list_api'),
    path('api/courses/<int:pk>/', CourseDetailAPIView.as_view(), name='course_detail_api'),
]
