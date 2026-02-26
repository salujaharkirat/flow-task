# authentication/urls.py

from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView, LogoutView, PasswordChangeView, UserDetailsView
from django.urls import path


urlpatterns = [
  path("register/", RegisterView.as_view(), name="rest_register"),
  path("login/", LoginView.as_view(), name="rest_login"),
  path("logout/", LogoutView.as_view(), name="rest_logout"),
  path("user/", UserDetailsView.as_view(), name="rest_user_details"),
  path("password/change/", PasswordChangeView.as_view(), name="password_reset"),
]