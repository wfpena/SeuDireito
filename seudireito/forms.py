# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from core.models import UserProfile


class UserLoginForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('username', 'password')
        widgets = {
            'username': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Nome de usuário'}),
            'password': forms.PasswordInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Senha'}),
        }
        labels = {
            'username': _(u'Usuário'),
            'password': _(u'Senha'),
        }

    # Validar/autenticar campos de login
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError(u"Usuário ou senha inválidos.")
        return self.cleaned_data

    def authenticate_user(self, username, password):
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError(u"Usuário ou senha inválidos.")
        return user

class UsuarioForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Senha'}),
        min_length=6, label='lock')
    confirm = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Confirme a senha'}),
        min_length=6, label='lock')
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Nome de usuário'}),
        label='person')
    email = forms.CharField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control line-input', 'placeholder': 'Email'}),
        label='email', required=False)

    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password',)
