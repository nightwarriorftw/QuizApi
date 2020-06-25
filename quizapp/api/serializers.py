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
        category = validated_data.pop('category')
        question = validated_data.pop('question')
        answer = validated_data.pop('answer')
        categoryObj = CategoryModel.objects.filter(category_name=category)[0]
        questionObj = QuestionModel.objects.create(
            question_text=question.pop('question_text'), question_image=question.pop('question_image', None))
        answerObj = AnswerModel.objects.create(
            answer_text = answer
        )
        choices_data = validated_data.pop('choices')
        if categoryObj is not None:
            obj = QuestionQuizModel.objects.create(category=categoryObj, question=questionObj, answer=answerObj)
        print(len(choices_data))
        if len(choices_data) > 0 :
            choices = []
            for choice_data in choices_data:
                # choice_id = choice_data.pop('id', None)
                choice= AnswerModel.objects.create(answer_text=choice_data.pop('answer_text'))
                print(choice)
                choices.append(choice)
            obj.choices.set(choices)
        
        return obj
