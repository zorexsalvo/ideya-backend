from django.urls import reverse
from rest_framework.test import APIClient
from django.test import TestCase
from backend.models import Problem, Solution

class SerializerTestCase(TestCase):
    def setUp(self):
        problem = Problem()
        problem.problem_id = 'P0001'
        problem.title = 'Setting up a testcase'
        problem.description = 'Creating test cases is hard'
        problem.created_by = 'thedeveloper'
        problem.save()

    def test_get_problems(self):
        url = reverse('problem_list')
        client = APIClient()
        response = client.get(url)

        self.assertEqual(1, len(response.json()))

    def test_create_problem(self):
        url = reverse('problem_list')
        client = APIClient()
        payload = {
            'title': 'We the Best Music',
            'description': 'Another one!',
            'created_by': 'DJ Khaled'
        }

        response = client.post(url, data=payload, format='json')
        self.assertEqual(201, response.status_code)
