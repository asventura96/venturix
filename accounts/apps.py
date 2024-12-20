# accounts/apps.py

"""
Configuração do aplicativo 'accounts' para a aplicação Django.

Define a configuração padrão e o nome do aplicativo.
"""

from django.apps import AppConfig


class AccountsConfig(AppConfig):
    """
    Classe de configuração para o aplicativo 'accounts'.
    Define o campo de chave primária padrão e o nome do aplicativo.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
