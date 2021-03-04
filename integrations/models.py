from django.db import models


class IntegrationData(models.Model):
    url_sufix = models.CharField(
        max_length=100,
        verbose_name='Sufixo do cliente',
        help_text="api.zapei.com.br/url_sufix"
    )
    token_zapei = models.TextField(
        verbose_name='Token Zapei',
        help_text="Na sua conta Zapei, clique em 'olá...' no canto superior direito, escolha integrações, e clique em Gerar Token"
    )

    def __str__(self):
        return self.client_name
