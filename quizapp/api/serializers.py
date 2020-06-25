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
        fields = ('id', 'answer_text',)


class OnlyQuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuestionModel
        fields = ('id', 'question_image', 'question_text',)


class QuestionSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    answer = ChoiceSerializer()
    choices = ChoiceSerializer(many=True, required=False, read_only=False)
    question = OnlyQuestionSerializer()

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

    def update(self, instance, validated_data):
        category_instance = validated_data.get('category')
        category = CategoryModel.objects.get(id=self.instance.category.id)
        category.category_name = category_instance.pop('category_name')
        category.save()

        q_instance = validated_data.pop('question')
        q = QuestionModel.objects.get(id=self.instance.question.id)
        q.question_text = q_instance.pop('question_text')
        if q_instance.get('question_image'):
            q.question_image = q_instance.pop('question_image')
        q.save()

        answer_instance = validated_data.pop('answer')
        answer = AnswerModel.objects.get(id=self.instance.answer.id)
        answer_instance.answer_text = answer_instance.pop('answer_text')
        answer.save()

        choices = validated_data.pop('choices', [])
        c = []
        if(len(choices) > 0):
            for choice_data in choices:
                choice_instance = AnswerModel.objects.filter(
                   answer_text=choice_data.get('answer_text'))[1]
                if not choice_instance:
                    choice_instance = AnswerModel.objects.create(
                        answer_text=choice_data.get('answer_text'))
                choice_instance.answer_text = choice_data.pop('answer_text')
                choice_instance.save()
                c.append(choice_instance)

        question_instance = QuestionQuizModel.objects.get(
            id=self.instance.id)
        question_instance.category = category
        question_instance.question = q
        question_instance.answer = answer
        question_instance.choices.set(c)
        question_instance.save()
        return question_instance

    def create(self, validated_data):
        category = validated_data.pop('category')
        question = validated_data.pop('question')
        answer = validated_data.pop('answer')
        if category and question and answer:
            categoryObj = CategoryModel.objects.filter(
                category_name=category.pop('category_name'))[0]
            questionObj = QuestionModel.objects.create(
                question_text=question.pop('question_text'), question_image=question.pop('question_image', None))
            answerObj = AnswerModel.objects.create(
                answer_text=answer
            )
            choices_data = validated_data.pop('choices')
            if categoryObj is not None:
                obj = QuestionQuizModel.objects.create(
                    category=categoryObj, question=questionObj, answer=answerObj)
            print(len(choices_data))
            if len(choices_data) > 0:
                choices = []
                for choice_data in choices_data:
                    choice = AnswerModel.objects.create(
                        answer_text=choice_data.pop('answer_text'))
                    choices.append(choice)
                obj.choices.set(choices)

            return obj

        else:
            return serializers.ValidationError('Fields missing !!')
