import os

import requests
from django.contrib.sessions.backends import db
from django.http import HttpRequest, HttpResponse

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from questions.models import Question
from questions.serializers import QuestionSerializers


class QuestionViewSet(viewsets.ViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializers

    @action(methods=["post"], detail=False)
    def questions(self, request: HttpRequest, *args, **kwargs: dict) -> HttpResponse:
        if request.method == "POST":
            count = kwargs['question_num']

            url = 'https://jservice.io/api/random?count={}'
            res = requests.get(url.format(count)).json()

            context = {}
            context = {'question': Question.objects.order_by('id').last().question}

            for i in range(len(res)):
                if Question.objects.filter(question_id=res[i]['id']).exists():
                    while Question.objects.filter(question_id=res[i]['id']).exists():
                        res_repeated = requests.get(url.format(1)).json()
                    question = Question(
                        question_id=res_repeated[i]['id'],
                        question=res_repeated[i]['question'],
                        answer=res_repeated[i]['answer'],
                        created_at=res_repeated[i]['created_at']
                    )
                    question.save()
                else:
                    question = Question(
                        question_id=res[i]['id'],
                        question=res[i]['question'],
                        answer=res[i]['answer'],
                        created_at=res[i]['created_at']
                    )
                    question.save()

            return Response(context)
        else:
            return Response(
                {"error": f"Неправильный запрос"}, status.HTTP_400_BAD_REQUEST
            )
