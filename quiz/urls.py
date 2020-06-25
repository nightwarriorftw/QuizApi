from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('quizapp.api.urls', namespace='quizapi')),
    path('accounts/api/',include('accounts.api.urls',namespace='accounts')),
]
