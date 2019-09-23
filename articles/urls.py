from django.urls import path

from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.ListView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('create', views.ArticleCreate.as_view(), name='create'),
    path('<int:pk>/edit', views.ArticleUpdate.as_view(), name='edit'),
    path('<int:pk>/delete', views.ArticleDelete.as_view(), name='delete'),
]