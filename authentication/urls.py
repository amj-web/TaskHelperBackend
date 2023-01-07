from authentication import views
from django.urls import path


urlpatterns=[
    path('register/',views.RegisterAPIView.as_view(),name="register"),
    # path('login/',views..as_view(),name="login"),
    # path('check/',views..as_view(),name="check"),
    # path('user/',views..as_view(),name="user"),
]