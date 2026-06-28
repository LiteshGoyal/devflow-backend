from django.urls import path

from apps.accounts.views import RegisterAPIView, LoginAPIView, MeAPIView, LogoutAPIView

urlpatterns = [
    path("register/",RegisterAPIView.as_view(),name="register",),
    path("login/",LoginAPIView.as_view(),name="login",),
    path("me/",MeAPIView.as_view(),name="me",),
    path("logout/",LogoutAPIView.as_view(),name="logout",),
    
]