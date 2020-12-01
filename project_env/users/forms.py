from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms
from django.core.exceptions import ValidationError

class CreateUserForm(forms.ModelForm):
    password1 = forms.CharField(label="Password" ,widget=forms.PasswordInput(
        attrs={'class': 'alert alert-primary required'}
    ),
    required=True)
    password2 = forms.CharField(label="Password Confirmation",
    widget=forms.PasswordInput(
        attrs={'class': 'alert alert-primary required'}
    ), required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'age', 'profile_picture']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'alert alert-primary required'}),
            'email': forms.TextInput(attrs={'class': 'alert alert-primary required'}),
            'age': forms.Select(attrs={'class': "form-control"}),
            'first_name': forms.TextInput(attrs={'class': 'alert alert-warning'}),
            'last_name': forms.TextInput(attrs={'class': 'alert alert-warning'}),

        }
        
    def clean_password2(self):
        # chack that both password are the same
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords Don't Match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user



class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'alert alert-primary'}), max_length=20)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'alert alert-primary'}))