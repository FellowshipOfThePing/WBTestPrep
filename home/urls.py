from django.urls import path
from . import views
from .views import QuestionView, QuestionResultView, SubmitAnswer
from home import views as home_views

urlpatterns = [
    path('', views.home, name='home-homepage'),
    path('question/<int:pk>/', QuestionView, name='question-detail'),
    path('question/<int:pk>/submitAnswer/', SubmitAnswer, name='question-submit'),
    path('question/<int:pk>/result/', QuestionResultView, name='question-result'),
]