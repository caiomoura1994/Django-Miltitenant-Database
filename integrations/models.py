from django.db import models


class RdStationZapei(models.Model):
    url_sufix = models.CharField(
        max_length=100,
        verbose_name='Sufixo do cliente',
        help_text="Acesse https://app.rdstation.com.br/integracoes/webhooks > clique em Criar Webhook > Escolha um nome, no campo GATILHO selecione: Conversão, no campo URL coloque: https://zapei-api.herokuapp.com/integracao/'Sufixo do cliente'/, Eventos de Conversão pode ficar Vazio"
    )
    token_zapei = models.TextField(
        verbose_name='Token Zapei',
        help_text="Acesse https://painel.zapei.com.br/admin/integrations > clique em Gerar Token"
    )

    class Meta:
        verbose_name = "Integração RdStationZapei"
        verbose_name_plural = "Integrações RdStationZapei"

    def __str__(self):
        return self.url_sufix
