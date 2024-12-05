from django.contrib import admin
from django.urls import path, include

from courses.views import CourseListAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('courses.urls')),
]
