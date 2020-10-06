from django.db import models

class TextoSite(models.Model):

    texto_principal = models.CharField(max_length=200, blank=True, null=True, verbose_name='Texto Principal')
    texto_secundario = models.CharField(max_length=200, blank=True, null=True, verbose_name='Texto Secundário')
    texto_3 = models.CharField(max_length=200, blank=True, null=True, verbose_name='Texto 03')
    texto_4 = models.CharField(max_length=200, blank=True, null=True, verbose_name='Texto 04')
    email = models.CharField(max_length=100, blank=True, null=True, verbose_name='E-Mail')
    instagran = models.CharField(max_length=100, blank=True, null=True, verbose_name='Instagram')
    twiter = models.CharField(max_length=100, blank=True, null=True, verbose_name='Twiter')
    facebook = models.CharField(max_length=100, blank=True, null=True, verbose_name='Facebook')
    telcelular = models.CharField(max_length=20, blank=True, null=True, verbose_name='Nº telefone celular')
    telfixo = models.CharField(max_length=20, blank=True, null=True, verbose_name='Nº telefone fixo')
    email = models.EmailField(blank=True, null=True, verbose_name='E-Mail')
    whatsapp = models.CharField(max_length=20, blank=True, null=True, verbose_name='Nº Whatsapp')
    endereco = models.CharField(max_length=200, blank=True, null=True, verbose_name='Endereço')
    dt_ultima_alteracao = models.DateField('Data Ultima Alterção', blank=True, null=True, auto_now=True)


    class Meta:
        verbose_name = 'Texto do Site'
        verbose_name_plural = 'Textos do Site'
