from django.core.exceptions import ValidationError
from django.contrib.auth.models import Group
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django import forms

from .models import User


class UserCreationForm(forms.ModelForm):  # Create User in admin panel

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ('email', 'phone_number', 'full_name')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError('A user with that email already exists.')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")

        if len(password1) < 8:
            raise ValidationError(
                "Password must be at least 8 characters long.")

        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField(
        help_text="You can change password using <a  href=\"../password/\" >this form</a>.")

    class Meta:
        model = User
        fields = ('email', 'phone_number', 'full_name',
                  'password', 'last_login')


class UserRegitrationForm(forms.Form):
    email = forms.EmailField()
    full_name = forms.CharField(label='full name', max_length=255)
    phone = forms.CharField(max_length=11)
    password = forms.CharField(widget=forms.PasswordInput)


class VerifyCodeForm(forms.Form):
    code = forms.IntegerField()
