from django.urls import path
from .views import (NewsList, NewDetail, NewsCreate, NewsUpdate, NewsDelete, ArticleCreate, ArticleUpdate, ArticleDelete, CategoryListView, subscribe)


urlpatterns = [
   path('', NewsList.as_view(), name='post_list'),
   path('<int:pk>', NewDetail.as_view(), name='post_detail'),
   path('create/', NewsCreate.as_view(), name='news_create'),
   path('<int:pk>/update/', NewsUpdate.as_view(), name='news_update'),
   path('<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
   path('articlecreate/', ArticleCreate.as_view(), name='article_create'),
   path('<int:pk>/articleupdate/', ArticleUpdate.as_view(), name='article_update'),
   path('<int:pk>/articledelete/', ArticleDelete.as_view(), name='article_delete'),
   path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
   path('categories/<int:pk>/subscribe', subscribe, name='subscribe'),
]