from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class RegistrationForm(UserCreationForm):
    """User registration form"""

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email'
        )

