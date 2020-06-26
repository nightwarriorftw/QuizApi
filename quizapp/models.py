from django.db import models
from django.contrib.auth.models import User

# Category of the questions
class CategoryModel(models.Model):
    category_name = models.CharField(max_length=70)

    def __str__(self):
        return self.category_name

class QuestionModel(models.Model):
    question_image = models.ImageField(null=True, blank=True)
    question_text = models.CharField(max_length=250)

    def __str__(self):
        return self.question_text

# Answer of a single question
class AnswerModel(models.Model):
    answer_text = models.CharField(max_length=250)

    def __str__(self):
        return self.answer_text


# Questions
class QuestionQuizModel(models.Model):
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    question = models.ForeignKey(QuestionModel, on_delete=models.CASCADE)
    answer = models.OneToOneField(
        AnswerModel, on_delete=models.CASCADE, related_name='correct_answer', null=True, blank=True)
    choices = models.ManyToManyField(
        'AnswerModel',related_name='choices', blank=True)

    def __str__(self):
        return self.question.question_text



# Quiz
class Quiz(models.Model):
    questions = models.ManyToManyField(
        QuestionQuizModel, related_name='questions')
    quiz_name = models.CharField(max_length=250)
    quiz_start_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    quiz_end_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    quiz_creation_time = models.DateTimeField(auto_now_add=True)
    quiz_updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Quizes'

    def __str__(self):
        return self.quiz_name


class QuizTakers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    answer_count = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)
    completion_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
