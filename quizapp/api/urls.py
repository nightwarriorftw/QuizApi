from rest_framework import routers

from .views import (
    CategoryViewset,
    QuestionViewset,
    QuizViewset,
    LiveQuizViewset,
    PastQuizViewset,
    UpcomingQuizViewset
)

app_name = 'quizapi'

router = routers.DefaultRouter()
router.register('category', CategoryViewset, basename='category'),
router.register('questions', QuestionViewset, basename='questions'),
router.register('quiz', QuizViewset, basename='quiz'),
router.register('live', LiveQuizViewset, basename='live'),
router.register('past', PastQuizViewset, basename='past'),
router.register('upcoming', UpcomingQuizViewset, basename='upcoming'),

urlpatterns = router.urls
