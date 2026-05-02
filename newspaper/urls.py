from django.urls import path
from .views import (ArticleListView, 
                    ArticleDetailView, 
                    ArticleCreateView, 
                    ArticleUpdateView,
                    )

urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('articulos/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('articulos/crear/', ArticleCreateView.as_view(), name='article-create'),
    path('articulos/<int:pk>/actualizar/', ArticleUpdateView.as_view(), name='article-update'),
]