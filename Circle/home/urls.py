from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    Notifications
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(),name='home'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
    path('post/new/',PostCreateView.as_view(),name='post-create'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'),
    path('about/',views.about,name='about'),
    path('notifications/',Notifications.as_view(),name='post-notifications'),
    path('loading/<int:pk>/',views.loading,name='loading'),
    path('confirming/<int:pk>/',views.confirming,name='confirming'),
]
