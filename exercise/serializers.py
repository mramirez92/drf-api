from rest_framework import serializers

from .models import Exercise


class ExercisesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id', 'person', 'day_of_week', 'muscle_worked', 'exercise_name', 'description', 'sets', 'reps', 'weight')
        model = Exercise
