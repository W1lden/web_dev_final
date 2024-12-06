from django.contrib import admin
from .models import (
    User, Category, Course, Lesson, Enrollment,
    Review, Payment, Quiz, QuizQuestion, UserProgress
)
from django.contrib import admin
from .models import User
from .forms import UserForm

class UserAdmin(admin.ModelAdmin):
    form = UserForm  # Используем кастомную форму
    fields = ('username', 'email', 'is_student', 'is_instructor')  # Исключаем поле "password"
    list_display = ('username', 'email', 'is_student', 'is_instructor')  # Поля в списке пользователей



admin.site.register(User, UserAdmin)

admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Enrollment)
admin.site.register(Review)
admin.site.register(Payment)
admin.site.register(Quiz)
admin.site.register(QuizQuestion)
admin.site.register(UserProgress)
