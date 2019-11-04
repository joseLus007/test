from django.db import models

class TimeStampedModel(models.Model):
    'so atualiza quando cria'
    created=models.DateTimeField('criado em',auto_now_add=True,auto_now=False)
    'atualiza data e hora quando voce altera '
    modified=models.DateTimeField('modificardo em',auto_now_add=False,auto_now=True)

    class Meta:
        abstract=True