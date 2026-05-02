from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (ListView, 
                                  DetailView, 
                                  CreateView,
                                  UpdateView,
                                  DeleteView,   
                                  )   
from .models import Article
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.db.models import Q


# Create your views here.
class ArticleListView(ListView):
    model = Article
    template_name = 'article-list.html'
    paginate_by = 10
    ordering = ['-created_at']

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | Q(content__icontains=query)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('q', '')
        return context

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article-detail.html'   

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'article-create.html'
    fields = ['title', 'content', 'excerpt']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    template_name = 'article-update.html'
    fields = ['title', 'content', 'excerpt']

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)

class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'article-delete.html'
    success_url = reverse_lazy('article-list')

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)