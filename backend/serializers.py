from .models import Problem, Solution
from rest_framework import serializers


class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = ('id', 'title', 'description', 'created_by')


class SolutionSerializer(serializers.ModelSerializer):
    problem = serializers.SlugRelatedField(
        queryset=Problem.objects.all(),
        slug_field='problem_id'
    )

    class Meta:
        model = Solution
        fields = ('problem', 'description', 'created_by')
