from django.contrib import admin
from .models import (
    CategoryModel,
    AnswerModel,
    QuestionModel,
    Quiz,
    QuizTakers,
    QuestionQuizModel
)

class CategoryAdmin(admin.ModelAdmin):
    class Meta:
        model = CategoryModel
        fields = '__all__'

admin.site.register(CategoryModel, CategoryAdmin)
admin.site.register(AnswerModel)
admin.site.register(QuestionModel)
admin.site.register(Quiz)
admin.site.register(QuizTakers)
admin.site.register(QuestionQuizModel)
