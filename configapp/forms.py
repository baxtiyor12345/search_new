import re

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from .models import *


class NewsForm(forms.Form):
    title = forms.CharField(max_length=150, label="Nomi", widget=forms.TextInput(attrs={"class" : "form-control"}))
    context = forms.CharField(label="Text", required=False,
                              widget=forms.Textarea(attrs={"class" : "form-control", "rows": 5}))
    is_bool = forms.BooleanField(label="Nashr etish", initial=True)
    category = forms.ModelChoiceField(empty_label="Category tanlash", label="category",
                                      queryset=Categories.objects.all(),
                                      widget=forms.Select(attrs={"class": "form-control"}))

    def save(self):
        pass


class NewsForms(forms.ModelForm):
    class Meta:
        model = News
        # fields='__all__'
        fields = ['title', 'context', 'is_bool', 'category']
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'context': forms.TextInput(attrs={"class": "form-control", "rows": 5}),
            'select': forms.Select(attrs={"class": "form-control"})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValueError('Nomi raqam bilan boshlanmasligi kerak')
        return title


class SearchForm(forms.Form):
    query = forms.CharField(label="Qidiruv", max_length=200)

class UserLoginForm(AuthenticationForm):
    username=forms.CharField(label='login',widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(label='password',widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model=User
        fields=('username','password')

