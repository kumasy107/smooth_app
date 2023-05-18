from django.shortcuts import render
from django.contrib.auth.views import TemplateView
from django.views.generic import DetailView, CreateView
from django.urls import reverse_lazy

from django.core.mail import EmailMessage
from django.template.loader import get_template


from .models import *
from .forms import *

class TopView(TemplateView):
    template_name='base/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = News.objects.all().order_by("-created_date")
        context['news_list'] = queryset
        return context

class NewsDetailView(DetailView):
    model = News
    template_name = 'base/news_detail.html'

class QuestionCreateView(CreateView):
    model = Question
    form_class = QuestionCreateForm
    template_name = 'base/question.html'
    success_url = reverse_lazy('base:home')

    def form_valid(self, form):
        # メール送信処理
        template = get_template('base/mail/question_mail.html')
        # mail_ctx={
        #     'name': form.cleaned_data['name'],
        #     'name_kana': form.cleaned_data['name_kana'],
        #     'color': form.cleaned_data['color'],
        # }
        mail_ctx = form.cleaned_data
        EmailMessage(
            subject='質問： ' + form.cleaned_data['title'],
            body=template.render(mail_ctx),
            from_email='teamoddshp@gmail.com',
            to=['yuto.k.h12@outlook.jp'],
            cc=[''],
            bcc=[''],
        ).send()

        return super().form_valid(form)