from django.urls import path
from django.contrib import admin
from .views import CourseListView, CourseDetailView, CourseViewSet, UserViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='course')
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CourseListView.as_view(), name='course_list'),
    path('courses/<int:course_id>/', CourseDetailView.as_view(), name='course_detail'),
    path('api/', include(router.urls)),
]
