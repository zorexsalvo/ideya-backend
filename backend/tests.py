# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from .models import Problem, Solution

class ProblemTestCase(TestCase):
    def setUp(self):
        problem = Problem()
        problem.problem_id = 'P0001'
        problem.title = 'Setting up a testcase'
        problem.description = 'Creating test cases is hard'
        problem.created_by = 'thedeveloper'
        problem.save()

    def test_problem_model(self):
        pass

    def test_create_a_problem(self):
        problem = Problem()
        problem.title = 'Forgotten raincoat/umbrella on a rainy season'
        problem.description = 'In this era of rush, where everything had to move ' \
                'in an instant many of us became forgetful because we are rushing ' \
                'and umbrella is not an exception to that which is a very useful tool.' \
                'be it in a hot sunny weather or a stormy day.'
        problem.created_by = 'concerned_citizen'
        problem.save()

        print(problem.problem_id)

        self.assertEqual(2, Problem.objects.count())
        self.assertIsNotNone(problem.problem_id)

    def test_create_a_solution(self):
        problem = Problem.objects.filter(problem_id='P0001').first()

        solution = Solution()
        solution.problem = problem
        solution.description = 'None. Tests are inevitable.'
        solution.created_by = 'yoursenior'
        solution.save()
