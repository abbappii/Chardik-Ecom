from django.urls import path

from blog.views.blog_logic import (
    BlogListView, 
    BlogSingleView, 
    BlogUpdateView,
    BlogDeleteView, 
    BlogCreateView
)

urlpatterns = [ 
    path('create/',BlogCreateView.as_view()),
    path('list/view/', BlogListView.as_view()),
    path('single/view/<int:pk>/', BlogSingleView.as_view()),
    path('update/view/<int:pk>/', BlogUpdateView.as_view()),
    path('delete/view/<int:pk>/', BlogDeleteView.as_view()),


]
