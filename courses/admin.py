from django.contrib import admin
from .models import (
    User, Category, Course, Lesson, Enrollment,
    Review, Payment, Quiz, QuizQuestion, UserProgress
)
from .forms import UserCreationForm, UserForm

class UserAdmin(admin.ModelAdmin):
    form = UserForm  # Форма для редактирования существующих пользователей
    add_form = UserCreationForm  # Форма для создания новых пользователей

    list_display = ('username', 'email', 'is_student', 'is_instructor')

    def get_form(self, request, obj=None, **kwargs):
        """Используем разные формы для добавления и изменения пользователей."""
        if obj is None:
            kwargs['form'] = self.add_form
        else:
            kwargs['form'] = self.form
        return super().get_form(request, obj, **kwargs)

    def get_fieldsets(self, request, obj=None):
        """Определяем разные наборы полей для добавления и редактирования."""
        if obj is None:
            return [
                (None, {
                    'fields': ('username', 'email', 'password', 'is_student', 'is_instructor'),
                }),
            ]
        else:
            return [
                (None, {
                    'fields': ('username', 'email', 'is_student', 'is_instructor'),
                }),
            ]

admin.site.register(User, UserAdmin)

# Регистрация остальных моделей
admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Enrollment)
admin.site.register(Review)
admin.site.register(Payment)
admin.site.register(Quiz)
admin.site.register(QuizQuestion)
admin.site.register(UserProgress)
