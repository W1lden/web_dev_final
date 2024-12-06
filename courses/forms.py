from django import forms
from django.contrib.auth.hashers import make_password
from .models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), label="Password")

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'is_student', 'is_instructor')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password_hash = make_password(self.cleaned_data['password'])  # Хэшируем пароль
        if commit:
            user.save()
        return user
