from django.contrib import admin

from django.urls import path
from rest_framework.routers import SimpleRouter

from questions.views import QuestionViewSet

router = SimpleRouter()


urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'api/v1/questions/<int:question_num>/', QuestionViewSet.as_view({"post": "questions"}))
]
