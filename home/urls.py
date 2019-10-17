from django.urls import path
from . import views
from .views import QuestionDetailView
from home import views as home_views

urlpatterns = [
    path('', views.home, name='home-homepage'),
    path('question/<int:pk>/', QuestionDetailView.as_view(), name='question-detail'),
]