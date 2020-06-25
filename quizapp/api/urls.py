from rest_framework import routers

from .views import (
    CategoryViewset,
    QuestionSerializer
)

app_name = 'quizapi'

router = routers.DefaultRouter()
router.register('category', CategoryViewset),
router.register('questions', QuestionSerializer),

urlpatterns = router.urls
