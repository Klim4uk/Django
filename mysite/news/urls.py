from django.conf.urls import url, include
from django.urls import path, re_path
from django.views.generic import ListView, DetailView
from . import views

urlpatterns = [
    #  path('',
    #      ListView.as_view(queryset=Articles.objects.all().order_by('-data')[:20],
    #                       template_name='news/posts.html')),
    # re_path(r'^(?P<pk>\d+)$', DetailView.as_view(model = Articles, template_name = 'news/post.html')),

    path('', views.news_list, name="list_news"),
    path('single/<int:pk>', views.new_single, name="new_single"),
    path('filter/<int:pk>', views.news_filter, name="news_filter"),
]


