from .serializers import ProblemSerializer, SolutionSerializer
from .models import Problem, Solution
from rest_framework import generics

class ProblemList(generics.ListCreateAPIView):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer


class SolutionList(generics.ListCreateAPIView):
    queryset = Solution.objects.all()
    serializer_class = SolutionSerializer
