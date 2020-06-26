from rest_framework import viewsets
from django.utils import timezone
from rest_framework.response import Response
from rest_framework import permissions

from quizapp.models import (
    CategoryModel,
    QuestionQuizModel,
    Quiz,
    QuizTakers
)
from quizapp.api.serializers import (
    CategorySerializer,
    QuestionSerializer,
    QuizSerializer,
    LiveQuizSerializer,
    PastQuizSerializer,
    QuizTakerSerializer
)


class CategoryViewset(viewsets.ModelViewSet):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAuthenticated,)


class QuestionViewset(viewsets.ModelViewSet):
    queryset = QuestionQuizModel.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (permissions.IsAuthenticated,)


class QuizViewset(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = (permissions.IsAuthenticated,)


class LiveQuizViewset(viewsets.ModelViewSet):
    serializer_class = LiveQuizSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        current = timezone.now()
        queryset = Quiz.objects.filter(
            quiz_start_time__lte=timezone.now(), quiz_end_time__gte=timezone.now())
        return queryset


class PastQuizViewset(viewsets.ModelViewSet):
    serializer_class = PastQuizSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        current = timezone.now()
        queryset = Quiz.objects.filter(quiz_end_time__lte=timezone.now())
        return queryset


class UpcomingQuizViewset(viewsets.ModelViewSet):
    serializer_class = PastQuizSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        current = timezone.now()
        queryset = Quiz.objects.filter(quiz_start_time__gte=timezone.now())
        return queryset

class QuizTakersViewsets(viewsets.ModelViewSet):
    serializer_class = QuizTakerSerializer
    permission_classes = (permissions.IsAuthenticated,)
    
    def get_queryset(self):
        return QuizTakers.objects.filter(user=self.request.user)
