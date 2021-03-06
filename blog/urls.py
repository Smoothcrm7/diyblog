from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.BlogListView.as_view(), name='blog'),
    path('blog/<int:pk>', views.BlogDetailView.as_view(), name='blog-detail'),
    path('bloggers/', views.ProfileListView.as_view(), name='profile-list'),
    path('bloggers/<int:pk>', views.ProfileDetailView.as_view(), name='profile-detail'),
    path('blog/<int:pk>/create/', views.add_comment_to_post, name='add_comment_to_post'),
]