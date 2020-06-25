from rest_framework import viewsets
from django.utils import timezone
from rest_framework.response import Response

from quizapp.models import (
    CategoryModel,
    QuestionQuizModel,
    Quiz,
)
from quizapp.api.serializers import (
    CategorySerializer,
    QuestionSerializer,
    QuizSerializer,
    LiveQuizSerializer,
    PastQuizSerializer
)


class CategoryViewset(viewsets.ModelViewSet):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer


class QuestionViewset(viewsets.ModelViewSet):
    queryset = QuestionQuizModel.objects.all()
    serializer_class = QuestionSerializer


class QuizViewset(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class LiveQuizViewset(viewsets.ModelViewSet):
    serializer_class = LiveQuizSerializer

    def get_queryset(self):
        current = timezone.now()
        queryset = Quiz.objects.filter(
            quiz_start_time__lte=timezone.now(), quiz_end_time__gte=timezone.now())
        return queryset


class PastQuizViewset(viewsets.ModelViewSet):
    serializer_class = PastQuizSerializer

    def get_queryset(self):
        current = timezone.now()
        queryset = Quiz.objects.filter(quiz_end_time__lte=timezone.now())
        return queryset

class UpcomingQuizViewset(viewsets.ModelViewSet):
    serializer_class = PastQuizSerializer

    def get_queryset(self):
        current = timezone.now()
        queryset = Quiz.objects.filter(quiz_start_time__gte=timezone.now())
        return queryset
