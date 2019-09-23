from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.utils import timezone
from django.urls import reverse

from .models import Article
from .forms import ArticleModelForm


class ListView(generic.ListView):
    context_object_name = 'latest_article_list'

    def get_queryset(self):
        """
        Return the last five published articles (not including those set to be
        published in the future).
        """
        return Article.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Article

    def get_queryset(self):
        """
        Excludes any articles that aren't published yet.
        """
        return Article.objects.filter(pub_date__lte=timezone.now())

class ArticleCreate(LoginRequiredMixin, generic.CreateView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    model = Article
    form_class = ArticleModelForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()        
        self.object = obj
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('articles:detail', kwargs={'pk': self.object.pk})

class ArticleUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Article
    form_class = ArticleModelForm

    def get_success_url(self):
        return reverse('articles:detail', kwargs={'pk': self.object.pk})

    def get_queryset(self):
        queryset = super(ArticleUpdate, self).get_queryset()
        return queryset.filter(author=self.request.user)

class ArticleDelete(LoginRequiredMixin, generic.DeleteView):
    model = Article
    form_class = ArticleModelForm

    def get_success_url(self):
        return reverse('articles:index')

    def get_queryset(self):
        queryset = super(ArticleDelete, self).get_queryset()
        return queryset.filter(author=self.request.user)