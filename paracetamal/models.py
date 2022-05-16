from django.db import models
from django.contrib.auth.models import User

class BigtableNomes(models.Model):
    id_principal = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=250)
    tipo_origem = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'bigtable'

    def __str__(self):
        return self.nome


class Usuario(User):
    pass