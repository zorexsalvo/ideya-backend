# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Problem(models.Model):
    CATEGORIES = (
        ('HEALTH', 'Health'),
        ('ECONOMY', 'Economy'),
        ('EDUCATION', 'Education'),
        ('MEDIA', 'Media'),
        ('COMMUNITY', 'Community'),
        ('ENVIRONMENT', 'Environment')
    )

    problem_id = models.CharField(max_length=255, unique=True, blank=True, null=True)
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255, choices=CATEGORIES, default='HEALTH')
    description = models.TextField(max_length=255)
    created_by = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        super(Problem, self).save(*args, **kwargs)

        if not self.problem_id:
            self.problem_id = '{0:05d}'.format(self.id)
            Problem.objects.filter(id=self.id).update(problem_id=self.problem_id)


class Solution(models.Model):
    problem = models.ForeignKey('Problem', related_name='solutions')
    description = models.CharField(max_length=100)
    created_by = models.CharField(max_length=100)
