from django import forms
from .models import Item
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('link','memo')
        widgets = {
            'link': forms.Textarea(attrs={'rows': 1}),
            'memo': forms.Textarea(attrs={'rows':4}),
                  }


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2','is_staff')