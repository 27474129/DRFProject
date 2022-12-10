from django.urls import path
from .views import UserRegView, UserAuthView, UserLogoutView, AccessFailedView


urlpatterns = [
    path("reg/", UserRegView.as_view(), name="reg_page"),
    path("auth/", UserAuthView.as_view(), name="auth_page"),
    path("logout/", UserLogoutView.as_view(), name="logout_page"),
    path("access_failed/", AccessFailedView.as_view(), name="access_failed_page"),
]
