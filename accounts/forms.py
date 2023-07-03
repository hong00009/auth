from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        # fields = '__all__'
        fields = ('username', 'email', )

class CustomAuthenticationForm(AuthenticationForm):
    pass