from authentication import views
from django.urls import path

# all auth urls

urlpatterns = [
    path("register/", views.RegisterAPIView.as_view(), name="register"),
    path("login/", views.LoginAPIView.as_view(), name="login"),
    path("check/", views.AuthUserAPIView.as_view(), name="check"),
    path("user/", views.UserAPIView.as_view(), name="user"),
    path(
        "specifci-user/<int:id>",
        views.UserSpecificAPIView.as_view(),
        name="specifci-user",
    ),
]
