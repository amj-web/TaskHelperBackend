from api import views
from django.urls import path

# all urls are defined here

urlpatterns = [
    path("create-category/", views.CategoryAPIView.as_view(),
         name="create-category"),
    path("create-todo/", views.TodoAPIView.as_view(),
         name="create-todo"),
    path("unique-todo/<str:pk>", views.TodoSpecifcAPIView.as_view(),
         name="category"),
    path(
        "unique-category/<str:pk>",
        views.CategorySpecificAPIView.as_view(),
        name="category",
    ),
    path(
        "user-category/",
        views.CategoryUserSpecifcAPIView.as_view(),
        name="user-category",
    ),
    path("user-todo/", views.TodoUserSpecifcAPIView.as_view(),
         name="user-todo"),
    path(
        "current-user-category/",
        views.CategoryCurrentUserAPIView.as_view(),
        name="current-user-category",
    ),
    path(
        "current-user-todo/",
        views.ToDoCurrentUserAPIView.as_view(),
        name="current-user-todo",
    ),
    path(
        "todo-delete/", views.ToDoCurrentUserDeleteAPIView.as_view(),
        name="todo-delete"
    ),
    path(
        "category-delete/",
        views.CategoryCurrentUserDeleteAPIView.as_view(),
        name="category-delete",
    ),
]
