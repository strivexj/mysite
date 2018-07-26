from django.contrib.auth.forms import UserCreationForm


class RegisterationForm(UserCreationForm):
    class Meta:
        fields = ("username", "email")
