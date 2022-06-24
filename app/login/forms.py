from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import CharField, PasswordInput
from .models import Account


class RegisterForm(UserCreationForm):
    password1 = CharField(label="Password", widget=PasswordInput)

    def __init__(self, *args, **kwargs) -> None:
        super(RegisterForm, self).__init__(*args, **kwargs)
        del self.fields["password2"]

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.staff = True
        if commit:
            user.save()
        return user

    class Meta:
        model = Account
        fields = ["username", "email"]


class LoginForm(AuthenticationForm):
    class Meta:
        model = Account
        fields = ["username", "password"]
