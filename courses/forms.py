from django import forms
from django.contrib.auth.hashers import make_password
from .models import User

class UserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), label="Password")

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'is_student', 'is_instructor')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password_hash = make_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'is_student', 'is_instructor')
