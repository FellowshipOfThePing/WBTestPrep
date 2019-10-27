from django.urls import path
from home import views as home_views
from . import views


# Url Patterns relating to:
#           About View
#           Stats View
#           Question Views           


urlpatterns = [
    path('', views.startpage, name='home-startpage'),
    path('about/', home_views.about, name="about"),
    path('stats/<test_type>/<subject>/', home_views.stats, name="stats"),
    path('study/<test_type>/', home_views.study, name="study"),
    path('question/<test_type>/<int:orderId>/', views.QuestionDetailView, name='question-detail'),
    path('question/<test_type>/<int:orderId>/submitAnswer/', views.SubmitAnswer, name='question-submit'),
    path('question/<test_type>/<int:orderId>/result/', views.QuestionResultView, name='question-result'),
    path('questionCopy/<username>/<int:copyId>/', views.QuestionReview, name='question-review'),
]