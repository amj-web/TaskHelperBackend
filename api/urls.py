from api import views
from django.urls import path


urlpatterns=[
    path('create-category/',views.CategoryAPIView.as_view(),name="create-category"),
    path('create-todo/',views.TodoAPIView.as_view(),name="create-todo"),
]