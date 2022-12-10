from django.contrib.auth.forms import UserCreationForm
from .models import User


class UserRegForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "password1", "password2")
    