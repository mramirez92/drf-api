from .models import Exercise
from django.views.generic import ListView, DetailView


class ExerciseList(ListView):
    model = Exercise


class ExerciseDetail(DetailView):
    model = Exercise
