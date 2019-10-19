from django.urls import path
from . import views
from .views import QuestionView, QuestionResultView, SubmitAnswer, QuestionReview
from home import views as home_views

urlpatterns = [
    path('', views.home, name='home-homepage'),
    path('question/<int:orderId>/', QuestionView, name='question-detail'),
    path('question/<int:orderId>/submitAnswer/', SubmitAnswer, name='question-submit'),
    path('question/<int:orderId>/result/', QuestionResultView, name='question-result'),
    path('questionCopy/<username>/<int:copyId>/', QuestionReview, name='question-review'),
]