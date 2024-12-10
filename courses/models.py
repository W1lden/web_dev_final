from django.db import models
from django.contrib.auth.hashers import make_password

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password_hash = models.CharField(max_length=255)
    is_student = models.BooleanField(default=True)
    is_instructor = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Проверяем, хэширован ли уже пароль
        if not self.password_hash.startswith('pbkdf2_'):
            self.password_hash = make_password(self.password_hash)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)  
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Course(models.Model):
    course_id = models.AutoField(primary_key=True)  
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, 
    limit_choices_to={'is_instructor': True})

    def __str__(self):
        return self.title


class Lesson(models.Model):
    lesson_id = models.AutoField(primary_key=True)  
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    video_url = models.URLField()

    def __str__(self):
        return self.title

class Enrollment(models.Model):
    enrollment_id = models.AutoField(primary_key=True)  
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50, default="active")

    def __str__(self):
        return f"{self.user.username} -> {self.course.title}"



class Review(models.Model):
    review_id = models.AutoField(primary_key=True) 
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} for {self.course.title}"


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)  
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50, default="completed")

    def __str__(self):
        return f"Payment by {self.user.username}"

class Quiz(models.Model):
    quiz_id = models.AutoField(primary_key=True)  
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    total_marks = models.IntegerField()

    def __str__(self):
        return self.title

class QuizQuestion(models.Model):
    question_id = models.AutoField(primary_key=True)  
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_text = models.TextField()
    option_a = models.CharField(max_length=200)
    option_b = models.CharField(max_length=200)
    option_c = models.CharField(max_length=200)
    option_d = models.CharField(max_length=200)
    correct_option = models.CharField(max_length=1)

    def __str__(self):
        return f"Question for {self.quiz.title}"


class UserProgress(models.Model):
    progress_id = models.AutoField(primary_key=True)  
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    completed_lessons = models.IntegerField(default=0)
    quiz_scores = models.JSONField(default=dict)

    def __str__(self):
        return f"Progress of {self.user.username} in {self.course.title}"
