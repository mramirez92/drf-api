from .models import Exercise
from rest_framework import generics
from .serializers import ExercisesSerializer


# from django.views.generic import ListView, DetailView


class ExerciseList(generics.ListCreateAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExercisesSerializer


class ExerciseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExercisesSerializer
