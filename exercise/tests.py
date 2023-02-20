from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from .models import Exercise


class ExerciseTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        tester = get_user_model().objects.create_user(
            username='USERNAME1', password='uncommon'
        )
        tester.save()

        test_exercise = Exercise.objects.create(
            person=tester,
            muscle_worked='Hamstring',
            exercise_name='Hamstring Curl',
            description='Seated Hamstring Curl Machine',
            weight=70,
            sets=3,
            reps=12,
        )
        test_exercise.save()

    def test_get_exercise(self):
        response = self.client.get(reverse('exercise_detail', args=(1,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        thing = response.data
        self.assertEqual(thing['weight'], 70)

    def test_get_exercise_list(self):
        response = self.client.get(reverse('exercise_list'), args=(1,))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.data
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["muscle_worked"], "Hamstring")

    def test_create(self):
        url = reverse("exercise_list")
        data = {"person": 1, "muscle_worked": "quads, hamstring", "weight": 135, "sets": 4, "reps": 12,
                "exercise_name": "leg press", "description": "leg press machine"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        data = Exercise.objects.all()
        self.assertEqual(len(data), 2)
        self.assertEqual(Exercise.objects.get(id=2).description, "leg press machine")

    def test_update_thing(self):
        url = reverse("exercise_detail", args=(1,))
        data = {"person": 1, "muscle_worked": "Hamstring", "weight": 75, "sets": 3, "reps": 10,
                "exercise_name": "Hamstring Curl", "description": "Seated Hamstring Curl Machine"}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        update = Exercise.objects.get(id=1)
        self.assertEqual(update.muscle_worked, data["muscle_worked"])
        self.assertEqual(update.weight, data["weight"])
        self.assertEqual(update.reps, data["reps"])

    def test_delete_thing(self):
        url = reverse("exercise_detail", args=(1,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        deleted = Exercise.objects.all()
        self.assertEqual(len(deleted), 0)
