from datetime import datetime

from django.db import models


class Question(models.Model):
    question_id = models.IntegerField(null=False)
    question = models.CharField(max_length=256, unique=True)
    answer = models.CharField(max_length=256, unique=True)
    created_at = models.DateTimeField()
    inserted_at = models.DateTimeField(default=datetime.now())
