from django.urls import path
from .views import CourseListView, CourseDetailView

urlpatterns = [
    path('courses/', CourseListView.as_view(), name='course_list'),
    path('courses/<int:course_id>/', CourseDetailView.as_view(), name='course_detail'),
]
