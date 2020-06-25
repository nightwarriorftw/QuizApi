from django.shortcuts import get_object_or_404
from rest_framework import serializers


from quizapp.models import (
    CategoryModel,
    QuestionQuizModel,
    AnswerModel,
    CategoryModel,
    QuestionModel,
)


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoryModel
        fields = '__all__'


class ChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = AnswerModel
        fields = ('answer_text',)


class OnlyQuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuestionModel
        fields = ('question_image', 'question_text',)


class QuestionSerializer(serializers.ModelSerializer):
    category = serializers.CharField()
    answer = serializers.CharField()
    choices = ChoiceSerializer(many=True, required=False,)
    question = OnlyQuestionSerializer()

    def get_category(self, instance):
        return instance.category.category_name

    def get_answer(self, instance):
        return instance.answer.answer_text

    class Meta:
        model = QuestionQuizModel
        fields = (
            'id',
            'category',
            'question',
            'answer',
            'choices',
        )
        extra_kwargs = {'choices': {'required': False}}

    def create(self, validated_data):
        # category = validated_data.pop('category', None)
        # question = validated_data.pop('question', None)
        # answer = validated_data.pop('answer', None)
        print(validated_data)
        return super().create(validated_data)
