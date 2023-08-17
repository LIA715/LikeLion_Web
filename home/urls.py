from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.PostDetail.as_view()),
    path('', views.index),
    path('create_post/', views.PostCreate.as_view()),
    path('api/', views.ListPost.as_view()),
    path('api/<int:pk>/', views.DetailPost.as_view())
]