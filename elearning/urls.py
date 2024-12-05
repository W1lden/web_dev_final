from django.contrib import admin
from django.urls import path
from courses.views import course_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/', course_list, name='course_list'),
]
