from django.urls import path
from .views import *
from django.contrib.auth.views import TemplateView


app_name = 'base'

urlpatterns = [
		# path('', views.TopicListView.as_view(), name='top'),
		# 以下のように，urls.pyだけで完結させることも可能
        path('', TopView.as_view(), name='home'),
        path('news/<int:pk>/', NewsDetailView.as_view(), name="news_detail"),
        path('notisave/privacy_policy/', TemplateView.as_view(template_name='base/privacy_notisave.html'), name='privacy_notisave'),
        path('smooth/privacy_policy/', TemplateView.as_view(template_name='base/privacy_smooth.html'), name='privacy_smooth'),
        path('privacy_policy', TemplateView.as_view(template_name='base/privacy_list.html'), name='privacy_list'),
        path('question/', QuestionCreateView.as_view(), name="question"),
]