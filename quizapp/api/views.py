from rest_framework import viewsets

from quizapp.models import (
    CategoryModel,
    QuestionQuizModel
)
from quizapp.api.serializers import (
    CategorySerializer,
    QuestionSerializer
)


class CategoryViewset(viewsets.ModelViewSet):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer


class QuestionSerializer(viewsets.ModelViewSet):
    queryset = QuestionQuizModel.objects.all()
    serializer_class = QuestionSerializer
