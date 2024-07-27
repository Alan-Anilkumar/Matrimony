from django.db import models
from django.contrib.auth.models import AbstractUser


class UserHobby(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class UserInterest(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class CustomUser(AbstractUser):
    SMOKING_HABIT_CHOICES = (
        ("NON-SMOKER", "Non Smoker"),
        ("OCCASIONALLY", "Occasionally"),
        ("REGULAR", "Regular"),
        ("WANTING TO QUIT", "Wanting To Quit"),
    )
    phone_number = models.IntegerField()
    date_of_birth = models.DateField()
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=[("M", "Male"), ("F", "Female")])
    hobbies = models.ManyToManyField(
        UserHobby, blank=True, related_name="user_hobbies"
    )
    profile_picture = models.ImageField(
        upload_to="profile_pictures",
        blank=True,
        default="profile_pictures/user_default.png",
    )
    qualification = models.CharField(max_length=100)
    smoking_habits = models.CharField(
        max_length=20, choices=SMOKING_HABIT_CHOICES, null=True
    )
    interests = models.ManyToManyField(
        UserInterest, blank=True, related_name="user_interests"
    )

    def __str__(self):
        return self.username
