# from django.shortcuts import render, get_object_or_404, redirect, render_to_response
# from .models import Quiz, Question, Answer, QuizAttempt, QuestionAttempt
# from django.views.generic import ListView
# from .forms import QuizForm
# from django.contrib.auth import LoginRequiredMixin

# class QuizView(LoginRequiredMixin, ListView):
#     model = Quiz
#     form = QuizForm(questions=self.question_set.all())





# # def render_quiz(request, pk):
# #     quiz = get_object_or_404(Quiz)
# #     form = QuizForm(questions=quiz.question_set.all())
# #     if request.method == "POST":
# #         form = QuizForm(request.POST, questions=quiz.question_set.all())
# #         if form.is_valid(): ## Will only ensure the option exists, not correctness.
# #             attempt = form.save()
# #             return redirect(attempt)
# #     return render_to_response('quiz.html', {"form": form})