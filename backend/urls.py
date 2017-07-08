from .views import ProblemList, SolutionList
from django.conf.urls import url

urlpatterns = [
        url(r'^problems/$', ProblemList.as_view(), name='problem_list'),
        url(r'^solutions/$', SolutionList.as_view(), name='solution_list'),
        ]
