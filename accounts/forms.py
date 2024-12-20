# accounts/forms.py

"""
Este módulo contém os formulários utilizados para o aplicativo 'accounts'.
Ele define os formulários para cadastro, edição e outras operações relacionadas
às Contas de Usuários.
"""

from django import forms
from django.contrib.auth.forms import PasswordResetForm

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
