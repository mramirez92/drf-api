from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from .models import Exercise


class ExerciseTests(APITestCase):
    @classmethod
    def set_user_test(cls):
        tester = get_user_model().objects.create_user(
            person='tester', password='uncommon'
        )
        tester.save()

        test_exercise = Exercise.objects.create(
            muscle_worked='Hamstring',
            exercise_name='Hamstring Curl',
            description='Seated Hamstring Curl Machine',
            sets='3',
            reps='12'
        )
        test_exercise.save()

    def test_get_exercise_list(self):
        response = self.client.get(reverse('exercise_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # exercise = response.data
        # self.assertEqual(len(exercise), 5)

    def test_get_exercise_by_id(self):
        response = self.client.get(reverse('exercise_detail', args='1'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        thing = response.data
        self.assertEqual(thing['weight'], 295)
