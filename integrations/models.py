from django.db import models


class RdStationZapei(models.Model):
    url_sufix = models.CharField(
        max_length=100,
        verbose_name='Sufixo do cliente',
        help_text="https://zapei-api.herokuapp.com/integracao/'Sufixo do cliente'/"
    )
    token_zapei = models.TextField(
        verbose_name='Token Zapei',
        help_text="Na sua conta Zapei, clique em 'olá...' no canto superior direito, escolha integrações, e clique em Gerar Token"
    )

    class Meta:
        verbose_name = "Integração"
        verbose_name_plural = "Integrações"

    def __str__(self):
        return self.url_sufix
