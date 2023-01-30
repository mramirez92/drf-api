from django.contrib.auth import get_user_model
from django.db import models


class Exercise(models.Model):
    person = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    day_of_week = models.DateField(auto_now=True)
    muscle_worked = models.CharField(max_length=64)
    exercise_name = models.CharField(max_length=128)
    description = models.TextField()
    sets = models.IntegerField(help_text="Enter number")
    reps = models.IntegerField(help_text="Enter number")
    weight = models.IntegerField(help_text="Enter number in pounds", default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    update_ate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.exercise_name} Performed by: {self.person}  on {self.day_of_week}"

