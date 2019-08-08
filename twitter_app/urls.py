from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('posts-by/<str:username>/', views.UserPostListView.as_view(), name='user_posts'),
    path('post/new', views.PostCreateView.as_view(), name='post_create'),
    path('about/', views.about, name='about'),
]