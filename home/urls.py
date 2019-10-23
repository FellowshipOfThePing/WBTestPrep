from django.urls import path
from . import views
from .views import QuestionView, QuestionResultView, SubmitAnswer, QuestionReview
from home import views as home_views

urlpatterns = [
    path('', views.startpage, name='home-startpage'),
    path('about/', home_views.about, name="about"),
    path('question/<test_type>/<int:orderId>/', QuestionView, name='question-detail'),
    path('question/<test_type>/<int:orderId>/submitAnswer/', SubmitAnswer, name='question-submit'),
    path('question/<test_type>/<int:orderId>/result/', QuestionResultView, name='question-result'),
    path('questionCopy/<username>/<int:copyId>/', QuestionReview, name='question-review'),
]